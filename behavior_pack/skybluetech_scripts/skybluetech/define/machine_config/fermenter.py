IO_ENERGY = "skybluetech:fermenter_io_energy"
IO_FLUID1 = "skybluetech:fermenter_io_fluid1"
IO_FLUID2 = "skybluetech:fermenter_io_fluid2"
IO_GAS = "skybluetech:fermenter_io_gas"
IO_ITEM = "skybluetech:fermenter_io_item1"
MUDBRICK = "minecraft:mud_bricks"
GLASS = "minecraft:glass"
STRUCTURE_PATTERN_MAPPING = {
    "M": MUDBRICK,
    "m": {MUDBRICK, IO_GAS, IO_ENERGY, IO_ITEM},
    "i": {MUDBRICK, IO_FLUID1, IO_FLUID2, IO_ENERGY, IO_ITEM},
    "G": GLASS,
    "g": {GLASS, MUDBRICK, IO_ENERGY}
}
STRUCTURE_PATTERN ={
    0: [
        "iii",
        "iMi",
        "i#i"
    ],
    1: [
        "MGM",
        "G G",
        "MGM"
    ],
    2: [
        "mmm",
        "mgm",
        "mmm"
    ]
}
STRUCTURE_REQUIRE_BLOCKS = {
    IO_ENERGY: 1,
    IO_ITEM: 1,
    IO_FLUID1: 1,
    IO_FLUID2: 1,
    IO_GAS: 1,
}

TEMPERATURE_MIN = 10
TEMPERATURE_MAX = 50
POOL_MAX_VOLUME = 16000

HI_TEMPERATURE_VITALITY_REDUCE = 0.01
LO_TEMPERATURE_VITALITY_REDUCE = 0.008
VITALITY_ADD_MAX = 0.005
BATERIA_MAX_HUNGER = 1
BATERIA_MIN_HUNGER = -1
VITALITY_HUNGER_REDUCE_MAX = 0.05
HUNGER_REDUCE = 0.01

class FermenterRecipe:
    def __init__(
        self,
        color, # type: int
        vitality_matter, # type: str
        vitality_count, # type: float
        inoculate_time, # type: float
        nutrition_matter, # type: str
        nutrition_count, # type: float
        min_temperature, # type: float
        max_temperature, # type: float
        fit_temperature, # type: float
        max_grow_speed, # type: float
        max_thickness, # type: float
        produce_thickness, # type: float
        out_gas_id, # type: str
        out_gas_volume, # type: float
        out_fluid_id, # type: str
        out_fluid_volume, # type: float
        volume_reduce, # type: float
    ):
        self.color = color
        self.vitality_matter = vitality_matter
        self.vitality_count = vitality_count
        self.inoculate_time = inoculate_time
        self.nutrition_matter = nutrition_matter
        self.nutrition_count = nutrition_count
        self.min_temperature = min_temperature
        self.max_temperature = max_temperature
        self.fit_temperature = fit_temperature
        self.max_grow_speed = max_grow_speed
        self.max_thickness = max_thickness
        self.produce_thickness = produce_thickness
        self.out_gas_id = out_gas_id
        self.out_gas_volume = out_gas_volume
        self.out_fluid_id = out_fluid_id
        self.out_fluid_volume = out_fluid_volume
        self.volume_reduce = volume_reduce


spec_recipes = {
    1: FermenterRecipe(
        color=0x9a6f4f,
        vitality_matter="minecraft:dirt",
        vitality_count=0.1,
        inoculate_time=30,
        nutrition_matter="skybluetech:bio_dust",
        nutrition_count=0.05,
        min_temperature=25,
        max_temperature=40,
        fit_temperature=30,
        max_grow_speed=0.1,
        max_thickness=0.6,
        produce_thickness=0.4,
        out_gas_id="skybluetech:methane",
        out_gas_volume=10,
        out_fluid_id="skybluetech:nutrious_mud",
        out_fluid_volume=1,
        volume_reduce=0.05,
    )
}

