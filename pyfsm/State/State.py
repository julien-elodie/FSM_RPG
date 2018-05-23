import json

from ..Error import UncorrectAttrError


class Attr(object):
    """docstring for Attr."""

    def __init__(self, name=None, value=None, attr={}):
        super(Attr, self).__init__()
        try:
            if name and value:
                self._name = name
                self.update(name=name, value=value)
            elif attr:
                self._name = list(attr.keys())[0]
                self.update(attr=attr)
            else:
                raise UncorrectAttrError("UncorrectAttribute!")
        except UncorrectAttrError as error:
            print(error.errorinfo)

    def update(self, name=None, value=None, attr={}):
        try:
            if name and value:
                self._update(name, value)
            elif value:
                self._update(self._name, value)
            elif attr:
                self._update(self._name, attr[self._name])
        except Exception as error:
            print(error)

    def _update(self, name=None, value=None):
        try:
            getattr(self, name)
        except AttributeError as error:
            print(error)
        else:
            setattr(self, name, value)

    def output(self):
        try:
            ret = {self._name, getattr(self, self._name)}
        except Exception as error:
            print(error)
        else:
            ret = {}
        finally:
            return ret


class State(object):
    """docstring for State."""

    def __init__(self, name):
        super(State, self).__init__()
        self._name = name
        self.attrList = set()

    def updateAttrs(self, attrs={}):
        for name in attrs.keys():
            self.attrList.add(name)
            setattr(self, name, attrs[name])

    def outputAttrs(self):
        ret = {}
        for name in self.attrList:
            ret[name] = getattr(self, name)
        return ret
