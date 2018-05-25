import json

from ..Error import UncorrectAttrError


class Attr(object):
    """属性对象生成类"""

    def __init__(self, name=None, value=None, attr={}):
        """提供两种形式(提供name&value, 提供字典对象attr)
        
        Keyword Arguments:
            name {str} -- 属性名 (default: {None})
            value {int} -- 属性值 (default: {None})
            attr {dict} -- 属性字典 (default: {{}})
        
        Raises:
            UncorrectAttrError -- 不正确的属性对象输入形式异常
        """

        super(Attr, self).__init__()
        try:
            if name and value:
                self._name = name
                self.update(name=name, value=value)
            elif attr:
                self._name = list(attr.keys())[0]
                self.update(attr=attr)
            else:
                raise UncorrectAttrError("Uncorrect Attribute!")
        except UncorrectAttrError as error:
            print(error.errorinfo)

    def update(self, name=None, value=None, attr={}):
        """更新或者初始化对象的属性
        
        Keyword Arguments:
            name {str} -- 属性名 (default: {None})
            value {int} -- 属性值 (default: {None})
            attr {dict} -- 属性字典 (default: {{}})
        """

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
        """基函数, 判断是修改属性还是更新属性
        
        Keyword Arguments:
            name {str} -- 属性名 (default: {None})
            value {int} -- 属性值 (default: {None})
        """

        try:
            getattr(self, name)
        except AttributeError as error:
            print(error)
        else:
            setattr(self, name, value)

    def output(self):
        """输出属性字典，未赋值则为空
        
        Returns:
            dict -- 属性字典
        """

        try:
            ret = {self._name, getattr(self, self._name)}
        except Exception as error:
            print(error)
        else:
            ret = {}
        finally:
            return ret


class State(object):
    """角色状态基类"""

    def __init__(self, name):
        super(State, self).__init__()
        self._name = name
        self.attrList = set()

    def updateAttrs(self, attrs={}):
        """添加或者更新角色的属性
        
        Keyword Arguments:
            attrs {dict} -- 属性字典 (default: {{}})
        """

        for name in attrs.keys():
            self.attrList.add(name)
            setattr(self, name, attrs[name])

    def outputAttrs(self):
        """输出目前状态的属性字典，未赋值则为空
        
        Returns:
            dict -- 属性字典
        """

        ret = {}
        for name in self.attrList:
            ret[name] = getattr(self, name)
        return ret
