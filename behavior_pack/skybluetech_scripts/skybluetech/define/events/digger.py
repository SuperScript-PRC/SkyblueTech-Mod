from skybluetech_scripts.tooldelta.events.basic import CustomS2CEvent


class DiggerWorkModeUpdatedEvent(CustomS2CEvent):
    name = "st:DWMC"

    def __init__(self, x=0, y=0, z=0, active=False):
        # type: (int, int, int, bool) -> None
        self.x = x
        self.y = y
        self.z = z
        self.active = active

    def marshal(self):
        return {
            "x": self.x,
            "y": self.y,
            "z": self.z,
            "active": self.active,
        }

    def unmarshal(self, data):
        self.x = data["x"]
        self.y = data["y"]
        self.z = data["z"]
        self.active = data["active"]


class DiggerUpdateCrack(CustomS2CEvent):
    name = "st:DUC"

    def __init__(self, dim=0, x=0, y=0, z=0, level=0):
        # type: (int, int, int, int, int) -> None
        self.dim = dim
        self.x = x
        self.y = y
        self.z = z
        self.level = level

    def marshal(self):
        return {
            "dim": self.dim,
            "x": self.x,
            "y": self.y,
            "z": self.z,
            "level": self.level,
        }

    def unmarshal(self, data):
        self.dim = data["dim"]
        self.x = data["x"]
        self.y = data["y"]
        self.z = data["z"]
        self.level = data["level"]
