import ast
import inspect
import os

from niveristand import errormessages
from niveristand.clientapi import realtimesequencedefinition as rtseqapi
from niveristand.decorators import Modes
from niveristand.exceptions import TranslateError, VeristandError
from niveristand.translation.py2rtseq.utils import Resources
from niveristand.translation.utils import generic_ast_node_transform


class RealTimeSequence:
    def __init__(self, top_level_func):
        self._top_level_func = top_level_func
        self._path = ''
        self._rtseq = None
        # finally, initialize the transform
        self._transform()

    def save(self, path=None):
        if self._rtseq is None:
            raise VeristandError(errormessages.save_without_valid_sequence)
        if path is not None:
            self._path = os.path.abspath(path)
        name = os.path.join(self._path, self._top_level_func.__name__) + ".nivsseq"
        rtseqapi.save_real_time_sequence(self._rtseq, name)
        return name

    def _transform(self):
        try:
            real_obj = self._top_level_func(__rtseq_mode__=Modes.UNWRAP)
        except (KeyError, TypeError):
            raise TranslateError(errormessages.invalid_top_level_func)
        src = inspect.getsource(real_obj)
        top_node = ast.parse(src)
        try:
            func_node = top_node.body[0]
        except TypeError:
            func_node = None
        if func_node is None or not isinstance(func_node, ast.FunctionDef):
            raise TranslateError(errormessages.invalid_top_level_func)

        self._rtseq = rtseqapi.create_real_time_sequence()
        transform_resources = Resources(self._rtseq)
        generic_ast_node_transform(func_node, transform_resources)
