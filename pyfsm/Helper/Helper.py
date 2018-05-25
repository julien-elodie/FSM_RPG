import datetime
import functools
import json
import math
import random
import sys
import time


def modifyPrint(value=[], end='\n'):
    print(' '.join(value), end=end)
    sys.stdout.flush()


def levelupRequiredExp(level):
    # TODO @Philous: 优化
    switcher = {
        "1": 10,
        "2": 20,
        "3": 30,
        "4": 40,
        "5": 50,
        "6": 60,
        "7": 70,
        "8": 80,
        "9": 90,
        "10": 100
    }
    return switcher.get(str(level), "Error Level!")


def castDice(mode=None):
    mode, shift = (mode + "+0").split("+")[:2]
    # 大小写不敏感
    times, dice = mode.lower().split("d")
    ret = []
    # judge dice
    if dice in ["4", "6", "8", "12", "20"]:
        # cast dice
        for _ in range(int(times)):
            ret.append(random.randint(1, int(dice)))
        return sum(ret) + int(shift)
    elif [times, dice, shift] == ["1", "2", "0"]:
        for _ in range(int(times)):
            ret.append(random.randint(1, 6) % 2)
        return sum(ret) + int(shift)
    elif [times, dice, shift] == ["1", "3", "0"]:
        for _ in range(int(times)):
            ret.append(math.ceil(random.randint(1, 6) / 2))
        return sum(ret) + int(shift)
    elif [times, dice, shift] == ["1", "100", "0"]:
        # special: 1d100
        for _ in range(2):
            ret.append(random.randint(1, 10))
        return ret[0] * 10 + ret[1]
    else:
        return "Error dice!"


# 属性鉴定
def abilityChecks(ability, value):
    if ability in ["Str", "Dex", "Con", "Int", "Wis", "Cha"]:
        return castDice(mode="1d20") + abilityModifiers(value=value)


# 属性调整值
def abilityModifiers(value):
    return math.floor((value - 10) / 2)


# 加权随机数
def weightedChoice(weights):
    """加权随机数，输入权重(降序排列调高运行速度)，输出索引
    link:http://www.cnblogs.com/zywscq/p/5469661.html
    
    Arguments:
        weights {list} -- 权重序列
    
    Returns:
        int -- 所选取的值在原序列中的索引
    """

    rnd = random.random() * sum(weights)
    for i, w in enumerate(weights):
        rnd -= w
        if rnd < 0:
            return i


class Logger(object):
    """docstring for Logger."""

    def __init__(self, msg=None):
        super(Logger, self).__init__()
        self._msg = msg + '\n' if msg else ''

    # decorator
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            self.timestamp(end=self._msg)
            func(*args, **kwargs)
        return wrapper

    @classmethod
    def timestamp(cls, end=''):
        time.sleep(abs(random.gauss(3, 1)))
        # show current time
        modifyPrint(
            ["[" + datetime.datetime.now().strftime('%c') + "] "], end=end)
