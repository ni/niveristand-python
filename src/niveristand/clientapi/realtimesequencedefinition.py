import os
from niveristand import _errormessages, errors
from niveristand import _internal
from niveristand._translation.py2rtseq.utils import _py_param_name_to_rtseq_param_name
from niveristand.clientapi import stimulusprofileapi
from niveristand.clientapi._factory import _DefaultGatewayFactory
from niveristand.clientapi._sequencecallinfo import _SequenceCallInfoFactory
from niveristand.clientapi._sequenceparameterassignmentinfo import _SequenceParameterAssignmentInfoFactory
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import Expression  # noqa: I100
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import ForEachLoop
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import ForLoop
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import GenerateError
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import IfElse
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import LocalDeclaration
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import Multitask
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import RealTimeSequence
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import ReturnDeclaration
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import StopTask
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import Task
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import WhileLoop
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import Yield
from System.IO import IOException


_internal.dummy()

factory = None
workspace = None


def add_local_variable(rt_seq, name, value):
    name = _create_unique_lv_name(name)
    local_declaration = LocalDeclaration(name, value._data_value)
    rt_seq.Variables.LocalVariables.AddLocalVariable(local_declaration)
    return name


def add_assignment(block, dest_name, source_name):
    add_expression(block, '%s = %s' % (dest_name, source_name))


def add_expression(block, expression):
    block.AddStatement(Expression('%s' % expression))


def add_yield(block):
    block.AddStatement(Yield())


def add_if_else(block, test_condition):
    if_else = IfElse(Expression(test_condition))
    block.AddStatement(if_else)
    return if_else


def add_for_loop(block, loop_variable, iterations):
    for_loop = ForLoop(loop_variable, Expression(str(iterations)), False)
    block.AddStatement(for_loop)
    return for_loop


def add_foreach_loop(block, loop_variable, iterations):
    foreach_loop = ForEachLoop(loop_variable, Expression(str(iterations)), False)
    block.AddStatement(foreach_loop)
    return foreach_loop


def add_while(block, test_condition):
    while_block = WhileLoop(Expression(test_condition), False)
    block.AddStatement(while_block)
    return while_block


def add_multi_task(block):
    multi_task = Multitask()
    block.AddStatement(multi_task)
    return multi_task


def add_task(multi_task, name):
    task = Task(name)
    multi_task.AddTask(task)
    return task.Body


def create_real_time_sequence():
    return RealTimeSequence()


def add_return_variable(rtseq, name, default_value):
    name = _create_unique_lv_name(name)
    return_declaration = ReturnDeclaration(name, default_value._data_value)
    rtseq.Variables.ReturnType = return_declaration
    return name


def add_generate_error(block, code, message, action):
    block.AddStatement(GenerateError(code, message, action))


def add_stop_task(block, taskname):
    block.AddStatement(StopTask(taskname))


def save_real_time_sequence(rtseq, filepath):
    try:
        rtseq.SaveSequence(os.path.join(filepath))
    except(IOException) as e:
        raise IOError(e.Message)


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


def to_channel_ref_name(name):
    return "ch_" + name


def _get_channel_node_info(name, node_info_list):
    for channel in node_info_list:
        if channel.FullPath == name:
            return channel
    raise errors.VeristandError(_errormessages.channel_not_found % name)


def run_rt_sequence(rt_sequence_path, rtseq_params):
    rtseq_params = \
        [_SequenceParameterAssignmentInfoFactory.create(_py_param_name_to_rtseq_param_name(key), rtseq_params[key])
         for key in rtseq_params]
    seq_call_info = _SequenceCallInfoFactory.create(rt_sequence_path, None, rtseq_params, False, 100000)
    session = _DefaultGatewayFactory.get_new_stimulus_profile_session(rt_sequence_path, [seq_call_info], "")
    sequence_control = session[os.path.splitext(os.path.basename(rt_sequence_path))[0] + ":1"]
    state = stimulusprofileapi.StimulusProfileState(session)
    sequence_control.register_sequence_complete_event_handler(state._sequence_complete_event_handler)
    session.deploy(True)
    return state
