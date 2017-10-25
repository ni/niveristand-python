import os
import inspect
import ast
from niveristand.translation.py2rtseq import transformers
from niveristand.decorators import Modes
from niveristand.clientapi import realtimesequencedefinition as rtseqapi


class RealTimeSequence:
    def __init__(self, obj, top_level_func=None):
        self._obj = obj
        self._seqs = dict()
        self._top_level_func = top_level_func
        self._transform()
        self._path = ''

    def save(self, path=None):
        if path is not None:
            self._path = os.path.abspath(path)
        for name, seq in self._seqs.items():
            rtseqapi.save_real_time_sequence(seq, os.path.join(self._path, name) + ".nivsseq")

    def _transform(self):
        try:
            real_obj = self._obj(__rtseq_mode__=Modes.UNWRAP)
        except:
            real_obj = self._obj
        src = inspect.getsource(real_obj)
        top_node = ast.parse(src)
        transformers.generic_transform(top_node, self._seqs, None)
