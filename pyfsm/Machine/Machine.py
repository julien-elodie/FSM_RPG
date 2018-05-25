import functools


class Machine(object):
    """对象生成基础类"""

    def __init__(self, name):
        super(Machine, self).__init__()
        self._name = name

    def start(self, initState):
        """设定初始状态
        
        Arguments:
            initState {State} -- 初始状态
        """

        self._state = initState

    def updateState(self, state):
        """更新状态
        
        Arguments:
            state {State} -- 待更新的状态
        """

        self._state = state

    @classmethod
    def updateAction(cls, func):
        """通过添加类成员函数来实现同一角色的技能学习以及不同角色的不同技能的兼容
        
        Arguments:
            func {function} -- 技能函数
        """

        @functools.wraps(func)
        def dummy(*args, **kwargs):
            func(*args, **kwargs)
        setattr(cls, func.__name__, dummy)
