import ast
import inspect
import os

from niveristand import errormessages
from niveristand.clientapi import realtimesequencedefinition as rtseqapi
from niveristand.decorators import Modes
from niveristand.exceptions import TranslateError, VeristandError
from niveristand.internal import BLOCK, LOCAL_VARIABLES, RTSEQ
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
        name = self._top_level_func.__name__
        rtseqapi.save_real_time_sequence(self._rtseq, os.path.join(self._path, name) + ".nivsseq")

    def _transform(self):
        try:
            real_obj = self._top_level_func(__rtseq_mode__=Modes.UNWRAP)
        except (KeyError, TypeError):
            raise TranslateError(errormessages.invalid_top_level_func)
        src = inspect.getsource(real_obj)
        top_node = ast.parse(src)
        resources = {LOCAL_VARIABLES: {}, RTSEQ: None, BLOCK: None}
        try:
            func_node = top_node.body[0]
        except TypeError:
            func_node = None
        if func_node is None or not isinstance(func_node, ast.FunctionDef):
            raise TranslateError(errormessages.invalid_top_level_func)
        generic_ast_node_transform(func_node, resources)
        self._rtseq = resources[RTSEQ]
