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
            doc {dict} -- [description] (default: {
                {
                    "new": "A new ActiveEvent!",
                    "del": "Event Finished!"
                }
            })
        """
        self._Doc = doc
        self._Name = name
        self._Func = self._defaultFunc

    def executeEvent(self):
        print(self._Doc.get("new"))
        self._Func()
        print(self._Doc.get("del"))
