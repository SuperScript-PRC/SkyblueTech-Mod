# coding=utf-8

from ..basic import ClientEvent


class ClientBlockUseEvent(ClientEvent):
    name = "ClientBlockUseEvent"

    playerId = '' # type: str
    """ 玩家Id """
    blockName = '' # type: str
    """ 方块的identifier，包含命名空间及名称 """
    aux = 0 # type: int
    """ 方块附加值 """
    x = 0 # type: int
    """ 方块x坐标 """
    y = 0 # type: int
    """ 方块y坐标 """
    z = 0 # type: int
    """ 方块z坐标 """
    clickX = 0.0 # type: float
    """ 点击点的x比例位置 """
    clickY = 0.0 # type: float
    """ 点击点的y比例位置 """
    clickZ = 0.0 # type: float
    """ 点击点的z比例位置 """


    def unmarshal(self, data):
        # type: (dict) -> None
        self._orig = data
        self.playerId = data["playerId"]
        self.blockName = data["blockName"]
        self.aux = data["aux"]
        self.x = data["x"]
        self.y = data["y"]
        self.z = data["z"]
        self.clickX = data["clickX"]
        self.clickY = data["clickY"]
        self.clickZ = data["clickZ"]

    def marshal(self):
        # type: () -> dict
        return {
            "playerId": self.playerId,
            "blockName": self.blockName,
            "aux": self.aux,
            "x": self.x,
            "y": self.y,
            "z": self.z,
            "clickX": self.clickX,
            "clickY": self.clickY,
            "clickZ": self.clickZ,
        }

    def cancel(self):
        """拦截与方块交互的逻辑。"""
        self._orig["cancel"] = True


class ModBlockEntityLoadedClientEvent(ClientEvent):
    name = "ModBlockEntityLoadedClientEvent"

    posX = 0 # type: int
    """ 自定义方块实体的位置X """
    posY = 0 # type: int
    """ 自定义方块实体的位置Y """
    posZ = 0 # type: int
    """ 自定义方块实体的位置Z """
    dimensionId = 0 # type: int
    """ 维度id """
    blockName = '' # type: str
    """ 方块的identifier，包含命名空间及名称 """


    def unmarshal(self, data):
        # type: (dict) -> None
        self.posX = data["posX"]
        self.posY = data["posY"]
        self.posZ = data["posZ"]
        self.dimensionId = data["dimensionId"]
        self.blockName = data["blockName"]

    def marshal(self):
        # type: () -> dict
        return {
            "posX": self.posX,
            "posY": self.posY,
            "posZ": self.posZ,
            "dimensionId": self.dimensionId,
            "blockName": self.blockName,
        }

class ModBlockEntityRemoveClientEvent(ClientEvent):
    name = "ModBlockEntityRemoveClientEvent"

    posX = 0 # type: int
    """ 自定义方块实体的位置X """
    posY = 0 # type: int
    """ 自定义方块实体的位置Y """
    posZ = 0 # type: int
    """ 自定义方块实体的位置Z """
    dimensionId = 0 # type: int
    """ 维度id """
    blockName = '' # type: str
    """ 方块的identifier，包含命名空间及名称 """


    def unmarshal(self, data):
        # type: (dict) -> None
        self.posX = data["posX"]
        self.posY = data["posY"]
        self.posZ = data["posZ"]
        self.dimensionId = data["dimensionId"]
        self.blockName = data["blockName"]

    def marshal(self):
        # type: () -> dict
        return {
            "posX": self.posX,
            "posY": self.posY,
            "posZ": self.posZ,
            "dimensionId": self.dimensionId,
            "blockName": self.blockName,
        }