# coding=utf-8
#
from mod.client import extraClientApi as clientApi
from ...internal import ClientComp, ClientLevelId
from ..internal.cacher import MethodCacher


_getMousePosition = MethodCacher(lambda :ClientComp.CreateActorMotion(clientApi.GetLocalPlayerId()).GetMousePosition)

def GetFocusPos():
    mouse_data = _getMousePosition()
    if mouse_data is not None:
        return mouse_data
    else:
        return clientApi.GetTouchPos()

def GetToggleMode():
    """
    返回 0 代表使用鼠标操作, 返回 1 代表使用触摸屏操作
    """
    return ClientComp.CreatePlayerView(clientApi.GetLocalPlayerId()).GetToggleOption(clientApi.GetMinecraftEnum().OptionId.INPUT_MODE)

def GetUIProfile():
    """
    0 表示经典模式, 1 表示携带版模式
    """
    return ClientComp.CreatePlayerView(ClientLevelId).GetUIProfile()
