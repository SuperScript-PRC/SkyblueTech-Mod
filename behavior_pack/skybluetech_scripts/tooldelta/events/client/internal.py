# -*- coding: utf-8 -*-
#
from ..basic import CustomC2SEvent, CustomS2CEvent


class TDRpcCallC2S(CustomC2SEvent):
    name = "td:RpcCallC2S"

    def __init__(self, funcname, args, kwargs):
        self.funcname = funcname
        self.args = args
        self.kwargs = kwargs


    def marshal(self):
        return {"f": self.funcname, "a": self.args, "k": self.kwargs}

    @classmethod
    def unmarshal(cls, data):
        return cls(data["f"], data["a"], data["k"])


class TDRpcCallS2CRet(CustomS2CEvent):
    name = "td:RpcCallS2CRet"

    def __init__(self, ret_value, error):
        self.ret_value = ret_value
        self.error = error

    def marshal(self):
        return {"r": self.ret_value, "e": self.error}

    @classmethod
    def unmarshal(cls, data):
        return cls(data["r"], data["e"])
