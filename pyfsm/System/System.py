import copy
import os
import random
import time

from ..Generator import Generator
from ..Helper import Logger, abilityChecks, modifyPrint, weightedChoice


class System(object):
    """docstring for System."""

    @Logger(msg="[System] Welcome to the fantastic world!")
    def __init__(self, seed=None):
        super(System, self).__init__()
        # save random seed
        self._seed = seed
        self._generator = Generator()
        self.loadHero()
        self._Monster = None
        self._Monsters = []
        self.LoadMonsters()

    @Logger(msg="[System] Loading Hero...")
    def loadHero(self):
        self._generator.loadConfig(filepath="./pyfsm/json/Hero/Hero.json")
        self._Hero = self._generator.generate()

    @Logger(msg="[System] Loading Monsters...")
    def LoadMonsters(self):
        for _, _, files in os.walk("./pyfsm/json/Monsters/"):
            for file in files:
                Monster = file.split(".")[0]
                self._Monsters.append(Monster)
                self._generator.loadConfig(
                    filepath="./pyfsm/json/Monsters/" + file)
                setattr(self, "_" + Monster, self._generator.generate())

    def Start(self):
        while True:
            self.SearchMonsters()
            self.Battle()

    @Logger(msg="[System] Searching Monsters...")
    def SearchMonsters(self):
        time.sleep(abs(random.gauss(5, 1.5)))
        self._Monster = copy.deepcopy(
            getattr(self, "_" + random.choice(self._Monsters)))
        self._Monster.appear()

    @Logger(msg="[System] Battle Start!")
    def Battle(self):
        Combat(Participants=[self._Hero, self._Monster])


class Combat(object):
    """docstring for Combat."""

    def __init__(self, Participants=[]):
        super(Combat, self).__init__()
        self._Participants = Participants
        self._combatRound = 1
        self._endCombat = False
        # Start
        self.DetermineSuperise()
        self.EstablishPositions()
        self.RollInitiative()
        while not self._endCombat:
            self.CombatRound()

    @Logger(msg="[Combat] Determining Superise.")
    def DetermineSuperise(self):
        # 突袭
        # TODO @Philous 暂无
        Logger.timestamp()
        modifyPrint(["[Combat] No Superise."])

    @Logger(msg="[Combat] Establishing Positions.")
    def EstablishPositions(self):
        # 决定位置
        # TODO @Philous 由于机制无法实现
        pass

    @Logger(msg="[Combat] Rolling Initiative.")
    def RollInitiative(self):
        # 先攻
        self._DexRank = {}
        for Participant in self._Participants:
            # 平手
            while True:
                checkPoints = abilityChecks("Dex", Participant._state.Dex)
                if checkPoints not in self._DexRank.values():
                    break
            self._DexRank[Participant] = checkPoints
        # sort
        self._DexRank = sorted(self._DexRank.items(),
                               key=lambda item: item[1], reverse=True)
        self._DexRank = dict(self._DexRank).keys()
        Logger.timestamp()
        modifyPrint(["[Initiative] The round order is:", ' '.join(
            [str(i + 1) + ", " + Participant._name for i, Participant in zip(range(len(self._DexRank)), self._DexRank)]) + "."])

    def CombatRound(self):
        Logger.timestamp()
        modifyPrint(["[Combat] Round " + str(self._combatRound) + "."])
        # TODO @Philous 战斗轮流程
        for Participant in self._DexRank:
            self.TakeTurns(owner=Participant)
        
        self._combatRound += 1

    def TakeTurns(self, owner):
        Logger.timestamp()
        modifyPrint(["[Combat]", owner._name + "'s", "turns"])
        # Move @philous 由于机制无法实现
        # Action
        self.ChooseAction(owner=owner)
        # 判断是否存活
        for Participant in self._DexRank:
            if Participant._state.Hp <= 0:
                self._combatRound = 1
                self._endCombat = True
                break

    def ChooseAction(self, owner):
        # TODO @Philous 技能待补全
        actions = ["Attack", "CastSpell", "Disengage", "Dodge", "UseObject"]
        weights = [1,0,0,0,0]
        action = actions[weightedChoice(weights=weights)]
        # TODO @Philous 决策待完善
        if action == "Attack":
            # Choose a target
            target = random.choice([Participant for Participant in self._DexRank if Participant._name is not owner._name]) #TODO
            owner.attack(target=target)
