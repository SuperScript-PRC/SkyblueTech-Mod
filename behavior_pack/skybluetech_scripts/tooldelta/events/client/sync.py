# -*- coding: utf-8 -*-

from mod.client import extraClientApi as clientApi
from ...internal import GetClient, GetServer
from ..basic import CustomC2SEvent, CustomS2CEvent


class ClientNewSync(CustomC2SEvent):
    name = "td:ClientNewSync"

    pid = ""

    def __init__(self, sync_name=""):
        self.sync_name = sync_name

    def marshal(self):
        m = GetClient().CreateEventData()
        m["sync_name"] = self.sync_name
        m["pid"] = clientApi.GetLocalPlayerId()
        return m

    def unmarshal(self, data):
        # type: (dict) -> None
        self.sync_name = data["sync_name"]
        self.pid = data["pid"]


class ClientPopSync(CustomC2SEvent):
    name = "td:ClientPopSync"

    pid = ""

    def __init__(self, sync_name=""):
        self.sync_name = sync_name

    def marshal(self):
        m = GetClient().CreateEventData()
        m["sync_name"] = self.sync_name
        m["pid"] = clientApi.GetLocalPlayerId()
        return m

    def unmarshal(self, data):
        # type: (dict) -> None
        self.sync_name = data["sync_name"]
        self.pid = data["pid"]


class ServerDelSync(CustomS2CEvent):
    name = "td:ServerDelSync"

    def __init__(self, sync_name=""):
        self.sync_name = sync_name

    def marshal(self):
        m = GetServer().CreateEventData()
        m["sync_name"] = self.sync_name
        return m

    def unmarshal(self, data):
        # type: (dict) -> None
        self.sync_name = data["sync_name"]


class S2CSyncDatas(CustomS2CEvent):
    name = "td:S2CSyncData"

    def __init__(self, sync_datas=None):
        # type: (list | None) -> None
        self.sync_datas = sync_datas or []

    def marshal(self):
        m = GetServer().CreateEventData()
        m["datas"] = self.sync_datas
        return m

    def unmarshal(self, data):
        # type: (dict) -> None
        self.sync_datas = data["datas"]
