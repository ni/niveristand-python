import sys
from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import DoubleValue, I32Value
from niveristand.clientapi import ErrorAction, RealTimeSequence
from niveristand.errors import RunAbortedError, RunError, RunFailedError, SequenceError, TranslateError
from niveristand.library import multitask, nivs_yield, task
from niveristand.library.primitives import generate_error
import pytest
from testutilities import rtseqrunner, validation

_stop_err = SequenceError(-100, "Stop", ErrorAction.StopSequence)
_abort_err = SequenceError(-200, "Abort", ErrorAction.AbortSequence)
_cont_err = SequenceError(1, "Continue", ErrorAction.ContinueSequenceExecution)
_cont_err_no_fail = SequenceError(0, "Continue", ErrorAction.ContinueSequenceExecution)


@nivs_rt_sequence
def _gen_stop():
    generate_error(-100, "Stop", ErrorAction.StopSequence)


@nivs_rt_sequence
def _gen_abort():
    generate_error(-200, "Abort", ErrorAction.AbortSequence)


@nivs_rt_sequence
def _gen_continue():
    generate_error(1, "Continue", ErrorAction.ContinueSequenceExecution)


@nivs_rt_sequence
def generate_error_simple():
    generate_error(1, "Continue", ErrorAction.ContinueSequenceExecution)


@nivs_rt_sequence
def generate_continue():
    try:
        a = DoubleValue(0)
        generate_error(1, "Continue", ErrorAction.ContinueSequenceExecution)
        a.value += 1
    finally:
        a.value += 1
    return a.value


@nivs_rt_sequence
def _generate_continue_no_fail():
    try:
        a = DoubleValue(0)
        generate_error(0, "Continue", ErrorAction.ContinueSequenceExecution)
        a.value += 1
    finally:
        a.value += 1
    return a.value


@nivs_rt_sequence
def generate_stop():
    try:
        a = DoubleValue(0)
        generate_error(-100, "Stop", ErrorAction.StopSequence)
        a.value += 1
    finally:
        a.value += 1
    return a.value


@nivs_rt_sequence
def generate_abort():
    try:
        a = DoubleValue(0)
        generate_error(-200, "Abort", ErrorAction.AbortSequence)
        a.value += 1
    finally:
        a.value += 1
    return a.value


@nivs_rt_sequence
def generate_continue_mt():
    a = DoubleValue(0)
    with multitask() as mt:
        @task(mt)
        def f1():
            generate_error(1, "Continue", ErrorAction.ContinueSequenceExecution)

        @task(mt)
        def f2():
            nivs_yield()
            a.value = 1
    return a.value


@nivs_rt_sequence
def generate_stop_mt():
    a = DoubleValue(0)
    with multitask() as mt:
        @task(mt)
        def f1():
            generate_error(-100, "Stop", ErrorAction.StopSequence)

        @task(mt)
        def f2():
            nivs_yield()
            a.value = 1
    return a.value


@nivs_rt_sequence
def generate_abort_mt():
    a = DoubleValue(0)
    with multitask() as mt:
        @task(mt)
        def f1():
            generate_error(-200, "Abort", ErrorAction.AbortSequence)

        @task(mt)
        def f2():
            nivs_yield()
            a.value = 1
    return a.value


@nivs_rt_sequence
def generate_continue_subroutine():
    a = DoubleValue(1)
    _gen_continue()
    a.value = 5
    return a.value


@nivs_rt_sequence
def generate_continue_subroutine1():
    try:
        a = DoubleValue(0)
        _gen_continue()
        a.value += 1
    finally:
        a.value += 1
    return a.value


@nivs_rt_sequence
def generate_stop_subroutine():
    a = DoubleValue(1)
    _gen_stop()
    a.value = 5
    return a.value


@nivs_rt_sequence
def generate_stop_subroutine1():
    try:
        a = DoubleValue(0)
        _gen_stop()
        a.value += 1
    finally:
        a.value += 1
    return a.value


@nivs_rt_sequence
def generate_abort_subroutine():
    a = DoubleValue(1)
    _gen_abort()
    a.value = 5
    return a.value


@nivs_rt_sequence
def generate_abort_subroutine1():
    try:
        a = DoubleValue(0)
        _gen_abort()
        a.value += 1
    finally:
        a.value += 1
    return a.value


@nivs_rt_sequence
def invalid_error_code():
    a = I32Value(-1)
    generate_error(a.value, "Message", ErrorAction.AbortSequence)


@nivs_rt_sequence
def invalid_error_message():
    generate_error(-1, 22, ErrorAction.AbortSequence)


@nivs_rt_sequence
def invalid_error_action():
    generate_error(1, "Message", 1)


@nivs_rt_sequence
def generate_multiple_errors():
    _gen_continue()
    _gen_continue()
    _gen_continue()
    _gen_stop()


@nivs_rt_sequence
def generate_multiple_errors1():
    try:
        _gen_continue()
        _gen_stop()
        _gen_continue()
    finally:
        _gen_continue()


@nivs_rt_sequence
def generate_multiple_errors2():
    _gen_continue()
    _gen_abort()
    _gen_continue()
    _gen_continue()


run_tests = [
    (generate_error_simple, (), (None, (_cont_err,))),
    (generate_continue, (), (2, (_cont_err,))),
    (generate_stop, (), (1, (_stop_err,))),
    (generate_abort, (), (0, (_abort_err,))),
    (generate_continue_mt, (), (1, (_cont_err,))),
    (generate_stop_mt, (), (0, (_stop_err,))),
    (generate_abort_mt, (), (0, (_abort_err,))),
    (generate_continue_subroutine, (), (5, (_cont_err,))),
    (generate_continue_subroutine1, (), (2, (_cont_err,))),
    (generate_stop_subroutine, (), (1, (_stop_err,))),
    (generate_stop_subroutine1, (), (1, (_stop_err,))),
    (generate_abort_subroutine, (), (1, (_abort_err,))),
    (generate_abort_subroutine1, (), (0, (_abort_err,))),
    (generate_multiple_errors, (), (None, (_stop_err, _cont_err, _cont_err, _cont_err))),
    (generate_multiple_errors1, (), (None, (_cont_err, _stop_err, _cont_err))),
    (generate_multiple_errors2, (), (None, (_abort_err, _cont_err))),
]

fail_transform_tests = [
    (invalid_error_code, (), TranslateError),
    (invalid_error_message, (), TranslateError),
    (invalid_error_action, (), TranslateError),
]

run_as_rts_tests = [
    (generate_error_simple, (), RunFailedError),
    (generate_continue, (), RunFailedError),
    (generate_stop, (), RunAbortedError),
    (generate_abort, (), RunAbortedError),
    (generate_continue_mt, (), RunFailedError),
    (generate_stop_mt, (), RunAbortedError),
    (generate_abort_mt, (), RunAbortedError),
    (generate_continue_subroutine, (), RunFailedError),
    (generate_continue_subroutine1, (), RunFailedError),
    (generate_stop_subroutine, (), RunAbortedError),
    (generate_stop_subroutine1, (), RunAbortedError),
    (generate_abort_subroutine, (), RunAbortedError),
    (generate_abort_subroutine1, (), RunAbortedError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


def test_gen_continue_no_fail():
    assert _generate_continue_no_fail() == 2
    assert rtseqrunner.run_rtseq_in_VM(_generate_continue_no_fail) == 2
    assert realtimesequencetools.run_py_as_rtseq(_generate_continue_no_fail) == 2


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    expected_value, expected_errors = expected_result
    with pytest.raises(RunError) as e:
        func_name(*params)
    if e.value.error.error_action in (ErrorAction.AbortSequence, ErrorAction.StopSequence):
        assert isinstance(e.value, RunAbortedError)
    else:
        assert isinstance(e.value, RunFailedError)
    all_errors = list(e.value.get_all_errors())
    for error, expected_error in zip(all_errors, expected_errors):
        assert error.error_code == expected_error.error_code
        assert error.error_action == expected_error.error_action
        assert error.message == expected_error.message


@pytest.mark.parametrize("func_name, params, expected_result", run_as_rts_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    with pytest.raises(expected_result):
        realtimesequencetools.run_py_as_rtseq(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result[0]


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
