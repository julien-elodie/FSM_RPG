from ..Machine import Machine
from ..State import State


class Controller:
    """docstring for Controller."""

    def __init__(self, machine: Machine):
        super(Controller, self).__init__()
        self._CurrentState = machine.getState()
        self._Machine = machine
        # TODO

    def handle(self, name: str):
        if self._CurrentState.HasTransition(name):
            self.transitionTo(self._CurrentState.getTarget(name))
            return
        if self._Machine.isResetEvent(name):
            self.transitionTo(self._Machine.getState())
            return

    def transitionTo(self, target: State):
        self._CurrentState = target
        self._CurrentState.executeActions()
