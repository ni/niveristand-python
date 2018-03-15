from niveristand._exceptions import RunError, VeristandNotImplementedError


def run_py_as_rtseq(toplevelfunc, timeout_within_each_step=100000):
    """
    Run a Python function as a Real-Time Sequence in the VeriStand Engine.

    Args:
        toplevelfunc: the Python function to run.
        timeout_within_each_step (Optional[int]): Timeout for each step before execution is aborted.

    Returns:
        The numeric value returned by the Real-Time Sequence execution.

    Raises:
        :class:`niveristand.TranslateError`: if the function could not be successfully translated.
        :class:`niveristand.RunAbortedError`: if :func:`niveristand.library.generate_error` was called with an action of Abort or Stop.
        :class:`niveristand.RunFailedError`: if :func:`niveristand.library.generate_error` was called with a Continue action.

    """
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


def save_py_as_rtseq(toplevelfunc, dest_folder):
    """
    Save a Python function as a Real-Time Sequence that is compatible with Stimulus Profile Editor.

    Args:
        toplevelfunc: the Python function to save.
        dest_folder[str]: the folder to save the sequence and all its dependencies to.

    Returns:
        The full path to the main sequence file.

    Raises:
        TranslateError: if the function could not be successfully translated.

    """
    from niveristand import RealTimeSequence
    seq = RealTimeSequence(toplevelfunc)
    filename = seq.save(dest_folder)
    return filename


def validate_py_as_rtseq(toplevelobj):
    raise VeristandNotImplementedError()


def run_rtseq(toplevelseq, destfolder):
    raise VeristandNotImplementedError()
