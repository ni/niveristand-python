import sys
import threading
from niveristand import nivs_rt_sequence, NivsParam
from niveristand import realtimesequencetools
from niveristand.clientapi import I32Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
from niveristand.library import multitask, nivs_yield, task
from niveristand.library._tasks import get_scheduler
import pytest
from testutilities import rtseqrunner, validation


@NivsParam('param', I32Value(0), NivsParam.BY_REF)
@nivs_rt_sequence
def _increase_param_by_ref(param):
    param.value += 1


@NivsParam('param', I32Value(0), NivsParam.BY_REF)
@nivs_rt_sequence
def _subseq_with_multitask(param):
    with multitask() as mt:
        @task(mt)
        def fa():
            nivs_yield()
            if param.value is 2:
                param.value = 3

        @task(mt)
        def fb():
            if param.value is 0:
                param.value = 1


@nivs_rt_sequence
def multitask_pass():
    a = I32Value(1)
    with multitask() as mt:
        @task(mt)
        def f1():
            pass

        @task(mt)
        def f2():
            pass
    return a.value


@nivs_rt_sequence
def multitask_access_local():
    a = I32Value(0)
    with multitask() as mt:
        @task(mt)
        def f1():
            a.value = 5

        @task(mt)
        def f2():
            a.value *= 7
    return a.value


@nivs_rt_sequence
def multitask_blocks_until_done():
    a = I32Value(0)
    with multitask() as mt:
        @task(mt)
        def f1():
            nivs_yield()
            a.value = 1

        @task(mt)
        def f2():
            a.value = 2
            nivs_yield()
    if a.value is not 1:
        a.value = -1
    return a.value


@nivs_rt_sequence
def multitask_nested():
    a = I32Value(0)
    with multitask() as mt:
        @task(mt)
        def f1():
            with multitask() as mt_inside:
                @task(mt_inside)
                def fa():
                    a.value = 5

                @task(mt_inside)
                def fb():
                    a.value *= 7

        @task(mt)
        def f2():
            a.value *= 13

    return a.value


@nivs_rt_sequence
def multitask_task_with_yield():
    a = I32Value(0)
    with multitask() as mt:
        @task(mt)
        def f1():
            nivs_yield()
            a.value = 1

        @task(mt)
        def f2():
            a.value = 2
            nivs_yield()
    return a.value


@nivs_rt_sequence
def multitask_tasks_with_different_iter_count():
    a = I32Value(0)
    ret = I32Value(1)
    with multitask() as mt:
        @task(mt)
        def f1():
            while a.value < 15:
                a.value += 1
                if a.value % 2 is not 1 and a.value < 10:
                    ret.value = a.value * -1
                nivs_yield()

        @task(mt)
        def f2():
            while a.value < 10:
                a.value += 1
                if a.value % 2 is not 0:
                    ret.value = a.value * -1
                if a.value > 10:
                    ret.value -= 100
                nivs_yield()
    ret.value *= a.value
    return ret.value


@nivs_rt_sequence
def multitask_nested_validate_order():
    a = I32Value(0)
    counter = I32Value(1000)
    ret = I32Value(0)
    with multitask() as mt_top:
        @task(mt_top)
        def fa():
            with multitask() as mt_nested:
                @task(mt_nested)
                def f0():
                    with multitask() as mt_bottom:
                        @task(mt_bottom)
                        def fx():
                            if a.value is not 0:
                                ret.value = -1000
                            while counter.value > 0:
                                counter.value -= 1
                                nivs_yield()

                @task(mt_nested)
                def f1():
                    if a.value > 3 and ret.value == 0:
                        ret.value = -1
                    a.value += 1
                    nivs_yield()
                    if a.value > 303 and ret.value == 0:
                        ret.value = -100
                    a.value += 100
                    nivs_yield()

                @task(mt_nested)
                def f2():
                    if a.value > 3 and ret.value == 0:
                        ret.value = -2
                    a.value += 1
                    nivs_yield()
                    if a.value > 303 and ret.value == 0:
                        ret.value = -200
                    a.value += 100
                    nivs_yield()

        @task(mt_top)
        def fb():
            if a.value > 3 and ret.value == 0:
                ret.value = -3
            a.value += 1
            nivs_yield()
            if a.value > 303 and ret.value == 0:
                ret.value = -300
            a.value += 100
            nivs_yield()

        @task(mt_top)
        def fc():
            while counter.value > 0:
                counter.value -= 1
                nivs_yield()

    if counter.value is not 0:
        ret.value -= 10000
    return ret.value


@nivs_rt_sequence
def multitask_multiple_in_sequence_validate_order():
    a = I32Value(0)
    with multitask() as mt:
        @task(mt)
        def f1():
            nivs_yield()
            if a.value is 1:
                a.value = 2

        @task(mt)
        def f2():
            if a.value is 0:
                a.value = 1
            nivs_yield()

    with multitask() as mt2:
        @task(mt2)
        def fa():
            nivs_yield()
            if a.value is 3:
                a.value = 4

        @task(mt2)
        def fb():
            if a.value is 2:
                a.value = 3
            nivs_yield()

    return a.value


@nivs_rt_sequence
def multitask_call_subroutine_params_by_ref():
    a = I32Value(0)
    b = I32Value(1)
    with multitask() as mt:
        @task(mt)
        def f1():
            _increase_param_by_ref(a)

        @task(mt)
        def f2():
            _increase_param_by_ref(b)

        @task(mt)
        def f3():
            a.value += b.value
    return a.value


@nivs_rt_sequence
def multitask_call_subroutine_with_multitask():
    a = I32Value(0)

    with multitask() as mt:
        @task(mt)
        def f1():
            _subseq_with_multitask(a)
            nivs_yield()
            if a.value is 3:
                a.value = 4

        @task(mt)
        def f2():
            if a.value is 1:
                a.value = 2
            nivs_yield()
            nivs_yield()
            nivs_yield()
            if a.value is 4:
                a.value = 5

    return a.value


@nivs_rt_sequence
def multitask_duplicate_name_fails():
    a = I32Value(0)
    with multitask() as mt:
        @task(mt)
        def f1():
            a.value = 1

        @task(mt)  # noqa: F811 redefinition is exactly what we're testing here.
        def f1():
            a.value = 2
    return a.value


@nivs_rt_sequence
def multitask_redefine_var_fails():
    a = I32Value(0)
    with multitask() as mt:
        @task(mt)
        def f1():
            a = I32Value(1)
            a.value = 2
    return a.value


@nivs_rt_sequence
def multitask_return_fails():
    a = I32Value(0)
    with multitask() as mt:
        @task(mt)
        def f1():
            a = I32Value(1)
            a.value = 2
        return a.value


@nivs_rt_sequence
def multitask_stmt_fails():
    a = I32Value(0)
    with multitask() as mt:
        @task(mt)
        def f1():
            a = I32Value(1)
            a.value = 2
        return a.value


@nivs_rt_sequence
def multitask_with_param_fails():
    a = I32Value(1)
    with multitask(a) as mt:
        @task(mt)
        def f1():
            pass

        @task(mt)
        def f2():
            pass
    return a.value


@nivs_rt_sequence
def multitask_task_with_param_fails():
    a = I32Value(1)
    with multitask(a) as mt:
        @task(mt)
        def f1(x):
            pass

        @task(mt)
        def f2():
            pass
    return a.value


@nivs_rt_sequence
def multitask_return_in_task_fails():
    a = I32Value(0)
    with multitask() as mt:
        @task(mt)
        def f1():
            a = I32Value(1)
            return a.value
    return a.value


@nivs_rt_sequence
def multitask_funcdef_in_task_fails():
    a = I32Value(0)
    with multitask() as mt:
        @task(mt)
        def f1():
            def func():
                pass
    return a.value


@nivs_rt_sequence
def multitask_no_var_name_fails():
    a = I32Value(0)
    with multitask():
        @task()
        def f1():
            pass
    return a.value


@nivs_rt_sequence
def multitask_wrong_var_name_fails():
    a = I32Value(0)
    with multitask():
        @task(a)
        def f1():
            pass
    return a.value


@nivs_rt_sequence
def multitask_task_multi_dec_fails():
    a = I32Value(0)
    with multitask() as mt:
        @task(mt)
        @task(mt)
        def f1():
            pass
    return a.value


run_tests = [
    (multitask_pass, (), 1),
    (multitask_nested, (), 455),
    (multitask_access_local, (), 35),
    (multitask_blocks_until_done, (), 1),
    (multitask_task_with_yield, (), 1),
    (multitask_call_subroutine_params_by_ref, (), 3),
    (multitask_tasks_with_different_iter_count, (), 15),
    (multitask_nested_validate_order, (), 0),
    (multitask_multiple_in_sequence_validate_order, (), 4),
    (multitask_call_subroutine_with_multitask, (), 5),
]

fail_transform_tests = [
    (multitask_duplicate_name_fails, (), VeristandError),
    (multitask_return_fails, (), TranslateError),
    (multitask_stmt_fails, (), TranslateError),
    (multitask_with_param_fails, (), TranslateError),
    (multitask_task_with_param_fails, (), TranslateError),
    (multitask_return_in_task_fails, (), TranslateError),
    (multitask_funcdef_in_task_fails, (), TranslateError),
    (multitask_no_var_name_fails, (), TranslateError),
    (multitask_wrong_var_name_fails, (), TranslateError),
    (multitask_task_multi_dec_fails, (), TranslateError),
    (multitask_redefine_var_fails, (), TranslateError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


def test_run_multiple_top_level_seqs():
    assert len(get_scheduler()._task_dict) == 0
    for func, params, expected in run_tests:
        actual = func(*params)
        assert actual == expected
        # check that there are no tasks left to run
        assert len(get_scheduler()._task_dict) == 0


def test_run_multiple_top_level_seqs_in_parallel():
    assert len(get_scheduler()._task_dict) == 0
    threads = list()
    thread_results = dict()
    for func, params, expected in run_tests:
        thread_results[func] = expected

        def run_func_helper(func):
            actual = func()
            thread_results[func] = (thread_results[func], actual)

        thread = threading.Thread(target=run_func_helper, name=func.__name__, args=(func,))
        threads.append(thread)
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    for func, results in thread_results.items():
        # results[1] is actual, results[0] is expected
        assert results[1] == results[0], "Func: %s failed assert" % func.__name__
    assert len(get_scheduler()._task_dict) == 0


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
