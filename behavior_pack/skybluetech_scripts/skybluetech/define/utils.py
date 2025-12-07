NEIGHBOR_BLOCKS_ENUM = (
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, -1),
    (0, 0, 1),
    (-1, 0, 0),
    (1, 0, 0),
)

OPPOSITE_FACING = (1, 0, 3, 2, 5, 4)

def GetFacingByDxyz(dx, dy, dz):
    # type: (int, int, int) -> int
    return NEIGHBOR_BLOCKS_ENUM.index((dx, dy, dz))
