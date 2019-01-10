import sys
from niveristand import nivs_rt_sequence, NivsParam
from niveristand import realtimesequencetools
from niveristand.clientapi import DoubleValue, DoubleValueArray
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError
from niveristand.library import multitask, nivs_yield, task
import pytest
from testutilities import rtseqrunner, validation


@NivsParam('param', DoubleValue(0), False)
@nivs_rt_sequence
def _sub_rt_seq(param):
    try:
        a = DoubleValue(1)
    finally:
        a.value = param.value
    return a.value


@nivs_rt_sequence
def try_simple():
    try:
        a = DoubleValue(1)
    finally:
        a.value = 5
    return a.value


@nivs_rt_sequence
def try_second_statement():
    a = DoubleValue(0)
    try:
        a.value = 5
    finally:
        a.value = 10
    return a.value


@nivs_rt_sequence
def return_in_try():
    try:
        a = DoubleValue(0)
        return a.value
    finally:
        a.value = 10


@nivs_rt_sequence
def return_in_finally():
    try:
        a = DoubleValue(0)
    finally:
        a.value = 10
        return a.value


@nivs_rt_sequence
def try_complex_body():
    try:
        a = DoubleValueArray([0, 1, 2, 3, 4])
        b = DoubleValue(0)
        for x in a.value:
            if x.value % 2 == 0:
                b.value += x.value
            else:
                b.value -= x.value
    finally:
        if b.value < 5:
            b.value = 1
    return b.value


@nivs_rt_sequence
def try_in_try():
    try:
        a = DoubleValue(0)
        try:
            a.value = 1
        finally:
            a.value = 3
    finally:
        a.value = 5
    return a.value


@nivs_rt_sequence
def try_in_if():
    if True:
        try:
            a = DoubleValue(0)
        finally:
            a.value = 5
    return a.value


@nivs_rt_sequence
def try_in_else():
    a = DoubleValue(0)
    if True:
        a.value = 1
    else:
        try:
            a.value = 3
        finally:
            a.value = 5
    return a.value


@nivs_rt_sequence
def try_in_while():
    while True:
        try:
            a = DoubleValue(0)
        finally:
            a.value = 5
    return a.value


@nivs_rt_sequence
def try_in_for():
    for i in range(5):
        try:
            a = DoubleValue(0)
        finally:
            a.value = 5
    return a.value


@nivs_rt_sequence
def call_subroutine_with_try():
    try:
        a = DoubleValue(0)
        b = DoubleValue(5)
        a.value = _sub_rt_seq(b)
    finally:
        b.value = 5
    return a.value


@nivs_rt_sequence
def try_with_except():
    try:
        a = DoubleValue(0)
    except Exception:
        a.value = 1
    finally:
        a.value = 3
    return a.value


@nivs_rt_sequence
def try_with_orelse():
    try:
        a = DoubleValue(0)
    except Exception:
        a.value = 3
    else:
        a.value = 5
    return a.value


@nivs_rt_sequence
def try_in_task():
    a = DoubleValue(0)
    with multitask() as mt:
        @task(mt)
        def f1():
            try:
                a.value += 1
            finally:
                a.value += 1

        @task(mt)
        def f2():
            nivs_yield()
    return a.value


@nivs_rt_sequence
def try_in_multitask():
    a = DoubleValue(0)
    with multitask() as mt:
        try:
            a.value = 5
        finally:
            a.value += 1

        @task(mt)
        def f1():
            try:
                a.value += 1
            finally:
                a.value += 1

        @task(mt)
        def f2():
            nivs_yield()
    return a.value


@nivs_rt_sequence
def try_in_multitask1():
    a = DoubleValue(0)
    with multitask() as mt:
        try:
            @task(mt)
            def f1():
                pass
        finally:
            a.value += 1

        @task(mt)
        def f2():
            nivs_yield()
    return a.value


run_tests = [
    (try_simple, (), 5),
    (try_complex_body, (), 1),
    (call_subroutine_with_try, (), 5),
]

fail_transform_tests = [
    (try_second_statement, (), TranslateError),
    (return_in_try, (), TranslateError),
    (return_in_finally, (), TranslateError),
    (try_in_try, (), TranslateError),
    (try_in_if, (), TranslateError),
    (try_in_else, (), TranslateError),
    (try_in_while, (), TranslateError),
    (try_in_for, (), TranslateError),
    (try_with_except, (), TranslateError),
    (try_with_orelse, (), TranslateError),
    (try_in_task, (), TranslateError),
    (try_in_multitask, (), TranslateError),
    (try_in_multitask1, (), TranslateError),
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


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
