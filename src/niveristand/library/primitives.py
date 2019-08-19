import time
from niveristand.errors import VeristandNotImplementedError


def abstime():
    """
    Returns the current date and time, in seconds, relative to the operating system's epoc.

    **Note**: Only available for RT sequences.
    """
    raise VeristandNotImplementedError()


def arraysize(x):
    """
    Returns the number of elements in x, where x is an array.

    Args:
        x: the array for which you want to get the number of elements.

    Returns:
        int: the size of the array. If **x** is not an array, this function returns 0.


    """
    if '__len__' in dir(x):
        return len(x)
    return 0


def clearfault(x):
    """
    Clears all faults set on channel x.

    Args:
        x: the channel you want to clear faults on.

    Channel `x` must be a reference to a channel and should not be a reference to a local variable.
    If `channel` references a local variable, :func:`clearfault` performs no operation.

    **Note**: Only available for RT sequences.

    """
    raise VeristandNotImplementedError()


def clearlasterror():
    """
    Clears the last error set by :func:`generate_error`.

    **Note**: Only available for RT sequences.
    """
    raise VeristandNotImplementedError()


def deltat():
    """
    Returns the duration, in seconds, of the current system timestep.

    To perform equality or comparison operations, use `deltatus`.

    **Note**: In Python Mode, this function always returns `0.01` for a rate of 100Hz.
    """
    return 0.01


def deltatus():
    """
    Returns the duration, in microseconds, of the current system timestep.

    **Note**: In Python Mode, this function always returns `10,000` for a rate of 100Hz.
    """
    return 10000


def fault(channel, value):
    """
    Faults `channel` with `value`.

    Args:
        channel: channel to fault.
        value(float): value to fault the channel.

    `channel` must be a reference to a channel and should not be a reference to a local variable.
    If `channel` references a local variable, :func:`fault` performs no operation.

    **Note**: Only available for RT sequences.

    """
    raise VeristandNotImplementedError()


def fix(x):
    """
    Rounds x to the nearest integer between x and zero.

    Args:
        x(float): value you want to round.

    Returns:
        (float): floating-point representation of the rounded value.

    **Note**: Only available for RT sequences.

    """
    raise VeristandNotImplementedError()


def getlasterror():
    """
    Returns the numeric error code of the last error set by :func:`generate_error`.

    **Note**: Only available for RT sequences.
    """
    raise VeristandNotImplementedError()


def iteration():
    """
    Returns the number of iterations since the current top-level sequence started.

    Returns:
        int: iteration count.

    """
    from niveristand.library._tasks import get_scheduler
    return get_scheduler().get_task_for_curr_thread().iteration_counter.count


def quotient(x, y):
    """
    Returns floor(x/y), the number of times y evenly divides into x.

    Args:
        x: dividend.
        y: divisor.

    Returns:
        int: integer quotient of x/y


    """
    return x // y


def rand(x):
    """
    Returns a random floating-point number between 0 and the maximum value.

    Args:
        x(float): maximum value.

    Returns:
        float: random number between 0 and `x`

    """
    from random import random
    return random() * x


def recip(x):
    """
    Returns 1/x.

    Args:
        x: divisor.

    **Note**: Only available for RT sequences.

    """
    raise VeristandNotImplementedError()


def rem(x, y):
    """
    Returns the remainder of x/y, when the quotient is rounded to the nearest integer.

    Args:
        x(float): dividend.
        y(float): divisor.

    """
    return x % y


def seqtime():
    """
    Returns the number of elapsed seconds since the epoch.

    Returns:
        float: time, in seconds, since the epoch.

    To perform equality or comparison operations, use `seqtimeus` instead.

    """
    return time.time()


def seqtimeus():
    """
    Returns the elapsed time, in microseconds, since the epoch.

    Returns:
        int: elapsed time, in microseconds, as reported by the system clock.

    """
    return int(time.time() * 10 ** 6)


def tickcountms():
    """
    Returns the current value of the milliseconds counter.

    Returns:
        int: time, in milliseconds, as reported by the high-precision counter (if available).

    """
    return int(time.clock() * 10 ** 3)


def tickcountus():
    """
    Returns the current value of the microseconds counter.

    Returns:
        int: time, in microseconds, as reported by the high-precision counter (if available).

    """
    return int(time.clock() * 10 ** 6)


def localhost_wait(amount=0.1):
    """
    Waits for channel values to update.

    Args:
        amount(float): time, in seconds, this function waits for channel values to update.

    When running in the VeriStand Engine, this function is ignored as channels are always up to date.

    """
    time.sleep(amount)


def generate_error(code, message, action):
    """
    Generates an error to report test failure.

    Args:
        code(int): error code to display.
        message(str): error string to display.
        action(:class:`niveristand.clientapi.ErrorAction`): action to perform.

    Returns:
        If action is Continue, returns the generated error.

    """
    from niveristand.clientapi._realtimesequencedefinitionapi.erroraction import ErrorAction
    from niveristand import errors
    from niveristand.library._tasks import get_scheduler
    assert isinstance(action, ErrorAction)
    error = errors.SequenceError(code, message, action)
    get_scheduler().get_task_for_curr_thread().error = error

    if action is ErrorAction.ContinueSequenceExecution:
        return error
    else:
        raise error
