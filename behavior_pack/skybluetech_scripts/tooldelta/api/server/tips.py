from ... import ServerComp, ServerLevelId

_setOnePopupMessage = ServerComp.CreateGame(ServerLevelId).SetOnePopupNotice
_setOneTipMessage = ServerComp.CreateGame(ServerLevelId).SetOneTipMessage
NotifyOneMessage = ServerComp.CreateMsg(ServerLevelId).NotifyOneMessage

def SetOnePopupNotice(playerId, message, subtitle="§6提示§f"):
    # type: (str, str, str) -> None
    _setOnePopupMessage(playerId, message, subtitle)

def SetOneTipMessage(playerId, message):
    # type: (str, str) -> None
    _setOneTipMessage(playerId, message)


__all__ = [
    "SetOnePopupNotice",
    "SetOneTipMessage",
]
