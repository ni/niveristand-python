import time
from niveristand.errors import VeristandNotImplementedError


def abstime():
    """
    Return the current date and time in seconds relative to the operating system's epoc.

    **Note**: Only available for Real-Time Sequences. @TODODOC
    """
    raise VeristandNotImplementedError()


def arraysize(x):
    """
    Return the number of elements in x, where x is an array.

    Args:
        x: the array.

    Returns:
        int: The size of the array. If the element is not an array, 0.


    """
    if '__len__' in dir(x):
        return len(x)
    return 0


def clearfault(x):
    """
    Clear any fault set on channel x.

    Args:
        x: the channel to clear the fault on.

    `channel` must be a reference to a channel and should not be a reference to a local variable.
    If `channel` references a local variable, :func:`clearfault` performs no operation.

    **Note**: Only available for Real-Time Sequences. @TODODOC
    """
    raise VeristandNotImplementedError()


def clearlasterror():
    """
    Clear the last error set by :func:`generate_error`.

    **Note**: Only available for Real-Time Sequences. @TODODOC
    """
    raise VeristandNotImplementedError()


def deltat():
    """
    Return the duration of the current system timestep in seconds.

    To perform equality or comparison operations, use deltatus instead.

    **Note**: Only available for Real-Time Sequences. @TODODOC
    """
    raise VeristandNotImplementedError()


def deltatus():
    """
    Return the duration of the current system timestep in microseconds.

    **Note**: Only available for Real-Time Sequences. @TODODOC
    """
    raise VeristandNotImplementedError()


def fault(channel, value):
    """
    Fault `channel` with `value`.

    Args:
        channel: the channel to fault
        value(float): the value to fault the channel

    `channel` must be a reference to a channel and should not be a reference to a local variable.
    If `channel` references a local variable, :func:`fault` performs no operation.

    **Note**: Only available for Real-Time Sequences. @TODODOC
    """
    raise VeristandNotImplementedError()


def fix(x):
    """
    Round x to the nearest integer between x and zero.

    Args:
        x(float): the value

    Returns:
        (float): the floating-point representation of the rounded value.

    **Note**: Only available for Real-Time Sequences. @TODODOC

    """
    raise VeristandNotImplementedError()


def getlasterror():
    """
    Return the numeric error code of the last error set by :func:`generate_error`.

    **Note**: Only available for Real-Time Sequences. @TODODOC
    """
    raise VeristandNotImplementedError()


def iteration():
    """
    Return the number of iterations since the current top-level sequence started.

    Returns:
        int: iteration count.

    """
    from niveristand.library._tasks import get_scheduler
    return get_scheduler().get_task_for_curr_thread().iteration_counter.count


def quotient(x, y):
    """
    Return floor(x/y), the number of times y evenly divides into x.

    Args:
        x: dividend.
        y: divisor.

    Returns:
        int: integer quotient of x/y


    """
    return x // y


def recip(x):
    """
    Return 1/x.

    Args:
        x: the divisor.

    **Note**: Only available for Real-Time Sequences. @TODODOC
    """
    raise VeristandNotImplementedError()


def rem(x, y):
    """
    Return the remainder of x/y, when the quotient is rounded to the nearest integer.

    Args:
        x(float): the dividend.
        y(float): the divisor

    **Note**: Only available for Real-Time Sequences. @TODODOC
    """
    raise VeristandNotImplementedError()


def seqtime():
    """
    Return the number of elapsed seconds since the epoc.

    Returns:
        float: number of seconds since the epoc.

    To perform equality or comparison operations, use seqtimeus instead.

    """
    return time.time()


def seqtimeus():
    """
    Return the number of elapsed microseconds since the epoc.

    Returns:
        int: number of microseconds as reported by the system clock.

    """
    return int(time.time() * 10 ** 6)


def tickcountms():
    """
    Return the current value of the milliseconds counter.

    Returns:
        int: number of milliseconds as reported by high-precision counter (if available)

    """
    return int(time.clock() * 10 ** 3)


def tickcountus():
    """
    Return the current value of the microseconds counter.

    Returns:
        int: number of microseconds as reported by high-precision counter (if available)

    """
    return int(time.clock() * 10 ** 6)


def localhost_wait(amount=0.1):
    """
    Wait for channel values to be updated.

    Args:
        amount(float): seconds to wait for update.

    When running in the VeriStand Engine this fuction will be ignored, as channels are always up to date.

    """
    time.sleep(amount)


def generate_error(code, message, action):
    """
    Generate an error to report test failure.

    Args:
        code(int): error code.
        message(str):
        action(:class:`niveristand.clientapi.ErrorAction`): action to perform.

    Returns:
        If action is Continue returns the generated error.

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
