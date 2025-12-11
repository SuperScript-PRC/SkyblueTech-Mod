# coding=utf-8
#
from mod.common.component.blockPaletteComp import BlockPaletteComponent
from skybluetech_scripts.tooldelta.events.server.block import BlockRemoveServerEvent, ServerPlaceBlockEntityEvent
from skybluetech_scripts.tooldelta.general import ServerInitCallback
from skybluetech_scripts.tooldelta.api.server.block import AddBlocksToBlockRemoveListener, GetBlockPaletteFromPosList
from ...define.flags import DEACTIVE_FLAG_STRUCTURE_BROKEN
from .base_machine import BaseMachine

if 0:
    BLOCK_PAT_INDEX = int
    POS_SET = set[tuple[int, int, int]]

blockRemovedListenPool = set()

@ServerInitCallback()
def onServerInit():
    AddBlocksToBlockRemoveListener(blockRemovedListenPool)

@ServerPlaceBlockEntityEvent.Listen()
def onEntityPlaceBlock(event):
    # type: (ServerPlaceBlockEntityEvent) -> None
    x = event.posX
    y = event.posY
    z = event.posZ
    for area in detect_areas.get(event.dimension, set()):
        if area.isInside(x, y, z):
            if area.Detect():
                area.bound.UnsetStructureDestroyed()
            else:
                area.bound.SetStructureDestroyed()
            area.bound.OnStructureChanged()


@BlockRemoveServerEvent.Listen(-1000)
def onBlockRemoved(event):
    # type: (BlockRemoveServerEvent) -> None
    x = event.x
    y = event.y
    z = event.z
    for area in detect_areas.get(event.dimension, set()):
        if area.isInside(x, y, z):
            if area.Detect():
                area.bound.UnsetStructureDestroyed()
            else:
                area.bound.SetStructureDestroyed()
            area.bound.OnStructureChanged()


detect_areas = {} # type: dict[int, set[DetectArea]]

def addDetectArea(dim, area):
    # type: (int, DetectArea) -> None
    detect_areas.setdefault(dim, set()).add(area)

def removeDetectArea(dim, area):
    # type: (int, DetectArea) -> None
    detect_areas[dim].remove(area)
    if not detect_areas[dim]:
        del detect_areas[dim]


class DetectArea(object):
    def __init__(self, dim, x, y, z, dx, dy, dz, bound):
        # type: (int, int, int, int, int, int, int, MultiBlockStructure) -> None
        self.dim = dim
        self.x = x
        self.y = y
        self.z = z
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.bound = bound
        palette = bound.structure_palette
        if palette is None:
            raise ValueError('StructureBlockPalette: palette is None')
        self.palette = palette

    def isInside(self, x, y, z):
        return (
            x >= self.x and x < self.x + self.dx
            and y >= self.y and y < self.y + self.dy
            and z >= self.z and z < self.z + self.dz
        )

    def __hash__(self):
        return hash((self.x, self.y, self.z, self.dx, self.dy, self.dz))

    def Detect(self):
        # type: () -> bool
        spalette = self.palette
        current_palette = GetBlockPaletteFromPosList(self.dim, spalette.all_poses)
        if spalette.Compare(current_palette):
            return True
        for _ in range(3):
            spalette = spalette.Rotate()
            if spalette.Compare(current_palette):
                return True
        return False


class StructureBlockPalette(object):
    def __init__(self, posblock_data, palette_data, max_x, max_y, max_z):
        # type: (dict[int, set[tuple[int, int, int]]], dict[int, str], int, int, int) -> None
        # posblock_data 的 x y z 最小值必须为 (0, 0, 0)
        self.posblock_data = posblock_data
        self.palette_data = palette_data
        self.max_x = max_x
        self.max_y = max_y
        self.max_z = max_z
        self.all_poses = list(j for i in posblock_data.values() for j in i)

    def Compare(self, block_palette):
        # type: (BlockPaletteComponent) -> bool
        for index, block_id in self.palette_data.items():
            pal_poses_set = set(block_palette.GetLocalPosListOfBlocks(block_id))
            my_poses_set = self.posblock_data[index]
            # len 比较可能比直接比较好?
            if len(pal_poses_set & my_poses_set) != len(my_poses_set):
                return False
        return True

    def Rotate(self):
        max_x = self.max_x
        max_z = self.max_z
        newPosBlockDat = {
            idx: set((max_z - z, y, max_x - x) for x, y, z in poses)
            for idx, poses in self.posblock_data.items()
        }
        return StructureBlockPalette(newPosBlockDat, self.palette_data, max_z, self.max_y, max_x)


class MultiBlockStructure(BaseMachine):
    """
    多方块机器结构的基类。
    
    需要调用 `__init__()`
    
    覆写: `OnUnload`
    """
    stucture_start_offset = (0, 0, 0) # type: tuple[int, int, int]
    structure_palette = None # type: StructureBlockPalette | None

    def __init__(self, dim, x, y, z, block_entity_data):
        if self.structure_palette is None:
            raise ValueError('StructureBlockPalette: structure_palette is None')
        self._last_destroyed = False
        offsetx, offsety, offsetz = self.stucture_start_offset
        self.area = DetectArea(
            dim, x + offsetx, y + offsety, z + offsetz,
            self.structure_palette.max_x,
            self.structure_palette.max_y,
            self.structure_palette.max_z,
            self
        )
        addDetectArea(dim, self.area)

    def OnStructureChanged(self):
        "覆写方法用于结构变更的回调。"

    def OnUnload(self):
        removeDetectArea(self.dim, self.area)

    def SetStructureDestroyed(self):
        if not self._last_destroyed:
            self.SetDeactiveFlag(DEACTIVE_FLAG_STRUCTURE_BROKEN)
            self._last_destroyed = True

    def UnsetStructureDestroyed(self):
        if self._last_destroyed:
            self.UnsetDeactiveFlag(DEACTIVE_FLAG_STRUCTURE_BROKEN)
            self._last_destroyed = False

def GenerateSimpleStructureTemplate(key, pattern, center_block_sign="#", size=(1, 1, 1)):
    # type: (dict[str, str], dict[int, list[str]], str, tuple[int, int, int]) -> tuple[StructureBlockPalette, tuple[int, int, int]]
    """
    key: 单字母键 -> 方块 ID
    """
    orig_posblock_data = {} # type: dict[BLOCK_PAT_INDEX, POS_SET]
    palette_data = {} # type: dict[int, str]
    pat2idx = {} # type: dict[str, int]
    offset_x = None # type: int | None
    offset_y = None # type: int | None
    offset_z = None # type: int | None

    def get_index_by_pattern(pattern):
        # type: (str) -> BLOCK_PAT_INDEX
        if pattern not in pat2idx:
            idx = pat2idx[pattern] = len(pat2idx)
            palette_data[idx] = key[pattern]
        return pat2idx[pattern]

    for layer, platform in pattern.items():
        for z, row_data in enumerate(platform):
            for x, pat in enumerate(row_data):
                if pat == " ":
                    continue
                if pat == center_block_sign:
                    offset_x = -x
                    offset_y = -layer
                    offset_z = -z
                    continue
                idx = get_index_by_pattern(pat)
                orig_posblock_data.setdefault(idx, set()).add((x, layer, z))

    if offset_x is None or offset_y is None or offset_z is None:
        raise ValueError("Invalid pattern")

    return (
        StructureBlockPalette(
            orig_posblock_data,
            palette_data,
            size[0], size[1], size[2],
        ),
        (offset_x, offset_y, offset_z)
    )


