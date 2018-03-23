class Event:
    """docstring for Event."""

    def __init__(self, name: str = "Event"):
        """[summary]

        Keyword Arguments:
            name {str} -- [description] (default: {"Event"})
        """
        super(Event, self).__init__()
        self._Name = name
        self._Func = self._defaultFunc

    def getName(self):
        return self._Name

    def setName(self, name: str):
        self._Name = name

    def getFunc(self):
        return self._Func

    def setFunc(self, func):
        self._Func = func if func else self._defaultFunc

    def _defaultFunc(self):
        print("This is an default function.")

    def executeEvent(self):
        self._Func()