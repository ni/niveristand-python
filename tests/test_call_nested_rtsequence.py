from niveristand import nivs_rt_sequence, NivsParam, realtimesequencetools
from niveristand.clientapi import DoubleValue
from niveristand.library import wait
import pytest


@ NivsParam('var1', DoubleValue(0), NivsParam.BY_REF)
@ nivs_rt_sequence
def nested_sequence(var1):
    wait(var1)


@NivsParam('param', DoubleValue(0), NivsParam.BY_REF)
@nivs_rt_sequence
def call_nested_sequence_after(param):
    wait(param)
    nested_sequence(param)


@NivsParam('param', DoubleValue(0), NivsParam.BY_REF)
@nivs_rt_sequence
def call_nested_sequence_before(param):
    nested_sequence(param)
    wait(param)


@NivsParam('param', DoubleValue(0), NivsParam.BY_REF)
@nivs_rt_sequence
def call_nested_sequence_twice(param):
    wait(param)
    nested_sequence(param)
    nested_sequence(param)
    wait(param)
    wait(param)


@NivsParam('param', DoubleValue(0), NivsParam.BY_REF)
@nivs_rt_sequence
def call_complex_nested_sequences(param):
    wait(param)
    call_nested_sequence_after(param)
    wait(param)
    call_nested_sequence_before(param)
    wait(param)


run_tests = [
    call_nested_sequence_after,
    call_nested_sequence_before,
    call_nested_sequence_twice,
    call_complex_nested_sequences
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name", run_tests, ids=idfunc)
def test_save_py_as_rts(func_name):
    realtimesequencetools.save_py_as_rtseq(func_name,
            r"C:\Users\Public\Documents\National Instruments\NI VeriStand 2020\Stimulus Profiles\Python Examples")
