import datetime
import functools
import json
import math
import random
import sys
import time


def modifyPrint(value=[], end='\n'):
    """通过字符串列表生成输出流并实时打印在屏幕上
    
    Keyword Arguments:
        value {list} -- 字符串列表 (default: {[]})
        end {str} -- 结尾符 (default: {'\n'})
    """

    print(' '.join(value), end=end)
    # 刷新缓冲区
    sys.stdout.flush()


def levelupRequiredExp(level):
    """查询升级所需的经验,提供映射表
    TODO @Philous: 优化
    
    Arguments:
        level {int} -- 人物等级
    
    Returns:
        int -- 升级所需的经验
    """

    switcher = {
        "1": 0,
        "2": 300,
        "3": 900,
        "4": 2700,
        "5": 6500,
        "6": 14000,
        "7": 23000,
        "8": 34000,
        "9": 48000,
        "10": 64000,
        "11": 85000,
        "12": 100000,
        "13": 120000,
        "14": 140000,
        "15": 165000,
        "16": 195000,
        "17": 225000,
        "18": 265000,
        "19": 305000,
        "20": 355000
    }
    return switcher.get(str(level), "Error Level!")


def castDice(mode=None):
    """模拟投骰子，提供多种类型及内嵌修正值
    
    Keyword Arguments:
        mode {str} -- 骰子类型,大小写不敏感,例如1d6(1D6) (default: {None})
    
    Returns:
        int -- 投掷结果
    """

    mode, shift = (mode + "+0").split("+")[:2]
    # 大小写不敏感
    times, dice = mode.lower().split("d")
    ret = []
    # judge dice
    if dice in ["4", "6", "10", "8", "12", "20"]:
        # cast dice
        for _ in range(int(times)):
            ret.append(random.randint(1, int(dice)))
        return sum(ret) + int(shift)
    elif [times, dice, shift] == ["1", "2", "0"]: # 1d2
        for _ in range(int(times)):
            ret.append(random.randint(1, 6) % 2)
        return sum(ret) + int(shift)
    elif [times, dice, shift] == ["1", "3", "0"]: # 1d3
        for _ in range(int(times)):
            ret.append(math.ceil(random.randint(1, 6) / 2))
        return sum(ret) + int(shift)
    elif [times, dice, shift] == ["1", "100", "0"]: # 1d100
        # special: 1d100
        for _ in range(2):
            ret.append(random.randint(1, 10))
        return ret[0] * 10 + ret[1]
    else:
        return "Error dice!"


def abilityChecks(ability, value):
    """进行属性鉴定
    
    Arguments:
        ability {str} -- 属性名
        value {int} -- 属性值
    
    Returns:
        int -- 判定结果(加修正值)
    """

    if ability in ["Str", "Dex", "Con", "Int", "Wis", "Cha"]:
        return castDice(mode="1d20") + abilityModifiers(value=value)


def abilityModifiers(value):
    """计算属性调整值
    
    Arguments:
        value {int} -- 属性值
    
    Returns:
        int -- 属性调整值
    """

    return math.floor((value - 10) / 2)

def proficiencyBonus(value):
    """计算熟练加值
    
    Arguments:
        value {int} -- 人物等级
    
    Returns:
        int -- 熟练加值
    """

    return math.ceil(value / 4) + 1


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
    """消息类"""

    def __init__(self, msg=None):
        super(Logger, self).__init__()
        self._msg = msg + '\n' if msg else ''

    def __call__(self, func):
        """decorator
        
        Arguments:
            func {function} -- 被装饰器渲染的函数
        
        Returns:
            function -- 渲染后的函数
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            self.timestamp(end=self._msg)
            func(*args, **kwargs)
        return wrapper

    @classmethod
    def timestamp(cls, end=''):
        """类方法，添加时间戳
        
        Keyword Arguments:
            end {str} -- 结尾符 (default: {''})
        """

        time.sleep(abs(random.gauss(3, 1)))
        # show current time
        modifyPrint(
            ["[" + datetime.datetime.now().strftime('%c') + "] "], end=end)
