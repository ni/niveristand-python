from collections import OrderedDict
from niveristand import _errormessages
from niveristand import errors
from niveristand.clientapi._datatypes.rtprimitives import DoubleValue


class Resources:
    def __init__(self, rtseq, alias):
        from niveristand.clientapi.realtimesequencepkg import RealTimeSequencePkg
        self._rtseq = rtseq
        self._seq_alias = alias
        self._block = None
        self._local_variables = {}
        self._parameters = OrderedDict()
        self._deps = RealTimeSequencePkg()
        self._channel_references = list()

    def get_rtseq(self):
        return self._rtseq

    def set_current_block(self, block):
        self._block = block

    def get_current_block(self):
        return self._block

    def add_variable(self, py_name, py_value, rtseq_name):
        variable = _Variable(py_value, rtseq_name)
        self._local_variables[py_name] = variable

    def has_variable(self, variable_name):
        return variable_name in self._local_variables

    def get_variable_rtseq_name(self, variable_name):
        return self._local_variables[variable_name].rtseq_name

    def get_variable_py_name(self, rtseq_var_name):
        result = ''
        for key in self._local_variables.keys():
            if self._local_variables[key].rtseq_name == rtseq_var_name:
                result = key
        return result

    def get_variable_py_value(self, variable_name):
        return self._local_variables[variable_name].py_value

    def add_referenced_sequence(self, referenced):
        self._deps.add_referenced_sequence(self._seq_alias, referenced)

    def get_dependency_pkg(self):
        return self._deps

    def set_dependency_pkg(self, pkg):
        self._deps = pkg

    def add_channel_ref(self, variable_name, channel_name, rtseq_var_name, channel_is_vector):
        self._channel_references.append(_ChannelReference(channel_name, rtseq_var_name, channel_is_vector))
        self.add_variable(variable_name, DoubleValue(0), rtseq_var_name)
        self.add_variable(variable_name + ".value", DoubleValue(0), rtseq_var_name)

    def has_channel_ref(self, rtseq_name):
        for channel_ref_obj in self._channel_references:
            if channel_ref_obj.rtseq_name == rtseq_name:
                return True
        return False

    def get_channel_ref_rtseq_name_from_channel_name(self, channel_name):
        for channel_ref_obj in self._channel_references:
            if channel_ref_obj.channel_name == channel_name:
                return channel_ref_obj.rtseq_name

    def get_all_channel_refs(self):
        return self._channel_references

    def add_parameter(self, param_name, default_value, by_value):
        if param_name in self._parameters:
            raise errors.UnexpectedError(_errormessages.unexpected_argument_redefine)
        rt_seq_param_name = _py_param_name_to_rtseq_param_name(param_name)
        self._parameters[param_name] = _Parameter(rt_seq_param_name, default_value, by_value)
        self.add_variable(param_name, default_value, rt_seq_param_name)
        self.add_variable(param_name + ".value", default_value, rt_seq_param_name)

    def get_parameters(self):
        return self._parameters.values()

    def update_parameter(self, param_name, default_value, by_value):
        if param_name not in self._parameters:
            raise errors.TranslateError(_errormessages.param_description_no_param)
        rt_seq_param_name = _py_param_name_to_rtseq_param_name(param_name)
        self._parameters[param_name] = _Parameter(rt_seq_param_name, default_value, by_value)
        self._local_variables[param_name].py_value = default_value


def _py_param_name_to_rtseq_param_name(name):
    return "p_" + name


class _Variable:
    def __init__(self, py_value, rtseq_name):
        self.py_value = py_value
        self.rtseq_name = rtseq_name


class _Parameter:
    def __init__(self, rtseq_name, default_value, by_value):
        self.rtseq_name = rtseq_name
        self.default_value = default_value
        self.by_value = by_value


class _ChannelReference:
    def __init__(self, channel_name, rtseq_name, channel_is_vector):
        self.channel_name = channel_name
        self.rtseq_name = rtseq_name
        self.channel_is_vector = channel_is_vector
