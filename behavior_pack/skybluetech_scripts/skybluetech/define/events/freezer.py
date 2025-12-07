from skybluetech_scripts.tooldelta.events.basic import CustomC2SEvent


class FreezerModeChangedEvent(CustomC2SEvent):
    name = "st:FreezerModeChanged"

    def __init__(self, dim=0, x=0, y=0, z=0, new_mode=0):
        # type: (int, int, int, int, int) -> None
        self.dim = dim
        self.x = x
        self.y = y
        self.z = z
        self.new_mode = new_mode

    def marshal(self):
        return {
            "dim": self.dim,
            "x": self.x,
            "y": self.y,
            "z": self.z,
            "new_mode": self.new_mode
        }

    def unmarshal(self, data):
        # type: (dict) -> None
        self.dim = data["dim"]
        self.x = data["x"]
        self.y = data["y"]
        self.z = data["z"]
        self.new_mode = data["new_mode"]
        self.player_id = data["__id__"]
