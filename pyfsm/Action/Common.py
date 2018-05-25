from ..Action import Action
from ..Helper import levelupRequiredExp, modifyPrint


# Active
@Action(name="Attack")
def attack(self, target):
    damage = self._state.Str
    modifyPrint([self._name, "attacks", target._name + ",",
                 "inflicting", str(damage), "damage."])
    target.hurt(initiator=self, damage=damage)


@Action(name="Appear")
def appear(self):
    modifyPrint([self._name, "appears."])


# Passive
@Action(name="Hurt")
def hurt(self, initiator, damage):
    modifyPrint([self._name, "suffered", str(damage), "damage."])
    self._state.Hp -= damage
    if self._state.Hp <= 0:
        self.defeated(initiator=initiator)
        if initiator._name == "Hero":
            initiator.victory()


@Action(name="Defeated")
def defeated(self, initiator):
    modifyPrint([self._name, "is defeated by", initiator._name + "."])
    initiator.exp(self._state.Exp)


@Action(name="Victory")
def victory(self):
    modifyPrint(["Victory!"])


@Action(name="Exp")
def exp(self, value):
    modifyPrint([self._name, "gain", str(value), "exp."])
    self._state.Exp += value
    requiredExp = levelupRequiredExp(level=self._state.Level)
    if self._state.Exp >= requiredExp:
        self.level(requiredExp=requiredExp)


@Action(name="Level")
def level(self, requiredExp):
    self._state.Exp -= requiredExp
    self._state.Level += 1
    modifyPrint([self._name, "get to level", str(self._state.Level)])
    # TODO @Philous： 升级加点
