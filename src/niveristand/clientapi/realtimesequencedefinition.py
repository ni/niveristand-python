import os

from niveristand import exceptions as nivsexceptions
from niveristand import internal
from niveristand.datatypes import Boolean
from niveristand.datatypes import DataType
from niveristand.datatypes import Double
from niveristand.datatypes import DoubleArray
from niveristand.datatypes import Int32
from niveristand.datatypes import Int64
from niveristand.datatypes import UInt32
from niveristand.datatypes import UInt64
from NationalInstruments.VeriStand.Data import BooleanValue  # noqa: I100 We need these C# imports to be out of order.
from NationalInstruments.VeriStand.Data import DoubleValue
from NationalInstruments.VeriStand.Data import DoubleValueArray
from NationalInstruments.VeriStand.Data import I32Value
from NationalInstruments.VeriStand.Data import I64Value
from NationalInstruments.VeriStand.Data import U32Value
from NationalInstruments.VeriStand.Data import U64Value
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import Expression
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import IfElse
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import LocalDeclaration
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import RealTimeSequence
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import ReturnDeclaration
import numpy as np
from System.IO import IOException

internal.dummy()


def add_local_variable(rt_seq, name, value):
    name = _create_unique_lv_name(name)
    converted_value = _convert_value_to_datavalue(value)
    local_declaration = LocalDeclaration(name, converted_value)
    rt_seq.Variables.LocalVariables.AddLocalVariable(local_declaration)
    return name


def add_assignment(block, dest_name, source_name):
    block.AddStatement(Expression('%s = %s' % (dest_name, source_name)))


def add_if_else(block, test_condition):
    if_else = IfElse(Expression(test_condition))
    block.AddStatement(if_else)
    return if_else


def create_real_time_sequence():
    return RealTimeSequence()


def add_return_variable(rtseq, name, default_value):
    name = _create_unique_lv_name(name)
    value = _convert_value_to_datavalue(default_value)
    return_declaration = ReturnDeclaration(name, value)
    rtseq.Variables.ReturnType = return_declaration
    return name


def save_real_time_sequence(rtseq, filepath):
    try:
        rtseq.SaveSequence(os.path.join(filepath))
    except(IOException) as e:
        raise IOError(e.Message)


def _convert_value_to_datavalue(nivsvalue):
    if isinstance(nivsvalue, Boolean):
        return BooleanValue(nivsvalue)
    if isinstance(nivsvalue, Double):
        return DoubleValue(float(nivsvalue.value))
    if isinstance(nivsvalue, DoubleArray):
        double_value_list = []
        for value in nivsvalue.value:
            double_value_list.append(DoubleValue(value.value))
        return DoubleValueArray(double_value_list)
    if isinstance(nivsvalue, Int32):
        return I32Value(nivsvalue.value)
    if isinstance(nivsvalue, Int64):
        return I64Value(nivsvalue.value)
    if isinstance(nivsvalue, UInt32):
        return U32Value(np.uint32(nivsvalue.value))
    if isinstance(nivsvalue, UInt64):
        return U64Value(np.uint64(nivsvalue.value))
    if isinstance(nivsvalue, DataType):
        raise nivsexceptions.VeristandNotImplementedError()
    raise nivsexceptions.UnexpectedError("Unable to convert value for type %s"
                                         % type(nivsvalue))


def _create_unique_lv_name(name):
    try:
        _create_unique_lv_name.lv_cnt += 1
    except AttributeError:
        _create_unique_lv_name.lv_cnt = 0
    if name is None:
        name = ''
    name = 'lv_' + name + '_' + str(_create_unique_lv_name.lv_cnt)
    _create_unique_lv_name.lv_cnt += 1
    return name
