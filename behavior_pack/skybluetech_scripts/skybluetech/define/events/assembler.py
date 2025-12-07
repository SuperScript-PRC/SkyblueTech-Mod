from skybluetech_scripts.tooldelta.events.basic import CustomS2CEvent, CustomC2SEvent


class AssemblerUpgradersUpdate(CustomS2CEvent):
    name = "st:AULU"

    def __init__(self, lis=None):
        # type: (list[tuple[str, str, int]] | None) -> None
        self.lis = lis or []

    def marshal(self):
        return {"lis": self.lis}

    def unmarshal(self, data):
        self.lis = data["lis"]

ACTION_PUSH_UPGRADER = 0
ACTION_PULL_UPGRADER = 1


class AssemblerActionRequest(CustomC2SEvent):
    name = "st:APUR"

    def __init__(self, x=0, y=0, z=0, action=-1, index=-1):
        # type: (int, int, int, int, int) -> None
        self.x = x
        self.y = y
        self.z = z
        self.action = action
        self.index = index

    def marshal(self):
        return {"action": self.action, "index": self.index, "x": self.x, "y": self.y, "z": self.z}

    def unmarshal(self, data):
        self.action = data["action"]
        self.index = data["index"]
        self.x = data["x"]
        self.y = data["y"]
        self.z = data["z"]
        self.pid = data["__id__"]
