from niveristand import errormessages
from niveristand.clientapi import stimulusprofileapi
from niveristand.exceptions import RunAbortedError, RunFailedError, VeristandNotImplementedError
from niveristand.translation import RealTimeSequence


def run_py_as_rtseq(toplevelfunc, timeout_within_each_step=100000):
    seq = RealTimeSequence(toplevelfunc)
    result_state = seq.run(timeout_within_each_step=timeout_within_each_step)
    result_state.wait_for_result()
    result_state.session.Undeploy()
    if result_state.completion_state == stimulusprofileapi.StimulusProfileState.CompletionState.Aborted:
        raise RunAbortedError(errormessages.run_aborted)
    elif result_state.completion_state == stimulusprofileapi.StimulusProfileState.CompletionState.Failed:
        raise RunFailedError(errormessages.run_failed)
    return result_state.ret_val


def save_rtseq_as_py(toplevelseq, srcfolder, destfolder):
    raise VeristandNotImplementedError()


def save_py_as_rtseq(toplevelobj, destfolder):
    seq = RealTimeSequence(toplevelobj)
    filename = seq.save(destfolder)
    return filename


def validate_py_as_rtseq(toplevelobj):
    raise VeristandNotImplementedError()


def run_rtseq(toplevelseq, destfolder):
    raise VeristandNotImplementedError()
