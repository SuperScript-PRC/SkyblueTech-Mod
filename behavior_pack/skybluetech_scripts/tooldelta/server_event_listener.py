# -*- coding: utf-8 -*-
#
import mod.server.extraServerApi as serverApi
from .general import ServerInitCallback, ServerUninitCallback
from .no_runtime_typing import TYPE_CHECKING
from .internal import GetServer, GetModName, GetModClientEngineName
from .events.basic import ServerEvent, CustomC2SEvent

# TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Any, Callable, TypeVar
    EventT = TypeVar('EventT', bound=ServerEvent)
# TYPE_CHECKING END


listeners = set()  # type: set[tuple[type[ServerEvent], str, Callable[[Any], None], int]]


def AddEventListener(event, listener, priority=0):
    # type: (type[EventT], Callable[[EventT], None], int) -> None
    """
    监听服务端事件。

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
    监听服务端事件, 作为装饰器使用。

    Args:
        event (type[Event]): 事件类
    """
    def wrapper(func):
        # type: (Callable[[EventT], None]) -> Callable[[EventT], None]
        AddEventListener(event, func, priority)
        return func

    return wrapper

@ServerInitCallback(-10000)
def OnServerListen():
    # type: () -> None
    """
    需要在 server class 的 ListenEvent 方法下调用 onServerListen()
    """
    server = GetServer()
    for event, listener_orig_name, listener, priority in listeners:
        setattr(server, listener_orig_name, listener)
        if issubclass(event, CustomC2SEvent):
            server.ListenForEvent(
                GetModName(),
                GetModClientEngineName(),
                event.name, server,
                listener, # pyright: ignore[reportArgumentType]
                priority
            )
        else:
            server.ListenForEvent(
                serverApi.GetEngineNamespace(),
                serverApi.GetEngineSystemName(),
                event.name, server,
                listener, # pyright: ignore[reportArgumentType]
                priority
            )

@ServerUninitCallback(-10000)
def OnServerUnlisten():
    # type: () -> None
    """
    需要在 server class 的 ListenEvent 方法下调用 onServerUnlisten()
    """
    server = GetServer()
    for event, _, listener, priority in listeners:
        if issubclass(event, CustomC2SEvent):
            server.UnListenForEvent(
                GetModName(),
                GetModClientEngineName(),
                event.name, server,
                listener, # pyright: ignore[reportArgumentType]
                priority
            )
        else:
            server.UnListenForEvent(
                serverApi.GetEngineNamespace(),
                serverApi.GetEngineSystemName(),
                event.name, server,
                listener, # pyright: ignore[reportArgumentType]
                priority
            )
