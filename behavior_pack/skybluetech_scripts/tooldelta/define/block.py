# -*- coding: utf-8 -*-

class BlockBasicInfo(object):
    blockLightAbsorption = 0 # type: int
    """ 方块透光率, 具体见官方wiki(opens new window) """
    blockLightEmission = 0 # type: int
    """ 方块亮度, 具体见官方wiki(opens new window) """
    breathability = 0 # type: int
    """ 方块的 可呼吸性 (只有定义了"minecraft:breathability"组件的方块有数据,其余默认为solid的枚举值)(需要开启假日创造者功能) """
    explosionResistance = 0.0 # type: float
    """ 方块爆炸抗性 """
    loot = '' # type: str
    """ loot table控制掉落物(只有定义了"minecraft:loot"组件的方块有数据,其余默认为空字符串"") """
    mapColor = '' # type: str
    """ 用十六进制颜色定义该方块在地图上显示的颜色(只有定义了"minecraft:map_color"组件的方块以及部分原版方块有数据,其余默认为"#0") """
    unwalkable = False # type: bool
    """ 生物是否可在上方行走,默认为false(只有定义了"minecraft:unwalkable"组件的方块有数据,其余默认为false) """
    tier = None # type: dict | None
    """ 与挖掘相关的属性,具体见挖掘属性(只有定义了"netease:tier"组件的方块有数据,其余默认为None) """
    renderLayer = 0 # type: int
    """ 方块渲染时使用的 材质 """
    solid = False # type: bool
    """ 方块是否为实心方块,影响生物在方块内是否受到窒息伤害 """
    pathable = False # type: bool
    """ 游戏内AI在进行寻路时，方块是否被当作障碍物(只有定义了"netease:pathable"组件的方块有数据,其余默认为false) """
    fireResistant = False # type: bool
    """ 方块是否防火(只有定义了"netease:fire_resistant"组件的方块有数据,其余默认为false) """
    creativeCategory = 0 # type: int
    """ 方块所在 创造栏目录 """
    destroyTime = 0.0 # type: float
    """ 方块摧毁时间 """

    @classmethod
    def unmarshal(cls, data):
        # type: (dict) -> BlockBasicInfo
        self = cls()
        self.blockLightAbsorption = data["blockLightAbsorption"]
        self.blockLightEmission = data["blockLightEmission"]
        self.breathability = data.get("breathability", 0)
        self.explosionResistance = data["explosionResistance"]
        self.loot = data["loot"]
        self.mapColor = data["mapColor"]
        self.unwalkable = data["unwalkable"]
        self.tier = data["tier"]
        self.renderLayer = data["renderLayer"]
        self.solid = data["solid"]
        self.pathable = data["pathable"]
        self.fireResistant = data["fireResistant"]
        self.creativeCategory = data["creativeCategory"]
        self.destroyTime = data["destroyTime"]
        return self

    def marshal(self):
        # type: () -> dict
        return {
            "blockLightAbsorption": self.blockLightAbsorption,
            "blockLightEmission": self.blockLightEmission,
            "breathability": self.breathability,
            "explosionResistance": self.explosionResistance,
            "loot": self.loot,
            "mapColor": self.mapColor,
            "unwalkable": self.unwalkable,
            "tier": self.tier,
            "renderLayer": self.renderLayer,
            "solid": self.solid,
            "pathable": self.pathable,
            "fireResistant": self.fireResistant,
            "creativeCategory": self.creativeCategory,
            "destroyTime": self.destroyTime,
        }
