from .Event import Event


class ActiveEvent(Event):
    """docstring for ActiveEvent."""

    def __init__(self,
                 name: str = "ActiveEvent",
                 doc: dict = {
                     "new": "A new ActiveEvent!",
                     "del": "Event Finished!"
                 }):
        """[summary]
        
        Keyword Arguments:
            name {str} -- [description] (default: {"ActiveEvent"})
            doc {dict} -- [description] (default: {{"new": "A new ActiveEvent!","del": "Event Finished!"}})
        """
        self._Doc = doc
        print(self._Doc.get("new"))
        self._Name = name
        self._Func = self._defaultFunc()
        print(self._Doc.get("del"))