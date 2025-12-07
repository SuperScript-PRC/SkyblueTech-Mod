# -*- coding: utf-8 -*-

from ...define.item import Item
from ...internal import ServerComp, ServerLevelId
from ..basic import ServerEvent


class PlayerTryPutCustomContainerItemServerEvent(ServerEvent):
    name = "PlayerTryPutCustomContainerItemServerEvent"

    item = Item("") # type: Item
    """ 尝试放入物品的物品信息字典 """
    collectionName = '' # type: str
    """ 放入容器名称，对应容器json中"custom_description"字段 """
    collectionType = '' # type: str
    """ 放入容器类型，目前仅支持netease_container和netease_ui_container """
    collectionIndex = 0 # type: int
    """ 放入容器索引 """
    playerId = '' # type: str
    """ 玩家id """
    x = 0 # type: int
    """ 容器方块x坐标 """
    y = 0 # type: int
    """ 容器方块y坐标 """
    z = 0 # type: int
    """ 容器方块z坐标 """


    def unmarshal(self, data):
        # type: (dict) -> None
        self._orig = data
        self.item = Item.from_dict(data["itemDict"])
        self.collectionName = data["collectionName"]
        self.collectionType = data["collectionType"]
        self.collectionIndex = data["collectionIndex"]
        self.playerId = data["playerId"]
        self.x = data["x"]
        self.y = data["y"]
        self.z = data["z"]

    def marshal(self):
        # type: () -> dict
        return {
            "itemDict": self.item.marshal(),
            "collectionName": self.collectionName,
            "collectionType": self.collectionType,
            "collectionIndex": self.collectionIndex,
            "playerId": self.playerId,
            "x": self.x,
            "y": self.y,
            "z": self.z,
        }

    def cancel(self):
        """ 拒绝此次放入自定义容器的操作 """
        # type: () -> None
        self._orig["cancel"] = True

    @classmethod
    def ListenWithUserData(cls, priority=0):
        # print("[TDEvent] Listen with user data: " + cls.name)
        ServerComp.CreateItem(ServerLevelId).GetUserDataInEvent(cls.name)
        return cls.Listen(priority)


class PlayerTryRemoveCustomContainerItemServerEvent(ServerEvent):
    name = "PlayerTryRemoveCustomContainerItemServerEvent"

    item = Item("") # type: Item
    """ 尝试拿出物品的物品信息字典 """
    collectionName = '' # type: str
    """ 拿出容器名称，对应容器json中"custom_description"字段 """
    collectionType = '' # type: str
    """ 拿出容器类型，目前仅支持netease_container和netease_ui_container """
    collectionIndex = 0 # type: int
    """ 拿出容器索引 """
    playerId = '' # type: str
    """ 玩家id """
    x = 0 # type: int
    """ 容器方块x坐标 """
    y = 0 # type: int
    """ 容器方块y坐标 """
    z = 0 # type: int
    """ 容器方块z坐标 """


    def unmarshal(self, data):
        # type: (dict) -> None
        self._orig = data
        self.item = Item.from_dict(data["itemDict"])
        self.collectionName = data["collectionName"]
        self.collectionType = data["collectionType"]
        self.collectionIndex = data["collectionIndex"]
        self.playerId = data["playerId"]
        self.x = data["x"]
        self.y = data["y"]
        self.z = data["z"]

    def marshal(self):
        # type: () -> dict
        return {
            "itemDict": self.item.marshal(),
            "collectionName": self.collectionName,
            "collectionType": self.collectionType,
            "collectionIndex": self.collectionIndex,
            "playerId": self.playerId,
            "x": self.x,
            "y": self.y,
            "z": self.z,
        }

    def cancel(self):
        """ 拒绝此次拿出 自定义容器的操作 """
        # type: () -> None
        self._orig["cancel"] = True


class ContainerItemChangedServerEvent(ServerEvent):
    name = "ContainerItemChangedServerEvent"

    pos = None # type: tuple[int,int,int] | None
    """ 容器坐标 """
    containerType = 0 # type: int
    """ 容器类型，类型含义见：容器类型枚举 """
    slot = 0 # type: int
    """ 容器槽位 """
    dimensionId = 0 # type: int
    """ 维度id """
    oldItem = Item("")
    """ 旧物品 """
    newItem = Item("")
    """ 新物品 """


    def unmarshal(self, data):
        # type: (dict) -> None
        self.pos = data["pos"]
        self.containerType = data["containerType"]
        self.slot = data["slot"]
        self.dimensionId = data["dimensionId"]
        self.oldItem = Item.from_dict(data["oldItemDict"])
        self.newItem = Item.from_dict(data["newItemDict"])

    def marshal(self):
        # type: () -> dict
        return {
            "pos": self.pos,
            "containerType": self.containerType,
            "slot": self.slot,
            "dimensionId": self.dimensionId,
            "oldItemDict": self.oldItem.marshal(),
            "newItemDict": self.newItem.marshal(),
        }

    @classmethod
    def ListenWithUserData(cls, priority=0):
        # print("[TDEvent] Listen with user data: " + cls.name)
        ServerComp.CreateItem(ServerLevelId).GetUserDataInEvent(cls.name)
        return cls.Listen(priority)


class ItemPushInCustomContainerServerEvent(ServerEvent):
    name = "ItemPushInCustomContainerServerEvent"

    item = Item("")
    """ 漏斗漏入物品的物品信息字典 """
    collectionName = '' # type: str
    """ 目标容器名称，目前仅支持netease_container """
    collectionIndex = 0 # type: int
    """ 目标容器索引 """
    x = 0 # type: int
    """ 容器方块x坐标 """
    y = 0 # type: int
    """ 容器方块y坐标 """
    z = 0 # type: int
    """ 容器方块z坐标 """


    def unmarshal(self, data):
        # type: (dict) -> None
        self._orig = data
        self.item = Item.from_dict(data["itemDict"])
        self.collectionName = data["collectionName"]
        self.collectionIndex = data["collectionIndex"]
        self.x = data["x"]
        self.y = data["y"]
        self.z = data["z"]

    def marshal(self):
        # type: () -> dict
        return {
            "itemDict": self.item.marshal(),
            "collectionName": self.collectionName,
            "collectionIndex": self.collectionIndex,
            "x": self.x,
            "y": self.y,
            "z": self.z,
        }

    def cancel(self):
        """ 取消漏入物品操作 """
        # type: () -> None
        self._orig["cancel"] = True


class ItemPullOutCustomContainerServerEvent(ServerEvent):
    name = "ItemPullOutCustomContainerServerEvent"

    item = Item("")
    """ 漏斗漏出物品的物品信息 """
    collectionName = '' # type: str
    """ 漏出物品的容器名称，目前仅支持netease_container """
    collectionIndex = 0 # type: int
    """ 漏出物品的容器索引 """
    x = 0 # type: int
    """ 容器方块x坐标 """
    y = 0 # type: int
    """ 容器方块y坐标 """
    z = 0 # type: int
    """ 容器方块z坐标 """


    def unmarshal(self, data):
        # type: (dict) -> None
        self._orig = data
        self.item = Item.from_dict(data["itemDict"])
        self.collectionName = data["collectionName"]
        self.collectionIndex = data["collectionIndex"]
        self.x = data["x"]
        self.y = data["y"]
        self.z = data["z"]
        self.cancel = data["cancel"]

    def marshal(self):
        # type: () -> dict
        return {
            "itemDict": self.item.marshal(),
            "collectionName": self.collectionName,
            "collectionIndex": self.collectionIndex,
            "x": self.x,
            "y": self.y,
            "z": self.z,
            "cancel": self.cancel,
        }

    def cancel(self):
        """ 取消漏入物品操作 """
        # type: () -> None
        self._orig["cancel"] = True


class ServerItemUseOnEvent(ServerEvent):
    name = "ServerItemUseOnEvent"
    
    entityId = '' # type: str
    """ 玩家实体id """
    item = Item("") # type: Item
    """ 使用的物品的物品信息字典 """
    x = 0 # type: int
    """ 方块 x 坐标值 """
    y = 0 # type: int
    """ 方块 y 坐标值 """
    z = 0 # type: int
    """ 方块 z 坐标值 """
    blockName = '' # type: str
    """ 方块的identifier """
    blockAuxValue = 0 # type: int
    """ 方块的附加值 """
    face = 0 # type: int
    """ 点击方块的面，参考Facing枚举 """
    dimensionId = 0 # type: int
    """ 维度id """
    clickX = 0.0 # type: float
    """ 点击点的x比例位置 """
    clickY = 0.0 # type: float
    """ 点击点的y比例位置 """
    clickZ = 0.0 # type: float
    """ 点击点的z比例位置 """


    def unmarshal(self, data):
        # type: (dict) -> None
        self._orig = data
        self.entityId = data["entityId"]
        self.item = Item.from_dict(data["itemDict"])
        self.x = data["x"]
        self.y = data["y"]
        self.z = data["z"]
        self.blockName = data["blockName"]
        self.blockAuxValue = data["blockAuxValue"]
        self.face = data["face"]
        self.dimensionId = data["dimensionId"]
        self.clickX = data["clickX"]
        self.clickY = data["clickY"]
        self.clickZ = data["clickZ"]

    def marshal(self):
        # type: () -> dict
        return {
            "entityId": self.entityId,
            "itemDict": self.item.marshal(),
            "x": self.x,
            "y": self.y,
            "z": self.z,
            "blockName": self.blockName,
            "blockAuxValue": self.blockAuxValue,
            "face": self.face,
            "dimensionId": self.dimensionId,
            "clickX": self.clickX,
            "clickY": self.clickY,
            "clickZ": self.clickZ,
            "ret": self._orig["ret"],
        }

    def cancel(self):
        """ 取消使用方块 """
        # type: () -> None
        self._orig["ret"] = True

    @classmethod
    def ListenWithUserData(cls, priority=0):
        # print("[TDEvent] Listen with user data: " + cls.name)
        ServerComp.CreateItem(ServerLevelId).GetUserDataInEvent(cls.name)
        return cls.Listen(priority)


class ActorAcquiredItemServerEvent(ServerEvent):
    name = "ActorAcquiredItemServerEvent"

    actor = '' # type: str
    """ 获得物品玩家实体id """
    secondaryActor = '' # type: str
    """ 物品给予者玩家实体id，如果不存在给予者的话，这里为空字符串 """
    item = Item("") # type: Item
    """ 获得的物品的物品信息字典 """
    acquireMethod = 0 # type: int
    """ 获得物品的方法，详见ItemAcquisitionMethod枚举 """

    def unmarshal(self, data):
        # type: (dict) -> None
        self.actor = data["actor"]
        self.secondaryActor = data["secondaryActor"]
        self.item = Item.from_dict(data["itemDict"])
        self.acquireMethod = data["acquireMethod"]

    def marshal(self):
        # type: () -> dict
        return {
            "actor": self.actor,
            "secondaryActor": self.secondaryActor,
            "itemDict": self.item.marshal(),
            "acquireMethod": self.acquireMethod,
        }


class OnCarriedNewItemChangedServerEvent(ServerEvent):
    name = "OnCarriedNewItemChangedServerEvent"

    oldItem = None # type: Item | None
    """ 旧物品的物品信息字典，当旧物品为空时，此项属性为None """
    newItem = None # type: Item | None
    """ 新物品的物品信息字典，当新物品为空时，此项属性为None """
    playerId = '' # type: str
    """ 玩家 entityId """

    def unmarshal(self, data):
        # type: (dict) -> None
        self.oldItem = Item.from_dict(data["oldItemDict"]) if data["oldItemDict"] else None
        self.newItem = Item.from_dict(data["newItemDict"]) if data["newItemDict"] else None
        self.playerId = data["playerId"]

    def marshal(self):
        # type: () -> dict
        return {
            "oldItemDict": self.oldItem.marshal() if self.oldItem else None,
            "newItemDict": self.newItem.marshal() if self.newItem else None,
            "playerId": self.playerId,
        }


class ItemDurabilityChangedServerEvent(ServerEvent):
    name = "ItemDurabilityChangedServerEvent"

    entityId = '' # type: str
    """ 物品拥有者的实体id """
    item = Item("") # type: Item
    """ 物品的物品信息字典 """
    durabilityBefore = 0 # type: int
    """ 变化前耐久度 """
    durability = 0 # type: int
    """ 变化后耐久度,支持修改。但是请注意修改范围，支持范围为[-32768,32767) """
    canChange = False # type: bool
    """ 是否支持修改，为true时支持通过durability修改，为false时不支持 """

    def unmarshal(self, data):
        # type: (dict) -> None
        self._orig = data
        self.entityId = data["entityId"]
        self.item = Item.from_dict(data["itemDict"])
        self.durabilityBefore = data["durabilityBefore"]
        self.durability = data["durability"]
        self.canChange = data["canChange"]

    def marshal(self):
        # type: () -> dict
        return {
            "entityId": self.entityId,
            "itemDict": self.item.marshal(),
            "durabilityBefore": self.durabilityBefore,
            "durability": self.durability,
            "canChange": self.canChange,
        }

    def ModifyDurability(self, durability):
        # type: (int) -> None
        self.durability = self._orig["durability"] = durability

    @classmethod
    def ListenWithUserData(cls, priority=0):
        # print("[TDEvent] Listen with user data: " + cls.name)
        ServerComp.CreateItem(ServerLevelId).GetUserDataInEvent(cls.name)
        return cls.Listen(priority)


class ServerItemTryUseEvent(ServerEvent):
    name = "ServerItemTryUseEvent"

    playerId = '' # type: str
    """ 玩家id """
    item = Item("") # type: Item
    """ 使用的物品的物品信息字典 """

    def unmarshal(self, data):
        # type: (dict) -> None
        self._orig = data
        self.playerId = data["playerId"]
        self.item = Item.from_dict(data["itemDict"])

    def marshal(self):
        # type: () -> dict
        return {
            "playerId": self.playerId,
            "itemDict": self.item.marshal(),
            "cancel": self.cancel,
        }

    def cancel(self):
        """ 取消使用物品 """
        # type: () -> None
        self._orig["cancel"] = True

    @classmethod
    def ListenWithUserData(cls, priority=0):
        # print("[TDEvent] Listen with user data: " + cls.name)
        ServerComp.CreateItem(ServerLevelId).GetUserDataInEvent(cls.name)
        return cls.Listen(priority)


class CraftItemOutputChangeServerEvent(ServerEvent):
    name = "CraftItemOutputChangeServerEvent"

    playerId = "" # type: str
    """ 玩家实体id """
    item = Item("") # type: Item
    """ 生成的物品 """
    screenContainerType = 0 # type: int
    """ 当前界面类型, 类型含义见：容器类型枚举 """

    def unmarshal(self, data):
        # type: (dict) -> None
        self._orig = data
        self.playerId = data["playerId"]
        self.item = Item.from_dict(data["itemDict"])
        self.screenContainerType = data["screenContainerType"]

    def marshal(self):
        # type: () -> dict
        return {
            "playerId": self.playerId,
            "itemDict": self.item.marshal(),
            "screenContainerType": self.screenContainerType,
        }

    def cancel(self):
        # type: () -> None
        "取消生成物品"
        self._orig["cancel"] = True


class UIContainerItemChangedServerEvent(ServerEvent):
    name = "UIContainerItemChangedServerEvent"

    playerId = "" # type: str
    """ 玩家实体id """
    slot = 0 # type: int
    """ 容器槽位，含义见：容器类型枚举 """
    oldItem = Item("") # type: Item
    """ 旧物品，格式参考物品信息字典 """
    newItem = Item("") # type: Item
    """ 生成的物品，格式参考物品信息字典 """

    def unmarshal(self, data):
        # type: (dict) -> None
        self.playerId = data["playerId"]
        self.slot = data["slot"]
        self.oldItem = Item.from_dict(data["oldItemDict"])
        self.newItem = Item.from_dict(data["newItemDict"])

    def marshal(self):
        # type: () -> dict
        return {
            "playerId": self.playerId,
            "slot": self.slot,
            "oldItemDict": self.oldItem.marshal(),
            "newItemDict": self.newItem.marshal(),
        }

