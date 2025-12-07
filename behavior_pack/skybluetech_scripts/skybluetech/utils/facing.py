def GetFrontDirFromFacing(facing):
    # type: (str) -> tuple[int, int, int]
    return {
        "north": (0, 0, -1),
        "south": (0, 0, 1),
        "east": (1, 0, 0),
        "west": (-1, 0, 0),
        "up": (0, 1, 0),
        "down": (0, -1, 0),
    }[facing]

def GetOppositeDirFromFacing(facing):
    # type: (str) -> tuple[int, int, int]
    return {
        "north": (0, 0, 1),
        "south": (0, 0, -1),
        "east": (-1, 0, 0),
        "west": (1, 0, 0),
        "up": (0, -1, 0),
        "down": (0, 1, 0),
    }[facing]
