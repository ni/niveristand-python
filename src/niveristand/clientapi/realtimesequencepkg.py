import collections
import inspect
from niveristand import RealTimeSequence
from niveristand.decorators import Modes
from niveristand.exceptions import VeristandError


class RealTimeSequencePkg(collections.MutableMapping):
    def __init__(self):
        self._rtseqs = dict()
        self._unresolved = list()

    def save_all(self, path):
        for seq in self:
            self[seq].save(path)

    def save_referenced(self, path):
        for seq in [s for s in self._rtseqs if isinstance(self._rtseqs[s], RealTimeSequence)]:
            self._rtseqs[seq].save(path)

    def add_referenced_sequence(self, referenced_sequence):
        referenced_sequence = str(referenced_sequence)
        if referenced_sequence not in self:
            self._unresolved.append(referenced_sequence)
        else:
            self._resolve(referenced_sequence)

    def get_referenced(self):
        return [self[r] for r in self._rtseqs if isinstance(self._rtseqs[r], RealTimeSequence)]

    def __len__(self):
        return len(self._rtseqs)

    def __getitem__(self, item):
        item = self._obj_to_key(item)
        self._resolve(item)
        return self._rtseqs.get(item)

    def _obj_to_key(self, item):
        return str(item) if not inspect.isfunction(item) else item.__name__

    def _resolve(self, item):
        seq = self._rtseqs.get(item)
        if inspect.isfunction(seq):
            seq = RealTimeSequence(seq)
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
                try:
                    if func(__rtseq_mode__=Modes.CHECK):
                        funcs_to_add.append(func)
                except TypeError:
                    pass
        else:
            raise VeristandError()
        for func in [f for f in funcs_to_add if self._obj_to_key(f) not in self._rtseqs]:
            name = func.__name__
            self._rtseqs[name] = func
            if name in self._unresolved:
                self._resolve(name)
                self._unresolved.remove(name)

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
