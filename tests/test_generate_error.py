import sys
from niveristand import decorators, RealTimeSequence
from niveristand.clientapi.datatypes import DoubleValue, I32Value
from niveristand.clientapi.realtimesequencedefinitionapi.erroraction import ErrorAction
from niveristand.exceptions import TranslateError, VeristandError
from niveristand.library.primitives import generate_error
from niveristand.library.tasks import multitask, nivs_yield
import pytest
from testutilities import rtseqrunner, validation


@decorators.nivs_rt_sequence
def _gen_stop():
    generate_error(-100, "Stop", ErrorAction.StopSequence)


@decorators.nivs_rt_sequence
def _gen_abort():
    generate_error(-200, "Abort", ErrorAction.AbortSequence)


@decorators.nivs_rt_sequence
def _gen_continue():
    generate_error(0, "Continue", ErrorAction.ContinueSequenceExecution)


@decorators.nivs_rt_sequence
def generate_error_simple():
    generate_error(1, "My Message", ErrorAction.ContinueSequenceExecution)


@decorators.nivs_rt_sequence
def generate_continue():
    try:
        a = DoubleValue(0)
        generate_error(0, "Continue", ErrorAction.ContinueSequenceExecution)
        a.value += 1
    finally:
        a.value += 1
    return a.value


@decorators.nivs_rt_sequence
def generate_stop():
    try:
        a = DoubleValue(0)
        generate_error(-5, "Stop", ErrorAction.StopSequence)
        a.value += 1
    finally:
        a.value += 1
    return a.value


@decorators.nivs_rt_sequence
def generate_abort():
    try:
        a = DoubleValue(0)
        generate_error(-5, "Abort", ErrorAction.AbortSequence)
        a.value += 1
    finally:
        a.value += 1
    return a.value


@decorators.nivs_rt_sequence
def generate_continue_mt():
    a = DoubleValue(0)
    with multitask() as mt:
        @decorators.task(mt)
        def f1():
            generate_error(0, "Continue", ErrorAction.ContinueSequenceExecution)

        @decorators.task(mt)
        def f2():
            nivs_yield()
            a.value = 1
    return a.value


@decorators.nivs_rt_sequence
def generate_stop_mt():
    a = DoubleValue(0)
    with multitask() as mt:
        @decorators.task(mt)
        def f1():
            generate_error(-1, "Stop", ErrorAction.StopSequence)

        @decorators.task(mt)
        def f2():
            nivs_yield()
            a.value = 1
    return a.value


@decorators.nivs_rt_sequence
def generate_abort_mt():
    a = DoubleValue(0)
    with multitask() as mt:
        @decorators.task(mt)
        def f1():
            generate_error(-2, "Abort", ErrorAction.AbortSequence)

        @decorators.task(mt)
        def f2():
            nivs_yield()
            a.value = 1
    return a.value


@decorators.nivs_rt_sequence
def generate_continue_subroutine():
    a = DoubleValue(1)
    _gen_continue()
    a.value = 5
    return a.value


@decorators.nivs_rt_sequence
def generate_continue_subroutine1():
    try:
        a = DoubleValue(0)
        _gen_continue()
        a.value += 1
    finally:
        a.value += 1
    return a.value


@decorators.nivs_rt_sequence
def generate_stop_subroutine():
    a = DoubleValue(1)
    _gen_stop()
    a.value = 5
    return a.value


@decorators.nivs_rt_sequence
def generate_stop_subroutine1():
    try:
        a = DoubleValue(0)
        _gen_stop()
        a.value += 1
    finally:
        a.value += 1
    return a.value


@decorators.nivs_rt_sequence
def generate_abort_subroutine():
    a = DoubleValue(1)
    _gen_abort()
    a.value = 5
    return a.value


@decorators.nivs_rt_sequence
def generate_abort_subroutine1():
    try:
        a = DoubleValue(0)
        _gen_abort()
        a.value += 1
    finally:
        a.value += 1
    return a.value


@decorators.nivs_rt_sequence
def invalid_error_code():
    a = I32Value(-1)
    generate_error(a.value, "Message", ErrorAction.AbortSequence)


@decorators.nivs_rt_sequence
def invalid_error_message():
    generate_error(-1, 22, ErrorAction.AbortSequence)


@decorators.nivs_rt_sequence
def invalid_error_action():
    generate_error(1, "Message", 1)


run_tests = [
    (generate_error_simple, (), None),
    (generate_continue, (), 2),
    (generate_stop, (), 1),
    (generate_abort, (), 0),
    (generate_continue_mt, (), 1),
    (generate_stop_mt, (), 0),
    (generate_abort_mt, (), 0),
    (generate_continue_subroutine, (), 5),
    (generate_continue_subroutine1, (), 2),
    (generate_stop_subroutine, (), 1),
    (generate_stop_subroutine1, (), 1),
    (generate_abort_subroutine, (), 1),
    (generate_abort_subroutine1, (), 0),
]

skip_tests = [
]

fail_transform_tests = [
    (invalid_error_code, (), TranslateError),
    (invalid_error_message, (), TranslateError),
    (invalid_error_action, (), TranslateError),
]


def idfunc(val):
    return val.__name__


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.skip("Python implementation of builtins missing")
@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    try:
        RealTimeSequence(func_name)
    except expected_result:
        pass
    except VeristandError as e:
        pytest.fail('Unexpected exception raised:' +
                    str(e.__class__) + ' while expected was: ' + expected_result.__name__)
    except Exception as exception:
        pytest.fail('ExpectedException not raised: ' + str(exception))


@pytest.mark.parametrize("func_name, params, reason", skip_tests, ids=idfunc)
def test_skipped(func_name, params, reason):
    pytest.skip(func_name.__name__ + ": " + reason)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
