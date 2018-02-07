from functools import wraps
import inspect
from niveristand.clientapi.datatypes import DataType
from niveristand.clientapi.datatypes import rtprimitives

rt_seq_mode_id = '__rtseq_mode__'


def nivs_rt_sequence(func):
    return _wrap_helper(func, None)


class NivsParam:
    BY_REF = False
    BY_VALUE = True

    def __init__(self, param_name, default_elem, by_value):
        self.param_name = param_name
        self.default_elem = default_elem
        self.by_value = by_value

    def __call__(self, f):
        return _wrap_helper(f, self)


def _wrap_helper(func, param):
    @wraps(func)
    def ret_func(*args, **kwargs):
        args = _reconstruct_args(func, args, param)
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
