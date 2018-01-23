class Resources:
    def __init__(self, rtseq, alias):
        from niveristand.clientapi.realtimesequencepkg import RealTimeSequencePkg
        self._rtseq = rtseq
        self._seq_alias = alias
        self._block = None
        self._local_variables = {}
        self._parameters = list()
        self._deps = RealTimeSequencePkg()

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

    def get_variable_py_value(self, variable_name):
        return self._local_variables[variable_name].py_value

    def add_referenced_sequence(self, referenced):
        self._deps.add_referenced_sequence(self._seq_alias, referenced)

    def get_dependency_pkg(self):
        return self._deps

    def set_dependency_pkg(self, pkg):
        self._deps = pkg

    def add_parameter(self, param_name, default_value, by_value):
        self._parameters.append(_Parameter(param_name, default_value, by_value))
        self.add_variable(param_name, default_value, param_name)
        self.add_variable(param_name + ".value", default_value, param_name)

    def get_parameters(self):
        return self._parameters


class _Variable:
    def __init__(self, py_value, rtseq_name):
        self.py_value = py_value
        self.rtseq_name = rtseq_name


class _Parameter:
    def __init__(self, rtseq_name, default_value, by_value):
        self.rtseq_name = rtseq_name
        self.default_value = default_value
        self.by_value = by_value
