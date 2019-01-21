from niveristand.errors import RunError, VeristandNotImplementedError


def run_py_as_rtseq(toplevelfunc, rtseq_params={}):
    """
    Runs a Python function as an RT sequence in the VeriStand Engine.

    Args:
        toplevelfunc: the Python function to run.
        rtseq_params (Dict[str, niveristand.clientapi._datatypes.rtprimitives.DoubleValue]):  the parameters to be
         passed to the RT sequence.

    Returns:
        Union[float, None]:
        The numeric value returned by the real-time sequence execution.

    Raises:
        :any:`TranslateError`: if the function is not successfully translated.
        :any:`RunAbortedError`: if this function calls :any:`generate_error` with an action of Abort or Stop.
        :any:`RunFailedError`: if this function calls :any:`generate_error` with a Continue action.

    """
    from niveristand.clientapi import RealTimeSequence
    seq = RealTimeSequence(toplevelfunc)
    result_state = seq.run(rtseq_params)
    result_state.wait_for_result()
    result_state.session.undeploy()
    if result_state.last_error:
        raise RunError.RunErrorFactory(result_state.last_error)
    return result_state.ret_val


def save_rtseq_as_py(toplevelseq, srcfolder, destfolder):
    raise VeristandNotImplementedError()


def save_py_as_rtseq(toplevelfunc, dest_folder):
    """
    Saves a Python function as an RT sequence that is compatible with the Stimulus Profile Editor.

    Args:
        toplevelfunc: the Python function you want to save.
        dest_folder[str]: the folder you want to save the sequence and all its dependencies in.

    Returns:
        The full path to the main sequence file.

    Raises:
        :class:`niveristand.errors.TranslateError`: if the function is not successfully translated.

    """
    from niveristand.clientapi import RealTimeSequence
    seq = RealTimeSequence(toplevelfunc)
    filename = seq.save(dest_folder)
    return filename


def validate_py_as_rtseq(toplevelobj):
    raise VeristandNotImplementedError()


def run_rtseq(toplevelseq, destfolder):
    raise VeristandNotImplementedError()
