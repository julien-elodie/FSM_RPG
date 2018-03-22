from .Event import Event


class PassiveEvent(Event):
    """docstring for PassiveEvent."""

    def __init__(self,
                 name: str = "PassiveEvent",
                 doc: dict = {
                     "new": "A new PassiveEvent!",
                     "del": "Event Finished!"
                 }):
        """[summary]
        
        Keyword Arguments:
            name {str} -- [description] (default: {"PassiveEvent"})
            doc {dict} -- [description] (default: {{"new": "A new PassiveEvent!","del": "Event Finished!"}})
        """
        self._Doc = doc
        print(self._Doc.get("new"))
        self._Name = name
        self._Func = self._defaultFunc()
        print(self._Doc.get("del"))