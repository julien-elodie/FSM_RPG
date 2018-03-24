from ..Machine import Machine
from ..State import State


class Controller:
    """docstring for Controller."""

    def __init__(self, machine: Machine):
        super(Controller, self).__init__()
        self._CurrentState = machine.getState()
        self._Machine = machine
        # TODO

    def getCurrentState(self):
        return self._CurrentState

    def handle(self, name: str):
        print(self._CurrentState.getActive(name).getCode())
        if self._CurrentState.hasTransition(name):
            print(
                self._CurrentState.getPassive(
                    self._CurrentState.getBind(name)).getCode())
            self.transitionTo(self._CurrentState.getTarget(name))
            return
        if self._Machine.isResetEvent(name):
            self.transitionTo(self._Machine.getState())
            return

    def transitionTo(self, target: State):
        self._CurrentState = target
        self._CurrentState.executeActions()
