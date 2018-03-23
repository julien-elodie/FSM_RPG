from ..Event import ActiveEvent
from ..Event import PassiveEvent
from ..Transition import Transition


class State:
    """docstring for State."""

    def __init__(self, name: str = "State"):
        """[summary]
        Keyword Arguments:
            name {str} -- [description] (default: {"State"})
        """
        super(State, self).__init__()
        self._Name = name
        self._Actives = []
        self._Passives = []
        self._Transitions = {}

    def addActive(self, active: ActiveEvent):
        """[summary]
        Arguments:
            active {ActiveEvent} -- [description]
        """
        if active in self._Actives:
            return
        else:
            self._Actives.append(active)

    def addPassive(self, passive: PassiveEvent):
        if passive in self._Passives:
            return
        else:
            self._Passives.append(passive)

    def addTransition(self, passive: PassiveEvent, target):
        """[summary]
        Arguments:
            passive {PassiveEvent} -- [description]
            target {State} -- [description]
        """
        self._Transitions[passive.getName] = Transition(self, passive, target)

    def getAllTargets(self):
        return [_.getTarget() for _ in self._Transitions.values()]

    def hasTransition(self, name: str):
        """[summary]
        Arguments:
            name {str} -- [description]
        """
        return name in self._Transitions.keys()

    def getTarget(self, name: str):
        """[summary]
        Arguments:
            name {str} -- [description]
        """
        return self._Transitions.get(name).getTarget()

    # TODO
    def executeActions(self):
        pass
