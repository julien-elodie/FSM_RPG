# Attr
class UncorrectAttrError(Exception):
    """docstring for UncorrectAttrError."""

    def __init__(self, ErrorInfo):
        super(UncorrectAttrError, self).__init__()
        self.errorinfo = ErrorInfo

    def __str__(self):
        return self.errorinfo
