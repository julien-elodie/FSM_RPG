from ..Action import Action
from ..Helper import (Logger, abilityModifiers, castDice, levelupRequiredExp,
                      modifyPrint)


"""Active
主动技能
"""


@Action(name="Attack")
def attack(self, target):
    # Attack Roll
    ret = castDice("1d20")
    if ret == 1:
        modifyPrint(["Doom!", self._name + "'s", "Attack", "missed."])
        hit = False
    elif ret == 20:
        modifyPrint(["Good Luck!", self._name,
                     "will take a excellent Attack!"])
        hit = True
    else:
        # Determine modifiers
        # Ability Modifier
        ret = ret + abilityModifiers(self._state.Str)
        # Proficiency Bonus @Philous 暂无
        # 与AC(护甲等级)比较
        ArmorClass = 10 + abilityModifiers(target._state.Dex)
        if ret >= ArmorClass:
            modifyPrint([self._name + "'s", "Attack", "hit."])
            hit = True
        else:
            modifyPrint([self._name + "'s", "Attack", "missed."])
            hit = False
    # Resolve the attack
    if hit:
        # TODO @Philous 武器输出未正确给出
        damage = castDice("1d8") + abilityModifiers(self._state.Str)
        if damage < 0:
            # 防止出现伤害为负
            damage = 0
        Logger.timestamp()
        modifyPrint(["[Attack]", self._name, "attacks", target._name + ",",
                     "inflicting", str(damage), "damage."])
        target.hurt(initiator=self, damage=damage)


@Action(name="Appear")
def appear(self):
    modifyPrint([self._name, "appears."])


@Action(name="Rest")
def rest(self):
    # 治疗投掷
    recovery = castDice(mode=self._state.HpDice)
    # 防止超量治疗
    preHp = self._state.Hp
    maxHp = int(self._state.HpDice.split(
        "d")[-1]) + abilityModifiers(self._state.Con)
    self._state.Hp = min(preHp + recovery, maxHp)
    modifyPrint([self._name, "recovered", str(self._state.Hp - preHp), "Hp."])

"""Passive
被动技能
"""


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
    requiredExp=levelupRequiredExp(level=self._state.Level + 1)
    if self._state.Exp >= requiredExp:
        self.level()


@Action(name="Level")
def level(self):
    self._state.Level += 1
    modifyPrint([self._name, "get to level", str(self._state.Level)])
    # TODO @Philous： 升级加点


"""Special
特殊技能
"""
