from .Event import Event


class PassiveEvent(Event):
    """docstring for PassiveEvent."""

    def __init__(self, name: str = "PassiveEvent", code: str = "Code"):
        """[summary]
        Keyword Arguments:
            name {str} -- [description] (default: {"PassiveEvent"})
            code {str} -- [description] (default: {"Code"})
        """
        super(PassiveEvent, self).__init__()
        Event.__init__(self, name=name, code=code)