# -*- coding: utf-8 -*-
#
import mod.server.extraServerApi as serverApi
from . import general


class ToolDeltaModServer(serverApi.GetServerSystemCls()):
    def __init__(self, namespace, name):
        super(ToolDeltaModServer, self).__init__(namespace, name)
        general.InitServer(self)

    def Destroy(self):
        general.UninitServer(self)

