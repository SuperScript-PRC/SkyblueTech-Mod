# coding=utf-8

def SetLoreAtPos(userdata, pos, lore):
    # type: (dict, int, str) -> None
    userdata["display"]["Lore"][pos]["__value__"] = lore

def GetLorePos(userdata, name):
    # type: (dict, str) -> int
    return userdata.get("lore_pos", {}).get(name, {}).get("__value__", 0)
