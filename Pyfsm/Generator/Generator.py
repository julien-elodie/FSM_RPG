import json

from Pyfsm.Event import ActiveEvent
from Pyfsm.Event import PassiveEvent
from Pyfsm import State
from Pyfsm import Machine


class Generator(object):
    """docstring for Generator."""

    def __init__(
            self,
            doc: dict = {
                "Active": [{
                    "name": "Open",
                    "code": "open the door"
                }, {
                    "name": "Close",
                    "code": "close the door"
                }],
                "Passive": [{
                    "name": "Opened",
                    "code": "Door is opening"
                }, {
                    "name": "Closed",
                    "code": "Door is closing"
                }],
                "State": [{
                    "name":
                    "Opened door",
                    "active": ["Close"],
                    "passive": ["Closed"],
                    "bind": [{
                        "active": "Close",
                        "passive": "Closed"
                    }],
                    "transition": [{
                        "active": "Close",
                        "target": "Closed door"
                    }]
                }, {
                    "name":
                    "Closed door",
                    "active": ["Open"],
                    "passive": ["Opened"],
                    "bind": [{
                        "active": "Open",
                        "passive": "Opened"
                    }],
                    "transition": [{
                        "active": "Open",
                        "target": "Opened door"
                    }]
                }],
                "Machine": {
                    "start": "Closed door"
                }
            }):
        super(Generator, self).__init__()
        self._Doc = doc
        self._Active = {}
        self._Passive = {}
        self._State = {}
        self._Machine = None

    def printDoc(self):
        print(json.dumps(self._Doc, indent=2))

    def generatorMachine(self):
        for active in self._Doc["Active"]:
            self._Active[active["name"]] = ActiveEvent(active["name"],
                                                       active["code"])

        for passive in self._Doc["Passive"]:
            self._Passive[passive["name"]] = PassiveEvent(
                passive["name"], passive["code"])

        for state in self._Doc["State"]:
            self._State[state["name"]] = State(state["name"])

        for state in self._Doc["State"]:
            for active in state["active"]:
                self._State[state["name"]].addActive(self._Active[active])
            for passive in state["passive"]:
                self._State[state["name"]].addPassive(self._Passive[passive])
            for bind in state["bind"]:
                self._State[state["name"]].addBind(bind["active"],
                                                   bind["passive"])
            for transition in state["transition"]:
                self._State[state["name"]].addTransition(
                    self._Active[transition["active"]],
                    self._State[transition["target"]])

        self._Machine = Machine(self._State[self._Doc["Machine"]["start"]])
        print(self._Machine.getState().getName())
        return self._Machine
