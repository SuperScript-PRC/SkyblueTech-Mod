# coding=utf-8
#
from .define import MachineRecipe, Input, Output

recipes = [
    MachineRecipe(
        {"fluid": {0: Input("minecraft:water", 250)}},
        {"item": {0: Output("minecraft:snowball", 1)}},
        tick_duration=20, power_cost=50
    ),
    MachineRecipe(
        {"fluid": {0: Input("minecraft:water", 1000)}},
        {"item": {0: Output("minecraft:snow", 1)}},
        tick_duration=80, power_cost=40
    ),
    MachineRecipe(
        {"fluid": {0: Input("minecraft:water", 1000)}},
        {"item": {0: Output("minecraft:ice", 1)}},
        tick_duration=80, power_cost=50
    ),
    MachineRecipe(
        {"fluid": {0: Input("minecraft:water", 1000)}},
        {"item": {0: Output("minecraft:packed_ice", 1)}},
        tick_duration=75, power_cost=45
    ),
    MachineRecipe(
        {"fluid": {0: Input("minecraft:water", 10000)}},
        {"item": {0: Output("minecraft:blue_ice", 1)}},
        tick_duration=400, power_cost=50
    ),
]
