import copy
import os
import random
import time

from ..Generator import Generator
from ..Helper import Logger, abilityChecks, modifyPrint


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
        time.sleep(abs(random.gauss(10, 3)))
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
        # start
        self.DetermineSuperise()
        self.EstablishPositions()
        self.RollInitiative()
        while not self._endCombat:
            self.CombatRound()

    @Logger(msg="[Combat] Determining Superise!")
    def DetermineSuperise(self):
        # 突袭
        # TODO @Philous 暂无
        Logger.timestamp()
        modifyPrint(["[Combat] No Superise."])

    @Logger(msg="[Combat] Establishing Positions!")
    def EstablishPositions(self):
        # 决定位置
        # TODO @Philous 由于机制无法实现
        pass

    @Logger(msg="[Combat] Rolling Initiative!")
    def RollInitiative(self):
        # 先攻
        self._DexRank = {}
        for Participant in self._Participants:
            # 平手
            while True:
                checkPoints = abilityChecks("Dex", Participant._state.Dex)
                if checkPoints not in self._DexRank.values():
                    break
            self._DexRank[Participant._name] = checkPoints
        # sort
        self._DexRank = sorted(self._DexRank.items(),
                               key=lambda item: item[1], reverse=True)
        self._DexRank = dict(self._DexRank).keys()
        Logger.timestamp()
        modifyPrint(["[Initiative] The round order is:", ' '.join(
            [str(i + 1) + ", " + Participant for i, Participant in zip(range(len(self._DexRank)), self._DexRank)]) + "."])

    
    def CombatRound(self):
        Logger.timestamp()
        modifyPrint(["[Combat] Round" + str(self._combatRound) + "."])
        self._combatRound += 1
        # TODO @Philous 战斗轮流程
        if self._combatRound > 3:
            self._endCombat = True
            self._combatRound = 1
