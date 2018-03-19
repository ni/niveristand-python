from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import CompilationEventType
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities import CompilerUtilities
from niveristand import _internal
from niveristand.errors import VeristandError

_internal.dummy()


def compile_rtseq(rtseq):
    success, _, compilation_events = \
        CompilerUtilities.TryGetCompiledInstance(rtseq, False, [], [])
    if not success:
        errormsg = " ".join([x.Message for x in compilation_events if x.EventType == CompilationEventType.Error])
        raise VeristandError(errormsg)
