# -*- coding: utf-8 -*-
#
import mod.client.extraClientApi as clientApi
from .general import ClientInitCallback, ClientUninitCallback
from .no_runtime_typing import TYPE_CHECKING
from .internal import GetModName, GetModServerEngineName

# TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Any, TYPE_CHECKING, Callable, TypeVar
    EventT = TypeVar("EventT", bound="ClientEvent")
    T = TypeVar("T")
# TYPE_CHECKING END

from .internal import GetClient
from .events.basic import ClientEvent, CustomS2CEvent

listeners = set()  # type: set[tuple[type[ClientEvent], str, Callable[[Any], None], int]]


def AddEventListener(event, listener, priority=0):
    # type: (type[EventT], Callable[[EventT], None], int) -> None
    """
    监听客户端事件。

    Args:
        event (type[Event]): 事件类
        listener ((T) -> None): 事件监听器
    """
    def custom_listener(data):
        evt = event()
        evt.unmarshal(data)
        listener(evt)

    funcname = listener.__module__ + "." + listener.__name__ # to avoid name conflict
    custom_listener.__name__ = funcname
    listeners.add((event, funcname, custom_listener, priority))

def ListenEvent(event, priority=0):
    # type: (type[EventT], int) -> Callable[[Callable[[EventT], None]], Callable[[EventT], None]]
    """
    监听客户端事件, 作为装饰器使用。

    Args:
        event (type[Event]): 事件类
    """
    def wrapper(func):
        # type: (Callable[[EventT], None]) -> Callable[[EventT], None]
        AddEventListener(event, func, priority)
        return func

    return wrapper

@ClientInitCallback(-10000)
def OnClientListen():
    # type: () -> None
    client = GetClient()
    for event, listener_orig_name, listener, priority in listeners:
        setattr(client, listener_orig_name, listener)
        if issubclass(event, CustomS2CEvent):
            client.ListenForEvent(
                GetModName(),
                GetModServerEngineName(),
                event.name, client, listener, # pyright: ignore[reportArgumentType]
                priority
            )
        else:
            client.ListenForEvent(
                clientApi.GetEngineNamespace(),
                clientApi.GetEngineSystemName(),
                event.name, client, listener, # pyright: ignore[reportArgumentType]
                priority
            )

@ClientUninitCallback(-10000)
def OnClientUnlisten():
    # type: () -> None
    client = GetClient()
    for event, _, listener, priority in listeners:
        if issubclass(event, CustomS2CEvent):
            client.UnListenForEvent(
                GetModName(),
                GetModServerEngineName(),
                event.name, client,
                listener, # pyright: ignore[reportArgumentType]
                priority
            )
        else:
            client.UnListenForEvent(
                clientApi.GetEngineNamespace(),
                clientApi.GetEngineSystemName(),
                event.name, client,
                listener, # pyright: ignore[reportArgumentType]
                priority
            )

