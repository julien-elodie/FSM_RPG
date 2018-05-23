from ..Action import Action
from ..Helper import modifyPrint


# Active
@Action(name="attack")
def attack(self, target):
    damage = self._state.STR
    modifyPrint([self._name, "attacks", target._name + ",",
                    "inflicting", str(damage), "damage."])
    target.hurt(damage=damage)                    

# Passive
@Action(name="hurt")
def hurt(self, damage):
    modifyPrint([self._name, "suffered", str(damage), "damage."])