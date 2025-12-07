# -*- coding: utf-8 -*-
from ...define.item import Item
from ...internal import ClientComp, ClientLevelId
from ..internal.cacher import MethodCacher

_addDropItemToWorld = MethodCacher(lambda :ClientComp.CreateItem(ClientLevelId).AddDropItemToWorld)
_setDropItemTransform = MethodCacher(lambda :ClientComp.CreateItem(ClientLevelId).SetDropItemTransform)
_deleteClientDropItemEntity = MethodCacher(lambda :ClientComp.CreateItem(ClientLevelId).DeleteClientDropItemEntity)

def CreateDropItemModelEntity(dim, xyz, item, bob_speed=0, spin_speed=0):
    # type: (int, tuple[float, float, float], Item, float, float) -> str
    return _addDropItemToWorld(item.marshal(), dim, xyz, bob_speed, spin_speed)

SetDropItemTransform = _setDropItemTransform
DeleteClientDropItemEntity = _deleteClientDropItemEntity