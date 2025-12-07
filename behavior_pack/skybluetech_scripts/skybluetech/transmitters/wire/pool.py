# -*- coding: utf-8 -*-
#
from weakref import WeakValueDictionary as WValueDict
from skybluetech_scripts.tooldelta.no_runtime_typing import TYPE_CHECKING

# TYPE_CHECKING
if TYPE_CHECKING:
    from .define import WireNetwork
    PosData = tuple[int, int, int, int, int]
# TYPE_CHECKING END

# TODO: 我的山头: 需要 GC?
pool = WValueDict() # type: WValueDict[int, WireNetwork]

def GetSameNetwork(network):
    # type: (WireNetwork) -> WireNetwork
    network_hash = hash(network)
    if network_hash in pool:
        return pool[network_hash]
    else:
        pool[network_hash] = network
        return network


# 用于标记已找出的网络。
# 防止机器初始化时重复计算网络。
# TODO: 我的山头: 需要 GC?
cNetworkPool = {} # type: dict[PosData, WireNetwork]

def GetCachedNetworkFromPos(posdata):
    # type: (PosData) -> WireNetwork | None
    return cNetworkPool.get(posdata)

def SetNetworkToPos(posdata, network):
    # type: (PosData, WireNetwork | None) -> None
    if network is not None:
        cNetworkPool[posdata] = network
    else:
        cNetworkPool.pop(posdata, None)
