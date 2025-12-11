# coding=utf-8
#
import mod.client.extraClientApi as clientApi
from . import general


class ToolDeltaModClient(clientApi.GetClientSystemCls()):
    def __init__(self, namespace, name):
        super(ToolDeltaModClient, self).__init__(namespace, name)
        general.InitClient(self)

    def Destroy(self):
        general.UninitClient(self)


