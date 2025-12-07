# -*- coding: utf-8 -*-

from ...define.item import Item
from ..basic import ServerEvent

class PlayerAttackEntityEvent(ServerEvent):
    name = "PlayerAttackEntityEvent"

    playerId = '' # type: str
    """ 玩家id """
    victimId = '' # type: str
    """ 受击者id """
    damage = 0.0 # type: float
    """ 伤害值：引擎传过来的值是0 允许脚本层修改为其他数 """
    isValid = 0 # type: int
    """ 脚本是否设置伤害值：1表示是；0 表示否 """
    isKnockBack = False # type: bool
    """ 是否支持击退效果，默认支持，当不支持时将屏蔽武器击退附魔效果 """
    isCrit = False # type: bool
    """ 本次攻击是否产生暴击,不支持修改 """


    def unmarshal(self, data):
        # type: (dict) -> None
        self._orig = data
        self.playerId = data["playerId"]
        self.victimId = data["victimId"]
        self.damage = data["damage"]
        self.isValid = data["isValid"]
        self.isKnockBack = data["isKnockBack"]
        self.isCrit = data["isCrit"]

    def marshal(self):
        # type: () -> dict
        return {
            "playerId": self.playerId,
            "victimId": self.victimId,
            "damage": self.damage,
            "isValid": self.isValid,
            "isKnockBack": self.isKnockBack,
            "isCrit": self.isCrit,
        }

    def cancel(self):
        # type: () -> None
        "取消该次攻击"
        self._orig["cancel"] = True


