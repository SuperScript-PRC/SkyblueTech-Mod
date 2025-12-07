# -*- coding: utf-8 -*-


class SNode(object):
    def __init__(self, base):
        # type: (str) -> None
        self.base = base

    def __truediv__(self, path):
        # type: (str) -> SNode
        return SNode(self.base + "/" + path)

    __div__ = __truediv__

    def __repr__(self):
        return self.base

    def __add__(self, path):
        # type: (str) -> SNode
        return SNode(self.base + path)

    def __hash__(self):
        return hash(self.base)


__all__ = ["SNode"]
