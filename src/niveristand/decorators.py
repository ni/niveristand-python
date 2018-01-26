from functools import wraps

rt_seq_mode_id = '__rtseq_mode__'


def nivs_rt_sequence(func):
    @wraps(func)
    def ret_func(*args, **kwargs):
        return func(*args, **kwargs)

    wrapped = getattr(func, rt_seq_mode_id, None)
    if wrapped is None:
        wrapped = func
    setattr(ret_func, rt_seq_mode_id, wrapped)
    return ret_func
