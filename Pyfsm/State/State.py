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
        self._Actives = {}
        self._Passives = {}
        self._Binds = {}
        self._Transitions = {}

    def getName(self):
        return self._Name

    def getActive(self, name: str):
        return self._Actives.get(name)

    def getPassive(self, name: str):
        return self._Passives.get(name)

    def addBind(self, active: ActiveEvent, passive: PassiveEvent):
        self._Binds[active] = passive

    def getBind(self, active: ActiveEvent):
        return self._Binds[active]

    def addActive(self, active: ActiveEvent):
        """[summary]
        Arguments:
            active {ActiveEvent} -- [description]
        """
        if active.getName() in self._Actives.keys():
            return
        else:
            self._Actives[active.getName()] = active

    def addPassive(self, passive: PassiveEvent):
        if passive.getName() in self._Passives.keys():
            return
        else:
            self._Passives[passive.getName()] = passive

    def addTransition(self, passive: PassiveEvent, target):
        """[summary]
        Arguments:
            passive {PassiveEvent} -- [description]
            target {State} -- [description]
        """
        self._Transitions[passive.getName()] = Transition(
            self, passive, target)

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
        print(self.getName())
