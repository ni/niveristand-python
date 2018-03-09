import sys
from niveristand import decorators, RealTimeSequence
from niveristand import realtimesequencetools
from niveristand.clientapi.datatypes import I32Value
from niveristand.exceptions import TranslateError
from niveristand.library.primitives import iteration
from niveristand.library.tasks import multitask, nivs_yield
import pytest
from testutilities import rtseqrunner, validation


@decorators.nivs_rt_sequence
def yield_single():
    a = I32Value(0)
    nivs_yield()
    a.value = iteration()
    return a.value


@decorators.nivs_rt_sequence
def yield_many():
    a = I32Value(0)
    nivs_yield()
    nivs_yield()
    nivs_yield()
    nivs_yield()
    nivs_yield()
    a.value = iteration()
    return a.value


@decorators.nivs_rt_sequence
def yield_in_while():
    a = I32Value(0)
    while a.value < 10:
        nivs_yield()
        a.value = iteration()
    return a.value


@decorators.nivs_rt_sequence
def yield_multitask():
    with multitask() as mt:
        @decorators.task(mt)
        def f1():
            for a in range(5):
                nivs_yield()

        @decorators.task(mt)
        def f2():
            with multitask() as mt_inner:
                @decorators.task(mt_inner)
                def fa():
                    for b in range(7):
                        nivs_yield()

                @decorators.task(mt_inner)
                def fb():
                    for c in range(13):
                        nivs_yield()
    a = I32Value(0)
    a.value = iteration()
    return a.value


@decorators.nivs_rt_sequence
def yield_as_parameter_fail():
    abs(nivs_yield())


@decorators.nivs_rt_sequence
def yield_as_operator_fails():
    a = I32Value(0)
    a.value = nivs_yield() + 1
    return a.value


run_tests = [
    (yield_single, (), 1),
    (yield_many, (), 5),
    (yield_in_while, (), 10),
    # multitask() has an implicit yield at the end of it. Keep that in mind!
    (yield_multitask, (), 15),
]

skip_tests = [
]

fail_transform_tests = [
    (yield_as_parameter_fail, (), TranslateError),
    (yield_as_operator_fails, (), TranslateError),
]


def idfunc(val):
    return val.__name__


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


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, reason", skip_tests, ids=idfunc)
def test_skipped(func_name, params, reason):
    pytest.skip(func_name.__name__ + ": " + reason)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
