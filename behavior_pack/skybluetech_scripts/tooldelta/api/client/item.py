# -*- coding: utf-8 -*-
#
from ...internal import ClientComp, ClientLevelId

def GetItemHoverName(itemName):
    # type: (str) -> str
    return ClientComp.CreateItem(ClientLevelId).GetItemHoverName(itemName)


__all__ = [
    'GetItemHoverName',
]
