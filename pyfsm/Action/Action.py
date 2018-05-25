import functools

from ..Helper import Logger


class Action(object):
    """docstring for Action."""

    def __init__(self, name):
        super(Action, self).__init__()
        self._name = name

    # decorator
    def __call__(self, func):
        @Logger()
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("[" + self._name + "]", end=' ')
            func(*args, **kwargs)
        return wrapper
