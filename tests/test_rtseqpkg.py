import os
import sys
import tempfile
from niveristand import nivs_rt_sequence
from niveristand.clientapi import I32Value, RealTimeSequence
from niveristand.clientapi.realtimesequencepkg import RealTimeSequencePkg

__num_of_valid_rtseqs__ = 4


@nivs_rt_sequence
def empty_func():
    pass


@nivs_rt_sequence
def returns_one():
    return 1


@nivs_rt_sequence
def calls_another():
    a = I32Value(0)
    a.value = returns_one()
    return a.value


@nivs_rt_sequence
def two_levels_deep():
    a = I32Value(0)
    a.value = calls_another()
    a.value += returns_one()
    empty_func()
    return a.value


def test_rtseqpkg_create_empty():
    pkg = RealTimeSequencePkg()
    assert len(pkg) == 0


def test_rtseqpkg_append_module():
    mod = sys.modules[__name__]
    pkg = RealTimeSequencePkg()
    pkg.append(mod)
    assert len(pkg) == __num_of_valid_rtseqs__


def test_rtseqpkg_append_func():
    pkg = RealTimeSequencePkg()
    pkg.append(empty_func)
    assert len(pkg) == 1


def test_rtseqpkg_index_returns_RealTimeSequence():
    pkg = RealTimeSequencePkg()
    pkg.append(empty_func)
    assert isinstance(pkg[empty_func], RealTimeSequence)


def test_rtseqpkg_can_iterate():
    pkg = RealTimeSequencePkg()
    pkg.append(empty_func)
    pkg.append(returns_one)
    assert isinstance(pkg[empty_func], RealTimeSequence)
    assert isinstance(pkg[returns_one], RealTimeSequence)


def test_rtseqpkg_append_dup_doesnt_append():
    pkg = RealTimeSequencePkg()
    pkg.append(empty_func)
    pkg.append(empty_func)
    assert len(pkg) == 1


def test_rtseqpkg_contains():
    pkg = RealTimeSequencePkg()
    pkg.append(empty_func)
    assert empty_func in pkg
    assert returns_one not in pkg
    pkg.append(returns_one)
    assert returns_one in pkg


def test_save_all_module():
    pkg = RealTimeSequencePkg()
    folder = tempfile.mkdtemp()
    pkg.append(sys.modules[__name__])
    pkg.save_all(folder)
    _, _, files = next(os.walk(folder))
    assert len(pkg) == __num_of_valid_rtseqs__
    assert len(files) == len(pkg)


def test_rtseq_with_deps():
    seq = RealTimeSequence(calls_another)
    folder = tempfile.mkdtemp()
    seq.save(folder)
    _, _, files = next(os.walk(folder))
    assert len(files) == 2


def test_rtseq_with_deps_multiple_times():
    seq = RealTimeSequence(calls_another)
    folder = tempfile.mkdtemp()
    seq.save(folder)
    root, _, files = next(os.walk(folder))
    assert len(files) == 2
    for file in files:
        os.remove(os.path.join(root, file))
    seq.save(folder)
    _, _, files = next(os.walk(folder))
    assert len(files) == 2


def test_rtseq_with_deps_multiple_times_diff_folder():
    seq = RealTimeSequence(calls_another)
    folder = tempfile.mkdtemp()
    seq.save(folder)
    _, _, files = next(os.walk(folder))
    assert len(files) == 2
    folder = tempfile.mkdtemp()
    seq.save(folder)
    _, _, files = next(os.walk(folder))
    assert len(files) == 2


def test_rtseq_several_calls():
    seq = RealTimeSequence(two_levels_deep)
    folder = tempfile.mkdtemp()
    seq.save(folder)
    _, _, files = next(os.walk(folder))
    assert len(files) == 4
