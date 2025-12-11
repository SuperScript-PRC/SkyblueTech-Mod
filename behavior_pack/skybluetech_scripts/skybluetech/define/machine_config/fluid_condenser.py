# coding=utf-8
#
from .define import MachineRecipe, Input, Output

MC_METAL = {"copper", "iron", "gold"}

def recipeMolten2Ingot(metal_id, power_cost=80, tick_duration=180):
    # type: (str, int, int) -> MachineRecipe
    return MachineRecipe(
        {"fluid": {0: Input("skybluetech:molten_" + metal_id, 144)}}, 
        {"item": {0: Output(("minecraft:" if metal_id in MC_METAL else "skybluetech:") + metal_id + "_ingot", 1)}},
        power_cost=power_cost, tick_duration=tick_duration
    )


recipes = [
    MachineRecipe(
        {"fluid": {0: Input("minecraft:lava", 1000)}},
        {"item": {0: Output("minecraft:obsidian", 1)}},
        tick_duration=200, power_cost=50
    ),
    #
    recipeMolten2Ingot("copper"),
    recipeMolten2Ingot("iron"),
    recipeMolten2Ingot("gold"),
    recipeMolten2Ingot("tin"),
    recipeMolten2Ingot("lead"),
    recipeMolten2Ingot("silver"),
    recipeMolten2Ingot("platinum"),
    recipeMolten2Ingot("nickel"),
]
