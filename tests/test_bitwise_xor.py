import sys

from niveristand import decorators, RealTimeSequence
from niveristand import realtimesequencetools
from niveristand.clientapi.datatypes import BooleanValue, ChannelReference, DoubleValue, I32Value, I64Value
from niveristand.exceptions import TranslateError, VeristandError
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@decorators.nivs_rt_sequence
def return_constant():
    a = I32Value(5)
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_simple_numbers():
    a = DoubleValue(0)
    a.value = 1 ^ 3
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_num_nivsdatatype():
    a = DoubleValue(0)
    a.value = 1 ^ DoubleValue(3)
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_nivsdatatype_nivsdatatype():
    a = DoubleValue(0)
    a.value = DoubleValue(1) ^ DoubleValue(3)
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_nivsdatatype_nivsdatatype1():
    a = DoubleValue(0)
    a.value = DoubleValue(1) ^ I32Value(3)
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_nivsdatatype_nivsdatatype2():
    a = BooleanValue(0)
    a.value = BooleanValue(1) ^ BooleanValue(3)
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_nivsdatatype_nivsdatatype3():
    a = DoubleValue(0)
    a.value = I32Value(1) ^ I32Value(3)
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_multiple_types():
    a = I32Value(0)
    a.value = 1 ^ I32Value(3) ^ 5
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_multiple_types1():
    a = I64Value(1)
    a.value = 1 ^ I64Value(5) ^ 3 ^ I32Value(7)
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_use_rtseq():
    a = DoubleValue(0)
    a.value = 1 ^ return_constant()
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_use_rtseq1():
    a = DoubleValue(0)
    a.value = return_constant() ^ 1
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_use_rtseq2():
    a = DoubleValue(0)
    a.value = I32Value(1) ^ return_constant()
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_use_rtseq3():
    a = DoubleValue(0)
    a.value = return_constant() ^ I32Value(1)
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_with_parantheses():
    a = I32Value(0)
    a.value = 1 ^ (5 ^ 3)
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_with_parantheses1():
    a = DoubleValue(0)
    a.value = 1 ^ (DoubleValue(3) ^ I32Value(5))
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_with_parantheses2():
    a = DoubleValue(0)
    a.value = DoubleValue(1) ^ (I32Value(2) ^ 3.0) ^ DoubleValue(4)
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_variables():
    a = I32Value(5)
    b = I32Value(0)
    b.value = 1 ^ a
    return b.value


@decorators.nivs_rt_sequence
def bitwise_xor_variables1():
    a = I64Value(5)
    b = I64Value(0)
    b.value = 1 ^ a.value
    return b.value


@decorators.nivs_rt_sequence
def bitwise_xor_variable_variable():
    a = I32Value(1)
    b = I64Value(3)
    c = I32Value(0)
    c.value = a.value ^ b.value
    return c.value


@decorators.nivs_rt_sequence
def bitwise_xor_variable_variable1():
    a = I32Value(1)
    b = I64Value(3)
    c = DoubleValue(0)
    c.value = a.value ^ b.value
    return c.value


@decorators.nivs_rt_sequence
def bitwise_xor_variable_rtseq():
    a = I32Value(1)
    b = DoubleValue(0)
    b.value = a.value ^ return_constant()
    return b.value


@decorators.nivs_rt_sequence
def bitwise_xor_variable_rtseq1():
    a = I32Value(1)
    b = DoubleValue(0)
    b.value = return_constant() ^ a.value
    return b.value


@decorators.nivs_rt_sequence
def bitwise_xor_to_channelref():
    a = DoubleValue(0)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value = 1 ^ b.value
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_binary_unary():
    a = I32Value(0)
    a.value = 3 ^ - 1
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_complex_expr():
    a = DoubleValue(0)
    a.value = 1 ^ (2 if 2 < 3 else 4)
    return a.value


# <editor-fold desc=Augassign tests>

@decorators.nivs_rt_sequence
def aug_bitwise_xor_simple_numbers():
    a = I32Value(3)
    a.value ^= 7
    return a.value


@decorators.nivs_rt_sequence
def aug_bitwise_xor_num_nivsdatatype():
    a = I32Value(1)
    a.value ^= I32Value(3)
    return a.value


@decorators.nivs_rt_sequence
def aug_bitwise_xor_use_rtseq():
    a = I32Value(1)
    a.value ^= return_constant()
    return a.value


@decorators.nivs_rt_sequence
def aug_bitwise_xor_with_parantheses():
    a = I32Value(1)
    a.value ^= 7 ^ (5 ^ 3)
    return a.value


@decorators.nivs_rt_sequence
def aug_bitwise_xor_variables():
    a = I32Value(7)
    b = I32Value(3)
    b.value ^= a.value
    return b.value


@decorators.nivs_rt_sequence
def aug_bitwise_xor_to_channelref():
    a = DoubleValue(1)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value ^= b.value
    return a.value


@decorators.nivs_rt_sequence
def aug_bitwise_xor_unary():
    a = I32Value(3)
    a.value ^= -1
    return a.value


# </editor-fold>

# <editor-fold desc=Invalid tests>

@decorators.nivs_rt_sequence
def bitwise_xor_invalid_variables():
    return a.value ^ b


@decorators.nivs_rt_sequence
def bitwise_xor_invalid_variables1():
    return a.value ^ b.value


@decorators.nivs_rt_sequence
def bitwise_xor_to_None():
    a = DoubleValue(0)
    a.value = None ^ 1
    return a.value


@decorators.nivs_rt_sequence
def bitwise_xor_invalid_rtseq_call():
    a = DoubleValue(0)
    a.value = return_constant ^ 1
    return a.value

# </editor-fold>


run_tests = [
    (return_constant, (), 5.0),
    (bitwise_xor_simple_numbers, (), 2),
    (bitwise_xor_nivsdatatype_nivsdatatype3, (), 2),
    (bitwise_xor_variables, (), 4),
    (bitwise_xor_variables1, (), 4),
    (bitwise_xor_multiple_types, (), 7),
    (bitwise_xor_multiple_types1, (), 0),
    (bitwise_xor_with_parantheses, (), 7),
    (bitwise_xor_variable_variable, (), 2),
    (bitwise_xor_variable_variable1, (), 2),
    (bitwise_xor_binary_unary, (), -4),
    (aug_bitwise_xor_simple_numbers, (), 4),
    (aug_bitwise_xor_variables, (), 4),
    (aug_bitwise_xor_num_nivsdatatype, (), 2),
    (aug_bitwise_xor_with_parantheses, (), 0),
    (aug_bitwise_xor_unary, (), -4),
    (bitwise_xor_complex_expr, (), 3),
    (bitwise_xor_use_rtseq, (), 4),
    (bitwise_xor_use_rtseq1, (), 4),
    (bitwise_xor_use_rtseq2, (), 4),
    (bitwise_xor_use_rtseq3, (), 4),
    (bitwise_xor_variable_rtseq, (), 4),
    (bitwise_xor_variable_rtseq1, (), 4),
    (aug_bitwise_xor_use_rtseq, (), 4),
]

skip_tests = [
    (bitwise_xor_invalid_rtseq_call, (), "RTSeq call not implemented yet."),
]

fail_transform_tests = [
    (bitwise_xor_invalid_variables, (), TranslateError),
    (bitwise_xor_invalid_variables1, (), TranslateError),
    (bitwise_xor_num_nivsdatatype, (), VeristandError),  # cannot do bitwise xor on Double
    (bitwise_xor_nivsdatatype_nivsdatatype, (), VeristandError),  # cannot do bitwise xor on Double
    (bitwise_xor_nivsdatatype_nivsdatatype1, (), VeristandError),  # cannot do bitwise xor on Double
    (bitwise_xor_nivsdatatype_nivsdatatype2, (), VeristandError),  # cannot do bitwise xor on Boolean
    (bitwise_xor_with_parantheses1, (), VeristandError),  # cannot do bitwise xor on Double
    (bitwise_xor_with_parantheses2, (), VeristandError),  # cannot do bitwise xor on Double
    (bitwise_xor_to_channelref, (), VeristandError),  # cannot do bitwise xor on Double
    (aug_bitwise_xor_to_channelref, (), VeristandError),  # cannot do bitwise xor on Double
    (bitwise_xor_to_None, (), TranslateError),
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
    try:
        RealTimeSequence(func_name)
    except expected_result:
        pass
    except VeristandError as e:
        pytest.fail('Unexpected exception raised:' +
                    str(e.__class__) + ' while expected was: ' + expected_result.__name__)
    except Exception as exception:
        pytest.fail('ExpectedException not raised: ' + exception)


@pytest.mark.parametrize("func_name, params, reason", skip_tests, ids=idfunc)
def test_skipped(func_name, params, reason):
    pytest.skip(func_name.__name__ + ": " + reason)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
