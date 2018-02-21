from functools import wraps
import inspect
from niveristand.clientapi.datatypes import DataType
from niveristand.clientapi.datatypes import rtprimitives
from niveristand.exceptions import StopTaskException
from niveristand.library.tasks import get_scheduler, nivs_yield

rt_seq_mode_id = '__rtseq_mode__'


def nivs_rt_sequence(func):
    @wraps(func)
    def ret_func(*args, **kwargs):
        is_top_level = False
        task = get_scheduler().try_get_task_for_curr_thread()
        if task is None:
            is_top_level = True
            this_task = get_scheduler().create_task_for_curr_thread()
            get_scheduler().register_task(this_task)
        retval = func(*args, **kwargs)
        if is_top_level:
            get_scheduler().get_task_for_curr_thread().mark_stopped()
            nivs_yield()
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
    setattr(ret_func, rt_seq_mode_id, wrapped)


def _reconstruct_args(f, args, new_param):
    real_func = getattr(f, rt_seq_mode_id, f)
    new_args = list(args)
    arg_spec = inspect.getargspec(real_func)[0]

    if new_param is not None and new_param.param_name in arg_spec and new_param.by_value:
        idx = arg_spec.index(new_param.param_name)
        datatype_name = new_param.default_elem.__class__.__name__
        datatype = rtprimitives.get_class_by_name(datatype_name)
        if isinstance(args[idx], DataType):
            value = args[idx].value
        else:
            value = args[idx]
        new_args[idx] = datatype(value)
    return tuple(new_args)


def task(mt):
    def _add_task_to_list(func):

        @wraps(func)
        def _internal_task(task_info):
            # all tasks start waiting for their turn from the scheduler.
            task_info.wait_for_turn()
            try:
                return func()
            except StopTaskException:
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
