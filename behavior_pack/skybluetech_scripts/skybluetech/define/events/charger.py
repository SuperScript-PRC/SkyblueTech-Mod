from skybluetech_scripts.tooldelta.events.basic import CustomS2CEvent, CustomC2SEvent


class ChargerItemModelUpdate(CustomS2CEvent):
    name = "st:CIMU"

    def __init__(self, x=0, y=0, z=0, item_id=None, enchanted=False):
        # type: (int, int, int, str | None, bool) -> None
        self.x = x
        self.y = y
        self.z = z
        self.item_id = item_id
        self.enchanted = enchanted

    def marshal(self):
        return {"item_id": self.item_id, "enchanted": self.enchanted, "xyz": [self.x, self.y, self.z]}

    def unmarshal(self, data):
        self.item_id = data["item_id"]
        self.enchanted = data["enchanted"]
        self.x, self.y, self.z = data["xyz"]


class ChargeItemModelRequest(CustomC2SEvent):
    name = "st:CIMR"

    def __init__(self, x=0, y=0, z=0):
        # type: (int, int, int) -> None
        self.x = x
        self.y = y
        self.z = z
        self.pid = ""

    def marshal(self):
        return {"x":  self.x, "y": self.y, "z": self.z}

    def unmarshal(self, data):
        self.x = data["x"]
        self.y = data["y"]
        self.z = data["z"]
        self.pid = data["__id__"]

