from ..events.server.ui import CreateUIRequest, ForceRemoveUIRequest
from ..events.client.control import OnKeyPressInGame
from ..client_event_listener import ListenEvent
from ..ui.reg import GetScreen
from .pool import GetActiveScreen, GetActiveScreens, GetActiveProxyScreens

@ListenEvent(CreateUIRequest)
def onCreateUIRequest(event):
    # type: (CreateUIRequest) -> None
    ui = GetScreen(event.ui_key)
    if ui is None:
        raise ValueError("UI not found: " + event.ui_key)
    ui.CreateUI(params={"sync": event.sync_id})

@ListenEvent(ForceRemoveUIRequest)
def onForceRemoveUIRequest(event):
    # type: (ForceRemoveUIRequest) -> None
    uiNode = GetActiveScreen(event.ui_key)
    if uiNode is None:
        return
    uiNode.RemoveUI()

@ListenEvent(OnKeyPressInGame)
def onKeyPressInGame(event):
    # type: (OnKeyPressInGame) -> None
    for ui in GetActiveScreens() + GetActiveProxyScreens():
        ui.OnCurrentPageKeyEvent(event)
