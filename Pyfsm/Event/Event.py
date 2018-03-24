class Event:
    """docstring for Event."""

    def __init__(self, name: str = "Event", code: str = "Code"):
        """[summary]
        Keyword Arguments:
            name {str} -- [description] (default: {"Event"})
            code {str} -- [description] (default: {"Code"})
        """
        super(Event, self).__init__()
        self._Name = name
        self._Code = code

    def getName(self):
        return self._Name

    def _setName(self, name: str):
        self._Name = name

    def getCode(self):
        return self._Code

    def _setCode(self, code: str):
        self._Code = code