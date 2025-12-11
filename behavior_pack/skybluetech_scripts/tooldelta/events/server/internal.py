# coding=utf-8
#
from ..basic import CustomS2CEvent, CustomC2SEvent


class TDRpcCallS2C(CustomS2CEvent):
    name = "td:RpcCallS2C"

    def __init__(self, funcname, args, kwargs):
        self.funcname = funcname
        self.args = args
        self.kwargs = kwargs


    def marshal(self):
        return {"f": self.funcname, "a": self.args, "k": self.kwargs}

    @classmethod
    def unmarshal(cls, data):
        return cls(data["f"], data["a"], data["k"])


class TDRpcCallC2SRet(CustomC2SEvent):
    name = "td:RpcCallC2SRet"

    def __init__(self, ret_value, error):
        self.ret_value = ret_value
        self.error = error

    def marshal(self):
        return {"r": self.ret_value, "e": self.error}

    @classmethod
    def unmarshal(cls, data):
        return cls(data["r"], data["e"])

