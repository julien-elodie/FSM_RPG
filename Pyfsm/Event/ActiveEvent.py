from .Event import Event


class ActiveEvent(Event):
    """docstring for ActiveEvent."""

    def __init__(self, name: str = "ActiveEvent", code: str = "Code"):
        """[summary]
        Keyword Arguments:
            name {str} -- [description] (default: {"ActiveEvent"})
            code {str} -- [description] (default: {"Code"})
        """
        super(ActiveEvent, self).__init__()
        Event.__init__(self, name=name, code=code)
