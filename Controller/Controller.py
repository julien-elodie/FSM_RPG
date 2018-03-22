from ..Machine import Machine

class Controller:
    """docstring for Controller."""
    def __init__(self, machine: Machine):
        super(Controller, self).__init__()
        self._CurrentState = machine.getState()
        self._Machine = machine
        # TODO
        
        