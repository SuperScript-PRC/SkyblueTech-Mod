# -*- coding: utf-8 -*-
#

from weakref import WeakValueDictionary
from ..no_runtime_typing import TYPE_CHECKING

# TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Callable, ParamSpec, TypeVar
    PT = ParamSpec("PT")
    RT = TypeVar("RT")
# TYPE_CHECKING END

def _generate_lock_name(func):
    # type: (Callable) -> str
    return func.__module__ + "." + func.__name__


GLockPool = WeakValueDictionary()


class LockedFuncRefObj:
    pass

def UniqueLock(debug=False):
    # type: (int) -> Callable[[Callable[PT, RT]], Callable[PT, RT | None]]
    """
    确保同一时间内至多只有 1 个该方法可以运行。
    如果已有, 则返回 None。
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            uname = _generate_lock_name(func)
            if uname not in GLockPool:
                GLockPool[uname] = LockedFuncRefObj() # just for ref
                return func(*args, **kwargs)
            else:
                if debug: # pragma: no cover
                    print("[LockedFunc]", uname, "already locked")
                return None
        wrapper.__name__ = func.__name__
        return wrapper
    return decorator

__all__ = [
    "UniqueLock",
]