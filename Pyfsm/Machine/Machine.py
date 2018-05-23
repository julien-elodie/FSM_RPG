import functools
import sys


class Machine(object):
    """docstring for Machine."""

    def __init__(self, name):
        super(Machine, self).__init__()
        self._name = name

    def start(self, initState):
        self._state = initState

    def updateState(self, state):
        self._state = state

    @classmethod
    def updateAction(cls, func):
        @functools.wraps(func)
        def dummy(*args, **kwargs):
            func(*args, **kwargs)
        setattr(cls, func.__name__, dummy)
