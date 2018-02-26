from enum import Enum


class ErrorAction(Enum):
    ContinueSequenceExecution = 0
    StopSequence = 1
    AbortSequence = 2
