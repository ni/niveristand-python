class Resources:
    def __init__(self, rtseq):
        self._rtseq = rtseq
        self._block = None
        self._local_variables = {}

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


class _Variable:
    def __init__(self, py_value, rtseq_name):
        self.py_value = py_value
        self.rtseq_name = rtseq_name
