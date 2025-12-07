NBT_BYTE = 1
NBT_SHORT = 2
NBT_INT = 3
NBT_LONG = 4
NBT_FLOAT = 5
NBT_DOUBLE = 6
NBT_BYTE_ARRAY = 7
NBT_STRING = 8
NBT_LIST = 9
NBT_COMPOUND = 10
NBT_INT_ARRAY = 11

def Tp(typ, val):
    return {"__type__": typ, "__value__": val}

def Byte(val):
    # type: (bool) -> dict
    return Tp(NBT_BYTE, val)

def Short(val):
    # type: (int) -> dict
    return Tp(NBT_SHORT, val)

def Int(val):
    # type: (int) -> dict
    return Tp(NBT_INT, val)

def Long(val):
    # type: (int) -> dict
    return Tp(NBT_LONG, val)

def Float(val):
    # type: (float) -> dict
    return Tp(NBT_FLOAT, val)

def Double(val):
    # type: (float) -> dict
    return Tp(NBT_DOUBLE, val)

def ByteArray(val):
    # type: (list) -> dict
    return Tp(NBT_BYTE_ARRAY, val)

def String(val):
    # type: (str) -> dict
    return Tp(NBT_STRING, val)

def List(val):
    # type: (list) -> dict
    """ WARNING: 一些地方可以直接使用 list。 """
    return Tp(NBT_LIST, val)

def Compound(val):
    # type: (dict) -> dict
    """ WARNING: 大部分地方都可以直接使用 dict。 """
    return Tp(NBT_COMPOUND, val)

def IntArray(val):
    # type: (list) -> dict
    return Tp(NBT_INT_ARRAY, val)

def GetValueWithDefault(nbt, key, default):
    return nbt.get(key, {"__value__": default})["__value__"]

