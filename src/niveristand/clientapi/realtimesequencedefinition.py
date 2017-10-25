import niveristand.internal
import niveristand.exceptions as nivsexceptions
import uuid
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import LocalDeclaration
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import RealTimeSequence
from NationalInstruments.VeriStand.Data import DoubleValue
from NationalInstruments.VeriStand.Data import I32Value
from System.IO import IOException
import os

_lv_cnt = 0

def add_local_variable(rt_seq, name, value):
    global _lv_cnt
    if name is None:
        name = ''
    name = 'lv_' + name + '_' + str(_lv_cnt)
    _lv_cnt += 1
    converted_value = _convert_value_to_datavalue(value)
    local_declaration = LocalDeclaration(name, converted_value)
    rt_seq.Variables.LocalVariables.AddLocalVariable(local_declaration)
    return name


def create_real_time_sequence():
    return RealTimeSequence()


def save_real_time_sequence(rtseq, filepath):
    try:
        rtseq.SaveSequence(os.path.join(filepath))
    except(IOException) as e:
        raise IOError(e.Message)


def _convert_value_to_datavalue(value):
    if isinstance(value, int):
        return I32Value(value)
    if isinstance(value, float):
        return DoubleValue(value)
    raise nivsexceptions.UnexpectedError("Unable to convert value for type %s"
                                         % type(value))
