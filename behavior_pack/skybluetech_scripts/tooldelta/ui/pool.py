if 0:
    from .screen_comp import UScreenNode
    from .proxy_screen import UScreenProxy

# Really useful?

active_screens = {} # type: dict[str, UScreenNode]
active_proxy_screens = {} # type: dict[str, UScreenProxy]


def _addActiveScreen(screen):
    # type: (UScreenNode) -> None
    active_screens[screen._key] = screen

def _removeActiveScreen(screen):
    # type: (UScreenNode) -> None
    active_screens.pop(screen._key, None)

def GetActiveScreen(key):
    # type: (str) -> UScreenNode | None
    return active_screens.get(key)

def GetActiveScreens():
    # type: () -> list[UScreenNode]
    return list(active_screens.values())


def _addActiveProxyScreen(proxy):
    # type: (UScreenProxy) -> None
    active_proxy_screens[proxy.screenName] = proxy

def _removeActiveProxyScreen(proxy):
    # type: (UScreenProxy) -> None
    active_proxy_screens.pop(proxy.screenName, None)

def GetActiveProxyScreen(key):
    # type: (str) -> UScreenProxy | None
    return active_proxy_screens.get(key)

def GetActiveProxyScreens():
    # type: () -> list[UScreenProxy]
    return list(active_proxy_screens.values())

__all__ = [
    "GetActiveScreen",
    "GetActiveScreens",
    "GetActiveProxyScreen",
    "GetActiveProxyScreens",
]
