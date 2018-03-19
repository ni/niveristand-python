import collections
import inspect
from niveristand import _errormessages
from niveristand._decorators import rt_seq_mode_id
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError


class RealTimeSequencePkg(collections.MutableMapping):
    def __init__(self):
        self._rtseqs = dict()
        self._dep_graph = dict()

    def save_all(self, path):
        for seq in self:
            self[seq].save(path)

    def save_referenced(self, path, referencer):
        for seq in self.get_referenced(referencer):
            if seq is None:
                raise TranslateError(_errormessages.dependency_not_found)
            seq.save(path)

    def add_referenced_sequence(self, referencer, referenced_sequence):
        referencer_name = self._obj_to_key(referencer)
        referenced_sequence = self._obj_to_key(referenced_sequence)
        if referencer_name not in self._dep_graph:
            self._dep_graph[referencer_name] = list()
        if referenced_sequence not in self._dep_graph[referencer_name]:
            self._dep_graph[referencer_name].append(referenced_sequence)

    def get_referenced(self, referencer):
        referencer = self._obj_to_key(referencer)
        return [self._try_resolve(dep_name) for dep_name in self._dep_graph[referencer]]

    def __len__(self):
        return len(self._rtseqs)

    def __getitem__(self, item):
        item = self._obj_to_key(item)
        seq = self._try_resolve(item)
        if seq is None:
            raise TranslateError(_errormessages.dependency_not_found)
        return self._rtseqs.get(item)

    def _obj_to_key(self, item):
        return str(item) if not inspect.isfunction(item) else item.__name__

    def _try_resolve(self, item):
        seq = self._rtseqs.get(item)
        if inspect.isfunction(seq):
            for dep in self._dep_graph[item]:
                if not isinstance(self._rtseqs[dep], RealTimeSequence):
                    self._try_resolve(item)
            seq = RealTimeSequence(seq, self)
            self._rtseqs[item] = seq
        return seq

    def __contains__(self, item):
        if self._obj_to_key(item) in self._rtseqs:
            return True
        return False

    def append(self, new):
        funcs_to_add = list()
        if inspect.isfunction(new) or isinstance(new, RealTimeSequence):
            funcs_to_add.append(new)
        elif inspect.ismodule(new):
            for func_name, func in inspect.getmembers(new, inspect.isfunction):
                if getattr(func, rt_seq_mode_id, None) is not None:
                    funcs_to_add.append(func)
        else:
            raise VeristandError()
        for func in [f for f in funcs_to_add if self._obj_to_key(f) not in self._rtseqs]:
            name = func.__name__
            self._rtseqs[name] = func
            if name not in self._dep_graph:
                self._dep_graph[name] = list()

    def count(self):
        len(self._rtseqs)

    def __iter__(self):
        return self._rtseqs.__iter__()

    def __setitem__(self, key, value):
        raise VeristandError()

    def __delitem__(self, key):
        raise VeristandError()

    def __reversed__(self):
        raise NotImplementedError

    def __index__(self):
        raise NotImplementedError()

    def extend(self):
        raise NotImplementedError()

    def insert(self):
        raise NotImplementedError()

    def pop(self, key, default=object()):
        raise NotImplementedError()

    def remove(self):
        raise NotImplementedError()

    def sort(self):
        raise NotImplementedError()

    def __add__(self, other):
        raise NotImplementedError()

    def __radd__(self, other):
        raise NotImplementedError()

    def __iadd__(self, other):
        raise NotImplementedError()

    def __mul__(self, other):
        raise NotImplementedError()

    def __imul__(self, other):
        raise NotImplementedError()

    def __rmul__(self, other):
        raise NotImplementedError()
