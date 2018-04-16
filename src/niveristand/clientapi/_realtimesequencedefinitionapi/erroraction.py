from enum import Enum


class ErrorAction(Enum):
    """Actions you can take when calling :func:`niveristand.library.generate_error`."""

    ContinueSequenceExecution = 0  #: Continue execution but still fail the test run.
    StopSequence = 1  #: Stop execution and call all try/finally blocks.
    AbortSequence = 2  #: Stop execution and avoid calling try/finally blocks.
