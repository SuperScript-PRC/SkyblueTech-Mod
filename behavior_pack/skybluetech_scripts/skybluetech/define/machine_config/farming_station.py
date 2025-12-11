# coding=utf-8
#

COMMON_CROPS = {
    "minecraft:wheat",
    "minecraft:potatoes",
    "minecraft:carrots",
    "minecraft:beetroot",
}

FULL_BLOCK_CROPS = {
    "minecraft:melon_block",
    "minecraft:pumpkin",
}

def isCommonCrop(block_name):
    # type: (str) -> bool
    return block_name in COMMON_CROPS

def isCommonCropRiped(block_states):
    # type: (dict) -> bool
    return block_states["growth"] == 7

def isArrisCrop(block_states):
    # type: (dict) -> bool
    return "arris:growth" in block_states

def isArrisCropRiped(block_states):
    # type: (dict) -> bool
    return block_states["arris:growth"] == 7

def isBlockCrop(block_name):
    return block_name in FULL_BLOCK_CROPS

