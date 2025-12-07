# -*- coding: utf-8 -*-
#
import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi
from mod.common.mod import Mod
from mod_log import logger
from .internal import setModName, GetModName, GetModServerEngineName, GetModClientEngineName
from .mod_server import ToolDeltaModServer
from .mod_client import ToolDeltaModClient


def RegisterMod():
    def wrapper(cls):
        # type: (type[ToolDeltaMod]) -> type[ToolDeltaMod]
        if cls.name is None:
            raise ValueError("mod name is None")
        setModName(cls.name)
        return Mod.Binding(name=cls.name, version=cls.version_str())(cls) # pyright: ignore[reportOptionalCall]

    return wrapper


class ToolDeltaMod(object):
    name = None # type: str | None
    version = (1, 0, 0) # type: tuple[int, int, int]

    def __init__(self):
        pass

    @Mod.InitServer() # pyright: ignore[reportOptionalCall]
    def initMod(self):
        server_system_name = GetModServerEngineName()
        server_system_path = ToolDeltaModServer.__module__ + "." + ToolDeltaModServer.__name__
        serverApi.RegisterSystem(GetModName(), server_system_name, server_system_path)
        logger.debug("ToolDelta: Mod server inited: " + server_system_name)

    @Mod.InitClient() # pyright: ignore[reportOptionalCall]
    def init(self):
        client_system_name = GetModClientEngineName()
        client_system_path = ToolDeltaModClient.__module__ + "." + ToolDeltaModClient.__name__
        clientApi.RegisterSystem(GetModName(), client_system_name, client_system_path)
        logger.debug("ToolDelta: Mod client inited: " + client_system_name)

    @classmethod
    def version_str(cls):
        return ".".join(map(str, cls.version))
