from ..internal import GetClient, GetServer
from .basic import CustomC2SEvent, CustomS2CEvent

def NotifyToServer(event):
    # type: (CustomC2SEvent) -> None
    GetClient().NotifyToServer(event.name, event.marshal())

def NotifyToClient(targetId, event):
    # type: (str, CustomS2CEvent) -> None
    GetServer().NotifyToClient(targetId, event.name, event.marshal())

def NotifyToClients(targetIds, event):
    # type: (list[str], CustomS2CEvent) -> None
    GetServer().NotifyToMultiClients(targetIds, event.name, event.marshal())

def NotifyToAll(event):
    # type: (CustomS2CEvent) -> None
    from mod.server import extraServerApi as serverApi
    GetServer().NotifyToMultiClients(serverApi.GetPlayerList(), event.name, event.marshal())