from functools import wraps
import inspect
from niveristand import _errormessages, errors
from niveristand.clientapi._datatypes import DataType
from niveristand.clientapi._datatypes import rtprimitives

rt_seq_mode_id = '__rtseq_mode__'


def nivs_rt_sequence(func):
    from niveristand.library._tasks import get_scheduler, nivs_yield

    @wraps(func)
    def ret_func(*args, **kwargs):
        is_top_level = False
        this_task = get_scheduler().try_get_task_for_curr_thread()
        if this_task is None:
            is_top_level = True
            this_task = get_scheduler().create_and_register_task_for_top_level()
            get_scheduler().sched()
            this_task.wait_for_turn()
        try:
            if is_top_level:
                from niveristand.clientapi import RealTimeSequence
                RealTimeSequence(func)
            retval = func(*args, **kwargs)
        except errors._SequenceError:
            # generate error already saved this error in the task, so we can just pass.
            pass
        finally:
            if is_top_level:
                this_task.mark_stopped()
                this_task.iteration_counter.finished = True
                nivs_yield()
                if this_task.error and this_task.error.should_raise:
                    raise errors.RunError.RunErrorFactory(this_task.error)
        return retval

    _set_rtseq_attrs(func, ret_func)
    return ret_func


class NivsParam:
    BY_REF = False
    BY_VALUE = True

    def __init__(self, param_name, default_elem, by_value):
        self.param_name = param_name
        self.default_elem = default_elem
        self.by_value = by_value

    def __call__(self, func):
        @wraps(func)
        def ret_func(*args, **kwargs):
            args = _reconstruct_args(func, args, self)
            return func(*args, **kwargs)

        _set_rtseq_attrs(func, ret_func)
        return ret_func


def _set_rtseq_attrs(func, ret_func):
    wrapped = getattr(func, rt_seq_mode_id, None)
    if wrapped is None:
        wrapped = func
        setattr(func, rt_seq_mode_id, wrapped)
    setattr(ret_func, rt_seq_mode_id, wrapped)


def _reconstruct_args(f, args, new_param):
    real_func = getattr(f, rt_seq_mode_id, f)
    new_args = list(args)
    arg_spec = inspect.getargspec(real_func)[0]

    if new_param is not None:
        if new_param.param_name in arg_spec:
            idx = arg_spec.index(new_param.param_name)
            datatype_name = new_param.default_elem.__class__.__name__
            datatype = rtprimitives.get_class_by_name(datatype_name)
            if new_param.by_value:
                if isinstance(args[idx], DataType):
                    value = args[idx].value
                else:
                    value = args[idx]
                new_args[idx] = datatype(value)
            else:
                if not isinstance(args[idx], DataType):
                    value = args[idx]
                    new_args[idx] = datatype(value)
        else:
            raise errors.VeristandError(_errormessages.param_description_no_param)

    return tuple(new_args)


def task(mt):
    """
    Mark a nested function-definition as a task inside a :func:`niveristand.library.multitask`.

    Args:
        mt: the parent :func:`niveristand.library.multitask`

    This function is meant to be used as a decorator.
    Refer to :ref:`_multitask_usage` for more details on using tasks.

    """
    def _add_task_to_list(func):
        from niveristand.library._tasks import nivs_yield

        @wraps(func)
        def _internal_task(task_info):
            # all tasks start waiting for their turn from the scheduler.
            task_info.wait_for_turn()
            try:
                return func()
            except (errors._StopTaskException, errors._SequenceError):
                pass
            finally:
                # if the task was stopped or it finished execution mark it stopped, then yield.
                # It won't get scheduled again, and the thread will be marked finished.
                task_info.mark_stopped()
                nivs_yield()

        mt.add_func(_internal_task)
        # return the original function, since we already added the wrapped one to the mt.
        # this allows the user to call it normally if they choose outside an mt context.
        return func
    return _add_task_to_list


_VALID_DECORATORS = {
    nivs_rt_sequence.__name__: nivs_rt_sequence,
    NivsParam.__name__: NivsParam,
    task.__name__: task,
}
