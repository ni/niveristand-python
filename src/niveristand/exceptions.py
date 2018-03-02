from niveristand.clientapi.realtimesequencedefinitionapi.erroraction import ErrorAction


class VeristandError(Exception):
    pass


class TranslateError(VeristandError):
    pass


class UnexpectedError(VeristandError):
    pass


class VeristandNotImplementedError(VeristandError):
    def __init__(self):
        """Throw Generic exception for things that are not implemented yet."""
        self.message = "Not Implemented"
        super(VeristandNotImplementedError, self).__init__(self.message)


class StopTaskException(Exception):
    pass


class RunError(VeristandError):
    def __init__(self, error):
        assert isinstance(error, SequenceError)
        self.error = error

    def get_all_errors(self):
        error = self.error
        while error:
            yield error
            error = error.inner_error

    @classmethod
    def RunErrorFactory(cls, error):
        assert isinstance(error, SequenceError)
        if error.error_action is ErrorAction.ContinueSequenceExecution:
            return RunFailedError(error)
        else:
            return RunAbortedError(error)


class RunFailedError(RunError):
    def __init__(self, error):
        super(RunFailedError, self).__init__(error)


class RunAbortedError(RunError):
    def __init__(self, error):
        super(RunAbortedError, self).__init__(error)


class SequenceError(VeristandError):
    def __init__(self, error_code, message, error_action):
        super(SequenceError, self).__init__(message)
        self.error_code = error_code
        self.error_action = error_action
        self.message = message
        self._inner_error = None

    @property
    def inner_error(self):
        return self._inner_error

    @inner_error.setter
    def inner_error(self, value):
        assert isinstance(value, SequenceError) or value is None
        assert self._inner_error is None
        self._inner_error = value

    @property
    def is_fatal(self):
        isfatal = (self.error_action in (ErrorAction.AbortSequence, ErrorAction.StopSequence)) or \
                  (self._inner_error and self.inner_error.is_fatal)
        return isfatal

    @property
    def should_raise(self):
        # If the error code was 0 in a Continue error then don't raise.
        return not (self.error_action is ErrorAction.ContinueSequenceExecution and self.error_code is 0)
