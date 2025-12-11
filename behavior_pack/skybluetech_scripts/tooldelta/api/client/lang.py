# coding=utf-8
#

from ...internal import ClientComp, ClientLevelId


def ZHCN(text):
    # type: (str) -> str
    return ClientComp.CreateGame(ClientLevelId).GetChinese(text)