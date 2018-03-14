import time
from niveristand._exceptions import VeristandNotImplementedError


def abstime():
    raise VeristandNotImplementedError()


def arraysize(x):
    raise VeristandNotImplementedError()


def clearfault(x):
    raise VeristandNotImplementedError()


def clearlasterror():
    raise VeristandNotImplementedError()


def deltat():
    raise VeristandNotImplementedError()


def deltatus():
    raise VeristandNotImplementedError()


def fault(channel, value):
    raise VeristandNotImplementedError()


def fix(x):
    raise VeristandNotImplementedError()


def getlasterror():
    raise VeristandNotImplementedError()


def iteration():
    from niveristand.library._tasks import get_scheduler
    return get_scheduler().get_task_for_curr_thread().iteration_counter.count


def quotient(x, y):
    return x // y


def recip(x):
    raise VeristandNotImplementedError()


def rem(x, y):
    raise VeristandNotImplementedError()


def seqtime():
    return time.time()


def seqtimeus():
    return int(time.time() * 10 ** 6)


def tickcountms():
    return int(time.clock() * 10 ** 3)


def tickcountus():
    return int(time.clock() * 10 ** 6)


def localhost_wait(amount=0.1):
    time.sleep(amount)


def generate_error(code, message, action):
    from niveristand.clientapi._realtimesequencedefinitionapi.erroraction import ErrorAction
    from niveristand import _exceptions
    from niveristand.library._tasks import get_scheduler
    assert isinstance(action, ErrorAction)
    error = _exceptions.SequenceError(code, message, action)
    get_scheduler().get_task_for_curr_thread().error = error

    if action is ErrorAction.ContinueSequenceExecution:
        return error
    else:
        raise error
