import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, I32Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
import pytest
from testutilities import rtseqrunner, validation


@nivs_rt_sequence
def _returns_true():
    a = BooleanValue(True)
    return a.value


@nivs_rt_sequence
def ifexp_bool_test_bool_assign():
    a = BooleanValue(False)
    a.value = True if True else False
    return a.value


@nivs_rt_sequence
def ifexp_bool_test_int_assign():
    a = I32Value(0)
    a.value = 1 if True else 0
    return a.value


@nivs_rt_sequence
def ifexp_bool_test_int_assign1():
    a = I32Value(0)
    a.value = 0 if not True else 1
    return a.value


@nivs_rt_sequence
def ifexp_bool_test_nivstype_assign():
    a = I32Value(0)
    b = I32Value(1)
    c = I32Value(0)
    a.value = b.value if True else c.value
    return a.value


@nivs_rt_sequence
def ifexp_nivsbool_test_nivstype_assign():
    a = I32Value(0)
    b = I32Value(1)
    c = I32Value(2)
    a.value = b.value if BooleanValue(False) else c.value
    return a.value


@nivs_rt_sequence
def ifexp_nivsbool_test_nivstype_assign1():
    a = I32Value(0)
    b = I32Value(1)
    c = I32Value(0)
    a.value = b.value if not BooleanValue(False) else c.value
    return a.value


@nivs_rt_sequence
def ifexp_nivsboolvar_test_int_assign():
    a = I32Value(0)
    b = BooleanValue(True)
    c = I32Value(1)
    d = I32Value(0)
    a.value = c.value if b.value else d.value
    return a.value


@nivs_rt_sequence
def ifexp_nivsboolvar_test_int_assign1():
    a = I32Value(0)
    b = BooleanValue(False)
    c = I32Value(1)
    d = I32Value(0)
    a.value = c.value if not b.value else d.value
    return a.value


@nivs_rt_sequence
def ifexp_expression_test_int_assign():
    a = I32Value(5)
    a.value = 1 if a <= 5 else 0
    return a.value


@nivs_rt_sequence
def ifexp_expression_test_int_assign1():
    a = I32Value(5)
    a.value = 1 if (a < 5) or True else 0
    return a.value


@nivs_rt_sequence
def ifexp_nested_ifexp():
    a = I32Value(5)
    a.value = 2 if (a < 5) else 1 if a <= 5 else 0
    return a.value


@nivs_rt_sequence
def ifexp_rtseq_test():
    a = I32Value(0)
    a.value = 1 if _returns_true() else 0
    return a.value


@nivs_rt_sequence
def ifexp_rtseq_test_rtseq_assign():
    a = BooleanValue(False)
    a.value = _returns_true() if _returns_true() else False
    return a.value


@nivs_rt_sequence
def ifexp_rtseq_test_rtseq_assign1():
    a = BooleanValue(False)
    a.value = _returns_true() if not _returns_true() else _returns_true()
    return a.value


@nivs_rt_sequence
def ifexp_bool_test_expression_assign():
    a = I32Value(0)
    a.value = (1 * 2) - 1 & 7 | a if True else 0
    return a.value


@nivs_rt_sequence
def ifexp_bool_test_expression_assign1():
    a = I32Value(0)
    a.value = 0 if not True else (1 * 2) - 1 & 7 | a
    return a.value


@nivs_rt_sequence
def aug_ifexp_bool_test_expression_assign():
    a = I32Value(0)
    a.value += 0 if not True else (1 * 2) - 1 & 7 | a
    return a.value


# <editor-fold desc=Invalid tests>

@nivs_rt_sequence
def ifexp_invalid_int_test():
    a = I32Value(0)
    a = I32Value(1) if 1 else I32Value(0)
    return a.value

# </editor-fold>


run_tests = [
    (ifexp_bool_test_bool_assign, (), True),
    (ifexp_bool_test_int_assign, (), 1),
    (ifexp_bool_test_int_assign1, (), 1),
    (ifexp_bool_test_nivstype_assign, (), 1),
    (ifexp_nivsboolvar_test_int_assign, (), 1),
    (ifexp_nivsboolvar_test_int_assign1, (), 1),
    (ifexp_expression_test_int_assign, (), 1),
    (ifexp_expression_test_int_assign1, (), 1),
    (ifexp_nested_ifexp, (), 1),
    (ifexp_bool_test_expression_assign, (), 1),
    (ifexp_bool_test_expression_assign1, (), 1),
    (aug_ifexp_bool_test_expression_assign, (), 1),
    (ifexp_rtseq_test, (), 1),
    (ifexp_rtseq_test_rtseq_assign, (), True),
    (ifexp_rtseq_test_rtseq_assign1, (), True),
]

fail_transform_tests = [
    (ifexp_invalid_int_test, (), VeristandError),
    (ifexp_nivsbool_test_nivstype_assign, (), TranslateError),
    (ifexp_nivsbool_test_nivstype_assign1, (), TranslateError),
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
