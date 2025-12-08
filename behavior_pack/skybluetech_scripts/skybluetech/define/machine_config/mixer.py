# -*- coding: utf-8 -*-
#
from .define import MachineRecipe, Input, Output

TAG_DUST_BLOCK = 'dust_block'

recipes = [
    MachineRecipe(
        {
            "fluid": {0: Input("minecraft:lava", 500)},
            "item": {0: Input("minecraft:netherrack", 1)}
        },
        {
            "item": {1: Output("minecraft:magma", 1)}
        },
        tick_duration=80, power_cost=40
    ),
    MachineRecipe(
        {
            "fluid": {0: Input("minecraft:water", 400)},
            "item": {0: Input("skybluetech:dust_block", 1)}
        },
        {
            "item": {1: Output("minecraft:clay", 1)}
        },
        tick_duration=40, power_cost=30
    ),
]
