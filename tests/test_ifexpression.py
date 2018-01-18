import sys

from niveristand import decorators, exceptions, RealTimeSequence
from niveristand.clientapi.datatypes import BooleanValue, I32Value
import pytest
from testutilities import rtseqrunner, validation


@decorators.nivs_rt_sequence
def returns_true():
    a = BooleanValue(True)
    return a.value


@decorators.nivs_rt_sequence
def ifexp_bool_test_bool_assign():
    a = BooleanValue(False)
    a.value = True if True else False
    return a.value


@decorators.nivs_rt_sequence
def ifexp_bool_test_int_assign():
    a = I32Value(0)
    a.value = 1 if True else 0
    return a.value


@decorators.nivs_rt_sequence
def ifexp_bool_test_int_assign1():
    a = I32Value(0)
    a.value = 0 if not True else 1
    return a.value


@decorators.nivs_rt_sequence
def ifexp_bool_test_nivstype_assign():
    a = I32Value(0)
    a = I32Value(1) if True else I32Value(0)
    return a.value


@decorators.nivs_rt_sequence
def ifexp_nivsbool_test_nivstype_assign():
    a = I32Value(0)
    a = I32Value(1) if BooleanValue(True) else I32Value(0)
    return a.value


@decorators.nivs_rt_sequence
def ifexp_nivsbool_test_nivstype_assign1():
    a = I32Value(0)
    a = I32Value(1) if not BooleanValue(False) else I32Value(0)
    return a.value


@decorators.nivs_rt_sequence
def ifexp_nivsboolvar_test_int_assign():
    a = I32Value(0)
    b = BooleanValue(True)
    a = I32Value(1) if b.value else I32Value(0)
    return a.value


@decorators.nivs_rt_sequence
def ifexp_nivsboolvar_test_int_assign1():
    a = I32Value(0)
    b = BooleanValue(False)
    a = I32Value(1) if not b.value else I32Value(0)
    return a.value


@decorators.nivs_rt_sequence
def ifexp_expression_test_int_assign():
    a = I32Value(5)
    a.value = 1 if a <= 5 else 0
    return a.value


@decorators.nivs_rt_sequence
def ifexp_expression_test_int_assign1():
    a = I32Value(5)
    a.value = 1 if (a < 5) or True else 0
    return a.value


@decorators.nivs_rt_sequence
def ifexp_nested_ifexp():
    a = I32Value(5)
    a.value = 2 if (a < 5) else 1 if a <= 5 else 0
    return a.value


@decorators.nivs_rt_sequence
def ifexp_rtseq_test():
    a = I32Value(0)
    a.value = 1 if returns_true() else 0
    return a.value


@decorators.nivs_rt_sequence
def ifexp_rtseq_test_rtseq_assign():
    a = BooleanValue(False)
    a.value = returns_true() if returns_true() else False
    return a.value


@decorators.nivs_rt_sequence
def ifexp_rtseq_test_rtseq_assign1():
    a = BooleanValue(False)
    a.value = returns_true() if not returns_true() else returns_true()
    return a.value


@decorators.nivs_rt_sequence
def ifexp_bool_test_expression_assign():
    a = I32Value(0)
    a.value = (1 * 2) - 1 & 7 | a if True else 0
    return a.value


@decorators.nivs_rt_sequence
def ifexp_bool_test_expression_assign1():
    a = I32Value(0)
    a.value = 0 if not True else (1 * 2) - 1 & 7 | a
    return a.value


@decorators.nivs_rt_sequence
def aug_ifexp_bool_test_expression_assign():
    a = I32Value(0)
    a.value += 0 if not True else (1 * 2) - 1 & 7 | a
    return a.value


# region invalid tests
@decorators.nivs_rt_sequence
def ifexp_invalid_int_test():
    a = I32Value(0)
    a = I32Value(1) if 1 else I32Value(0)
    return a.value


# end region invalid tests

run_tests = [
    (returns_true, (), True),
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
    (ifexp_invalid_int_test, (), exceptions.VeristandError),
]

skip_tests = [
    (ifexp_nivsbool_test_nivstype_assign, (), "We can't override ifexp so even though it translates"
                                              "fine python uses the objref as the test, not the value."),
    (ifexp_nivsbool_test_nivstype_assign1, (), "We can't override ifexp so even though it translates"
                                               "fine python uses the objref as the test, not the value."),
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
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    try:
        RealTimeSequence(func_name)
    except expected_result:
        pass
    except exceptions.VeristandError as e:
        pytest.fail('Unexpected exception raised:' +
                    str(e.__class__) + ' while expected was: ' + expected_result.__name__)
    except Exception as exception:
        pytest.fail('ExpectedException not raised: ' + exception)


@pytest.mark.parametrize("func_name, params, reason", skip_tests, ids=idfunc)
def test_skipped(func_name, params, reason):
    pytest.skip(func_name.__name__ + ": " + reason)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
