# -*- coding: utf-8 -*-
#

from .define import PresetMachineRecipe, Input, Output

DEFAULT_TICK_DURATION = 160
DEFAULT_POWER = 80
L_TICK_DURATION = 200
L_POWER = 120

preset = PresetMachineRecipe(DEFAULT_POWER, DEFAULT_TICK_DURATION)
preset2 = PresetMachineRecipe(L_POWER, L_TICK_DURATION)

TAG_TIN_DUST = "dusts/tin"
TAG_COPPER_DUST = "dusts/copper"
TAG_IRON_DUST = "dusts/iron"
TAG_NICKEL_DUST = "dusts/nickel"
TAG_COAL_DUST = "dusts/coal"

TAG_TIN_INGOT = "ingots/tin"
TAG_NICKEL_INGOT = "ingots/nickel"

recipes = [
    # Alloy
    preset.ItemRecipe(
        {0: Input("dusts/copper", 3, True), 1: Input(TAG_TIN_DUST, 1, True)},
        {2: Output("skybluetech:bronze_ingot", 4)}
    ),
    preset2.ItemRecipe(
        {0: Input("minecraft:copper_ingot", 3), 1: Input(TAG_TIN_INGOT, 1, True)},
        {2: Output("skybluetech:bronze_ingot", 4)}
    ),
    preset.ItemRecipe(
        {0: Input(TAG_IRON_DUST, 2, True), 1: Input(TAG_NICKEL_DUST, 1, True)},
        {2: Output("skybluetech:invar_ingot", 3)}
    ),
    preset2.ItemRecipe(
        {0: Input("minecraft:iron_ingot", 3, True), 1: Input(TAG_NICKEL_INGOT, 1, True)},
        {2: Output("skybluetech:invar_ingot", 4)}
    ),
    preset.ItemRecipe(
        {0: Input(TAG_IRON_DUST, 1, True), 1: Input(TAG_COAL_DUST, 1, True)},
        {2: Output("skybluetech:steel_ingot", 1)}
    ),
    preset2.ItemRecipe(
        {0: Input("minecraft:iron_ingot", 1), 1: Input(TAG_COAL_DUST, 1, True)},
        {2: Output("skybluetech:steel_ingot", 1)}
    )
]
