from enum import Enum


class ErrorAction(Enum):
    """Actions you can take when calling :func:`niveristand.library.generate_error`."""

    ContinueSequenceExecution = 0  #: Continues execution but still fails the test run.
    StopSequence = 1  #: Stops execution and calls all try/finally blocks.
    AbortSequence = 2  #: Stops execution and avoid calling try/finally blocks.
