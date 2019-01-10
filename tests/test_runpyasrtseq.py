import sys
import threading
from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import DoubleValue, ErrorAction, RealTimeSequence
from niveristand.errors import RunAbortedError, RunFailedError, TranslateError
from niveristand.library import generate_error
from niveristand.library._tasks import get_scheduler
import pytest
from testutilities import validation


@nivs_rt_sequence
def return_var():
    a = DoubleValue(5)
    return a.value


@nivs_rt_sequence
def _increment(a):
    a.value += 1
    return a.value


@nivs_rt_sequence
def sub_routine_caller():
    a = DoubleValue(5)
    _increment(a)
    return a.value


@nivs_rt_sequence
def invalid_sequence():
    a = DoubleValue(5)
    a += 1
    return a


@nivs_rt_sequence
def return_void():
    a = DoubleValue(5)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def generate_error_continue():
    generate_error(1, "Continue", ErrorAction.ContinueSequenceExecution)


@nivs_rt_sequence
def generate_error_stop():
    generate_error(2, "Stop", ErrorAction.StopSequence)


@nivs_rt_sequence
def generate_error_abort():
    generate_error(3, "Abort", ErrorAction.AbortSequence)


run_tests = [
    (return_var, (), 5),
    (sub_routine_caller, (), 6),
    (return_void, (), None),
]


fail_transform_tests = [
    (invalid_sequence, (), TranslateError),
    (generate_error_continue, (), RunFailedError),
    (generate_error_stop, (), RunAbortedError),
    (generate_error_abort, (), RunAbortedError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


def test_not_wait_to_complete():
    seq = RealTimeSequence(return_var)
    result_state = seq.run(False)
    assert result_state.ret_val is None
    result_state.wait_for_result()
    assert result_state.ret_val == 5


def test_run_multiple_top_level_seqs():
    assert len(get_scheduler()._task_dict) is 0
    for func, params, expected in run_tests:
        actual = realtimesequencetools.run_py_as_rtseq(func)
        assert actual == expected
        # check that the scheduler is empty after every run.
        assert len(get_scheduler()._task_dict) is 0


def test_run_multiple_top_level_seqs_in_parallel():
    threads = list()
    thread_results = dict()
    for func, params, expected in run_tests:
        thread_results[func] = expected

        def run_func_helper(func):
            actual = realtimesequencetools.run_py_as_rtseq(func)
            thread_results[func] = (thread_results[func], actual)

        thread = threading.Thread(target=run_func_helper, name=func.__name__, args=(func,))
        threads.append(thread)
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    for func, results in thread_results.items():
        assert results[0] == results[1], "Func: %s failed assert" % func.__name__


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        realtimesequencetools.run_py_as_rtseq(func_name)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
