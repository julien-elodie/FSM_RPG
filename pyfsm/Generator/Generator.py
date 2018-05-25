import json
import sys

from ..Action.Common import appear, attack, defeated, exp, hurt, level, victory
from ..Machine import Machine
from ..State import State


class Generator(object):
    """docstring for Generator."""

    def __init__(self):
        super(Generator, self).__init__()

    def loadConfig(self, filepath):
        with open(filepath, 'r') as Config:
            self._json = json.load(Config)

    def generate(self):
        machine = Machine(name=self._json.get("Name"))
        state = State(name="init")
        state.updateAttrs(attrs=self._json.get(
            "States").get("init").get("Attr"))
        machine.updateState(state)
        # Active
        for active in self._json.get("Actions").get("Active"):
            active = getattr(sys.modules[__name__], active)
            machine.updateAction(active)
        # Passive
        for passive in self._json.get("Actions").get("Passive"):
            passive = getattr(sys.modules[__name__], passive)
            machine.updateAction(passive)
        return machine
