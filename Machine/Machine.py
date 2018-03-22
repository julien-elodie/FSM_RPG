from ..State import State
from ..Event import PassiveEvent


class Machine:
    """docstring for Machine."""

    def __init__(self, state: State):
        """[summary]
        
        Arguments:
            start {State} -- [description]
        """
        super(Machine, self).__init__()
        self._State = state
        self._ResetEvents = []

    def getState(self):
        return self._State

    def setState(self, state: State):
        self._State = state

    def getAllStates(self):
        result = []
        self.collectStates(result, self._State)
        return result

    def collectStates(self, result: list, state: State):
        if state in result:
            return
        else:
            result.append(state)
        for target in state.getAllTargets():
            self.collectStates(result, target)

    def addResetEvent(self, passive: PassiveEvent):
        for state in self.getAllStates():
            if state.hasTransition(passive.getName()):
                continue
            state.addTransition(passive, self._State)
            if passive in self._ResetEvents:
                continue
            self._ResetEvents.append(passive)

    def isResetEvent(self, name: str):
        # TODO
        pass
