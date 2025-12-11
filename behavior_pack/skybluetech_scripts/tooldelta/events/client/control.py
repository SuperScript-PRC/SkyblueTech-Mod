# coding=utf-8

from ..basic import ClientEvent

class OnKeyPressInGame(ClientEvent):
    name = "OnKeyPressInGame"

    screenName = '' # type: str
    """ 当前screenName """
    key = '' # type: str
    """ 键码（注：这里的int型被转成了str型，比如"1"对应的就是枚举值文档中的1），详见KeyBoardType枚举 """
    isDown = '' # type: str
    """ 是否按下，按下为1，弹起为0 """

    def unmarshal(self, data):
        # type: (dict) -> None
        self.screenName = data["screenName"]
        self.key = data["key"]
        self.isDown = data["isDown"]

    def marshal(self):
        # type: () -> dict
        return {
            "screenName": self.screenName,
            "key": self.key,
            "isDown": self.isDown,
        }

