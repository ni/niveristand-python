import ast
import inspect
import os
import tempfile

from niveristand import errormessages
from niveristand.clientapi import realtimesequencedefinition as rtseqapi
from niveristand.clientapi import rtsequencedefinitionutils as rtsequtils
from niveristand.decorators import Modes
from niveristand.exceptions import TranslateError, VeristandError
from niveristand.translation.py2rtseq.utils import Resources
from niveristand.translation.utils import generic_ast_node_transform
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import Reference  # noqa: I100 C# imports are exempt
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import References  # noqa: I100 C# imports are exempt


class RealTimeSequence:
    def __init__(self, top_level_func, rtseq_pkg=None):
        self._top_level_func = top_level_func
        self._path = ''
        self._rtseq = None
        self._rtseqpkg = rtseq_pkg
        self._ref = None
        # finally, initialize the transform
        self._transform()

    def save(self, path=None):
        if self._rtseq is None:
            raise VeristandError(errormessages.save_without_valid_sequence)
        if path is not None:
            self._path = os.path.abspath(path)
        elif not os.path.isdir(self._path):
            self._path = tempfile.mkdtemp()

        name = self._build_file_name()
        rtseqapi.save_real_time_sequence(self._rtseq, name)
        self._rtseqpkg.save_referenced(self._path, self)
        self._update_references()
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
        transform_resources = Resources(self._rtseq, str(self))
        if self._rtseqpkg is not None:
            transform_resources.set_dependency_pkg(self._rtseqpkg)
        generic_ast_node_transform(func_node, transform_resources)
        self._rtseqpkg = transform_resources.get_dependency_pkg()
        self._rtseqpkg.append(inspect.getmodule(real_obj))
        self.save()
        rtsequtils.compile_rtseq(self._rtseq)

    def _update_references(self):
        self._ref = Reference(str(self), self._build_file_name())
        self._rtseq.References = References()
        for referenced in self._rtseqpkg.get_referenced(self):
            self._rtseq.References.AddReference(referenced.get_reference())

    def _build_file_name(self):
        return os.path.join(self._path, str(self) + ".nivsseq")

    def get_reference(self):
        return self._ref

    def __str__(self):
        return self._top_level_func.__name__
