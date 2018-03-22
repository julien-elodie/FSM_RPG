from ..State import State
from ..Event import PassiveEvent


class Transition:
    """docstring for Transition."""

    def __init__(self, source: State, trigger: PassiveEvent, target: State):
        """[summary]
        
        Arguments:
            source {State} -- [description]
            trigger {PassiveEvent} -- [description]
            target {State} -- [description]
        """
        super(Transition, self).__init__()
        self._Source = source
        self._Trigger = trigger
        self._Target = target

    def getSource(self):
        return self._Source

    def setSource(self, source: State):
        self._Source = source

    def getTrigger(self):
        return self._Trigger

    def setTrigger(self, trigger: PassiveEvent):
        self._Trigger = trigger

    def getTarget(self):
        return self._Target

    def setTarget(self, target: State):
        self._Target = target

    # TODO
