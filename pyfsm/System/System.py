import copy
import os
import random
import time

from ..Error import EmptyHerosOrMonstersError
from ..Generator import Generator
from ..Helper import Logger, abilityChecks, modifyPrint, weightedChoice


class System(object):
    """托管角色行为，怪物遭遇的基础类"""

    @Logger(msg="[System] Welcome to the fantastic world!")
    def __init__(self, seed=None):
        super(System, self).__init__()
        # save random seed
        self._seed = seed
        # 生成器
        self._generator = Generator()
        # 加载角色
        self.loadHero()
        # 加载怪物
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
        """托管主流程，暂时只有遭遇怪物和战斗，预计增加，场景切换，随机事件等
        """

        while True:
            self.SearchMonsters()
            self.Battle()

    @Logger(msg="[System] Searching Monsters...")
    def SearchMonsters(self):
        # 随机化搜寻时间
        time.sleep(abs(random.gauss(5, 1.5)))
        # 深拷贝，防止原始对象被篡改
        self._Monster = copy.deepcopy(
            getattr(self, "_" + random.choice(self._Monsters)))
        self._Monster.appear()

    @Logger(msg="[System] Battle Start!")
    def Battle(self):
        # 生成战斗对象索引字典，方便多对多的战斗
        Participants = {
            "Heros": [self._Hero],
            "Monsters": [self._Monster]
        }
        # 战斗托管
        Combat(Participants=Participants)
        # 战斗结束后恢复
        self._Hero.rest()


class Combat(object):
    """托管战斗的基础类"""

    def __init__(self, Participants={"Heros": [], "Monsters": []}):
        """战斗对象不可缺省

        Keyword Arguments:
            Participants {dict} -- 战斗对象索引字典 (default: {{"Heros": [], "Monsters": []}})

        Raises:
            EmptyHerosOrMonstersError -- 战斗对象中英雄或者怪物为空异常
        """

        super(Combat, self).__init__()
        # 判断是否有战斗对象
        try:
            if not len(Participants.get("Heros")) + len(Participants.get("Monsters")):
                raise EmptyHerosOrMonstersError("Empty Heros Or Monsters!")
        except EmptyHerosOrMonstersError as error:
            print(error.errorinfo)
        else:
            self._Heros = Participants.get("Heros")
            self._Monsters = Participants.get("Monsters")
            self._Participants = self._Heros + self._Monsters
        self._combatRound = 1
        self._endCombat = False
        # Start Combat
        self.DetermineSuperise()
        self.EstablishPositions()
        self.RollInitiative()
        while not self._endCombat:
            self.CombatRound()

    @Logger(msg="[Combat] Determining Superise.")
    def DetermineSuperise(self):
        """突袭
        # TODO @Philous 暂无
        """

        Logger.timestamp()
        modifyPrint(["[Superise] No Superise."])

    @Logger(msg="[Combat] Establishing Positions.")
    def EstablishPositions(self):
        """决定位置
        TODO @Philous 由于机制无法实现
        """

        pass

    @Logger(msg="[Combat] Rolling Initiative.")
    def RollInitiative(self):
        """先攻
        """

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
        """战斗轮
        """

        Logger.timestamp()
        modifyPrint(["[Combat] Round " + str(self._combatRound) + "."])
        # TODO @Philous 战斗轮流程
        for Participant in self._DexRank:
            if not self._endCombat:
                self.TakeTurns(owner=Participant)
        self._combatRound += 1

    def TakeTurns(self, owner):
        """每个对象的回合

        Arguments:
            owner {Machine} -- 参与战斗轮的对象
        """

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
        """对象的行动

        Arguments:
            owner {Machine} -- 参与战斗轮的对象
        """

        # TODO @Philous 技能待补全
        actions = ["Attack", "CastSpell", "Disengage", "Dodge", "UseObject"]
        weights = [1, 0, 0, 0, 0]
        action = actions[weightedChoice(weights=weights)]
        # TODO @Philous 决策待完善
        if action == "Attack":
            # Choose a target
            target = random.choice(
                self._Heros if owner in self._Monsters else self._Monsters)
            owner.attack(target=target)
