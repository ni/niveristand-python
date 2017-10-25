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
