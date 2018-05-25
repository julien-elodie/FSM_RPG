# Attr
class UncorrectAttrError(Exception):
    """不正确的属性对象输入形式异常"""

    def __init__(self, ErrorInfo):
        super(UncorrectAttrError, self).__init__()
        self.errorinfo = ErrorInfo

    def __str__(self):
        return self.errorinfo

# Combat
class EmptyHerosOrMonstersError(Exception):
    """战斗对象中英雄或者怪物为空异常"""

    def __init__(self, ErrorInfo):
        super(EmptyHerosOrMonstersError, self).__init__()
        self.errorinfo = ErrorInfo

    def __str__(self):
        return self.errorinfo