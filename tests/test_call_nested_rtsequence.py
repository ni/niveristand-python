from niveristand import nivs_rt_sequence, realtimesequencetools
from niveristand.clientapi import DoubleValue
from niveristand.library import wait
import pytest


@ nivs_rt_sequence
def nested_sequence():
    wait(DoubleValue(1))


@nivs_rt_sequence
def call_nested_sequence_after():
    param = DoubleValue(1)
    wait(param)
    nested_sequence()


@nivs_rt_sequence
def call_nested_sequence_before():
    param = DoubleValue(1)
    nested_sequence()
    wait(param)


@nivs_rt_sequence
def call_nested_sequence_twice():
    param = DoubleValue(1)
    wait(param)
    nested_sequence()
    nested_sequence()
    wait(param)
    wait(param)


@nivs_rt_sequence
def call_complex_nested_sequences():
    param = DoubleValue(1)
    wait(param)
    call_nested_sequence_after()
    wait(param)
    call_nested_sequence_before()
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
def test_run_py_as_rts(func_name):
    realtimesequencetools.run_py_as_rtseq(func_name)
