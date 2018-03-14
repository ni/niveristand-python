from niveristand._exceptions import RunError, VeristandNotImplementedError


def run_py_as_rtseq(toplevelfunc, timeout_within_each_step=100000):
    from niveristand import RealTimeSequence
    seq = RealTimeSequence(toplevelfunc)
    result_state = seq.run(timeout_within_each_step=timeout_within_each_step)
    result_state.wait_for_result()
    result_state.session.Undeploy()
    if result_state.last_error:
        raise RunError.RunErrorFactory(result_state.last_error)
    return result_state.ret_val


def save_rtseq_as_py(toplevelseq, srcfolder, destfolder):
    raise VeristandNotImplementedError()


def save_py_as_rtseq(toplevelobj, destfolder):
    from niveristand import RealTimeSequence
    seq = RealTimeSequence(toplevelobj)
    filename = seq.save(destfolder)
    return filename


def validate_py_as_rtseq(toplevelobj):
    raise VeristandNotImplementedError()


def run_rtseq(toplevelseq, destfolder):
    raise VeristandNotImplementedError()
