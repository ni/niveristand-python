from functools import wraps

rt_seq_mode_id = '__rtseq_mode__'


class Modes:
    """
    The different modes an RT Sequence can operate on.

    Technically this should have been an enum, but enum doesn't exist
    in python 2.7
    """

    CHECK = 1
    UNWRAP = 2


def nivs_rt_sequence(func):
    @wraps(func)
    def ret_func(*args, **kwargs):
        if kwargs[rt_seq_mode_id] is not None:
            if kwargs[rt_seq_mode_id] is Modes.UNWRAP:
                # when using inspect.getsource in combination with @wraps
                # python 2.7 fails to parse the decorated function.
                # This block of code unwraps the function if it gets called,
                # and it allows us to support any decorator that implements
                # this dual-mode behavior.
                return func
            elif kwargs[rt_seq_mode_id] is Modes.CHECK:
                # In CHECK mode, just return True to signal that we are
                # indeed a valid rtseq wrapper.
                return True

        return func(*args, **kwargs)

    return ret_func
