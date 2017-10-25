from niveristand.exceptions import VeristandNotImplementedError
from niveristand.translation import RealTimeSequence


def run_py_as_rtseq(toplevelfunc, wait_until_complete=True):
    raise VeristandNotImplementedError()


def save_rtseq_as_py(toplevelseq, srcfolder, destfolder):
    raise VeristandNotImplementedError()


def save_py_as_rtseq(toplevelobj, destfolder):
    seq = RealTimeSequence(toplevelobj)
    seq.save(destfolder)
    return


def validate_py_as_rtseq(toplevelobj):
    raise VeristandNotImplementedError()


def run_rtseq(toplevelseq, destfolder):
    raise VeristandNotImplementedError()
