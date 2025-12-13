# coding=utf-8
#
from mod.common.component.blockPaletteComp import BlockPaletteComponent
from skybluetech_scripts.tooldelta.api.timer import AsDelayFunc
from skybluetech_scripts.tooldelta.events.server import (
    BlockRemoveServerEvent,
    EntityPlaceBlockAfterServerEvent,
)
from skybluetech_scripts.tooldelta.general import ServerInitCallback
from skybluetech_scripts.tooldelta.api.server.block import (
    AddBlocksToBlockRemoveListener,
    GetBlockPaletteBetweenPos,
)
from ...define.flags import DEACTIVE_FLAG_STRUCTURE_BROKEN
from .base_machine import BaseMachine, GUIControl

if 0:
    from typing import TypeVar
    from .base_machine import BaseMachine

    MT = TypeVar("MT", bound=BaseMachine)
    BLOCK_PAT_INDEX = int
    POS_SET = set[tuple[int, int, int]]

blockRemovedListenPool = set()  # type: set[str]

server_inited = False


@ServerInitCallback()
def onServerInit():
    global server_inited
    print(blockRemovedListenPool)
    AddBlocksToBlockRemoveListener(blockRemovedListenPool)
    server_inited = True


@EntityPlaceBlockAfterServerEvent.Listen()
@AsDelayFunc(0)
def onEntityPlaceBlock(event):
    # type: (EntityPlaceBlockAfterServerEvent) -> None
    x = event.x
    y = event.y
    z = event.z
    for area in detect_areas.get(event.dimensionId, set()):
        if not area.bound._last_destroyed:
            continue
        if area.isInside(x, y, z):
            if area.Detect():
                print("Detect OK")
                area.bound.UnsetStructureDestroyed()
            else:
                print("Detect failed")
                area.bound.SetStructureDestroyed()
            area.bound.OnStructureChanged()


@BlockRemoveServerEvent.Listen(-100)
@AsDelayFunc(0)
def onBlockRemoved(event):
    # type: (BlockRemoveServerEvent) -> None
    x = event.x
    y = event.y
    z = event.z
    for area in detect_areas.get(event.dimension, set()):
        if area.bound._last_destroyed:
            continue
        if area.isInside(x, y, z):
            if area.Detect():
                print("Detect OK")
                area.bound.UnsetStructureDestroyed()
            else:
                print("Detect failed")
                area.bound.SetStructureDestroyed()
            area.bound.OnStructureChanged()


detect_areas = {}  # type: dict[int, set[DetectArea]]


def addDetectArea(dim, area):
    # type: (int, DetectArea) -> None
    detect_areas.setdefault(dim, set()).add(area)


def removeDetectArea(dim, area):
    # type: (int, DetectArea) -> None
    detect_areas[dim].remove(area)
    if not detect_areas[dim]:
        del detect_areas[dim]


def rotate_90(x, z, x1, z1, y):
    # type: (int, int, int, int, int) -> tuple[int, int, int]
    dx = x - x1
    dz = z - z1
    return (x1 + dz, y, z1 - dx)


class DetectArea(object):
    def __init__(self, dim, center_x, center_y, center_z, bound):
        # type: (int, int, int, int, MultiBlockStructure) -> None
        pal = bound._palette
        self.dim = dim
        self.min_x = min(pal.min_x, -pal.min_x, pal.min_z, -pal.min_z) + center_x
        self.min_y = pal.min_y + center_y
        self.min_z = min(pal.min_x, -pal.min_x, pal.min_z, -pal.min_z) + center_z
        self.max_x = max(pal.min_x, -pal.min_x, pal.min_z, -pal.min_z) + center_x
        self.max_y = pal.max_y + center_y
        self.max_z = max(pal.min_x, -pal.min_x, pal.min_z, -pal.min_z) + center_z
        self.center_x = center_x
        self.center_y = center_y
        self.center_z = center_z
        self.bound = bound
        palette = bound.structure_palette
        if palette is None:
            raise ValueError("StructureBlockPalette: palette is None")
        self.palette = palette
        self.functional_block_poses = {}  # type: dict[str, list[tuple[int, int, int]]]

    def isInside(self, x, y, z):
        return (
            x >= self.min_x
            and x <= self.max_x
            and y >= self.min_y
            and y <= self.max_y
            and z >= self.min_z
            and z <= self.max_z
        )

    def __hash__(self):
        return hash((
            self.min_x,
            self.min_y,
            self.min_z,
            self.max_x,
            self.max_y,
            self.max_z,
        ))

    def Detect(self):
        # type: () -> bool
        spalette = self.palette
        current_palette = GetBlockPaletteBetweenPos(
            self.dim,
            (self.min_x, self.min_y, self.min_z),
            (self.max_x, self.max_y, self.max_z),
            eliminateAir=False,
        )
        if current_palette is None:
            return False
        co_x = self.center_x - self.min_x
        co_y = self.center_y - self.min_y
        co_z = self.center_z - self.min_z
        # print(
        #     "Comparing",
        #     (
        #         spalette.min_x + self.center_x,
        #         spalette.min_y + self.center_y,
        #         spalette.min_z + self.center_z,
        #     ),
        #     (
        #         spalette.max_x + self.center_x,
        #         spalette.max_y + self.center_y,
        #         spalette.max_z + self.center_z,
        #     ),
        #     "Getting",
        #     (self.min_x, self.min_y, self.min_z),
        #     (self.max_x, self.max_y, self.max_z),
        #     co_x,
        #     co_z,
        # )
        if spalette.Compare(current_palette, co_x, co_z):
            if spalette.BlocksEnough(current_palette):
                self.updateFunctionalBlocks(current_palette, co_x, co_y, co_z)
                return True
        for _ in range(3):
            spalette = spalette.Rotate()
            # print(
            #     "Comparing",
            #     (
            #         spalette.min_x + self.center_x,
            #         spalette.min_y + self.center_y,
            #         spalette.min_z + self.center_z,
            #     ),
            #     (
            #         spalette.max_x + self.center_x,
            #         spalette.max_y + self.center_y,
            #         spalette.max_z + self.center_z,
            #     ),
            # )
            if spalette.Compare(current_palette, co_x, co_z):
                if spalette.BlocksEnough(current_palette):
                    self.updateFunctionalBlocks(current_palette, co_x, co_y, co_z)
                    return True
        return False

    def updateFunctionalBlocks(self, palette, co_x, co_y, co_z):
        # type: (BlockPaletteComponent, int, int, int) -> None
        self.functional_block_poses = {
            block_id: [
                (x - co_x + self.center_x, y - co_y + self.min_y, z - co_z + self.center_z)
                for x, y, z in
                palette.GetLocalPosListOfBlocks(block_id)
            ]
            for block_id in self.bound.functional_block_ids
        }


class StructureBlockPalette(object):
    def __init__(
        self,
        posblock_data,  # type: dict[int, set[tuple[int, int, int]]]
        palette_data,  # type: dict[int, str | set[str]]
        min_x,  # type: int
        min_y,  # type: int
        min_z,  # type: int
        max_x,  # type: int
        max_y,  # type: int
        max_z,  # type: int
        require_blocks_count,  # type: dict[str, int]
        _rotation=0,
    ):
        # type: (...) -> None
        # 原点坐标为 (0, 0, 0)
        self.posblock_data = posblock_data
        self.palette_data = palette_data
        self.min_x = min_x
        self.min_y = min_y
        self.min_z = min_z
        self.max_x = max_x
        self.max_y = max_y
        self.max_z = max_z
        self.require_blocks_count = require_blocks_count
        self._rotation = _rotation
        # self.all_poses = set(j for i in posblock_data.values() for j in i)
        if not server_inited:
            for block_id in palette_data.values():
                if isinstance(block_id, str):
                    blockRemovedListenPool.add(block_id)
                else:
                    blockRemovedListenPool.update(block_id)

    def Compare(self, block_palette, co_x, co_z):
        # type: (BlockPaletteComponent, int, int) -> bool
        """
        比较方块调色板内容是否与此调色板匹配。

        Args:
            block_palette (BlockPaletteComponent): 调色板
            center_x (int): 调色板中心偏移x
            center_z (int): 调色板中心偏移z
        """
        for index, block_ids in self.palette_data.items():
            if isinstance(block_ids, str):
                block_ids = {block_ids}
            pal_poses_set = set(
                (x - co_x, y, z - co_z)
                for block_id in block_ids
                for x, y, z in block_palette.GetLocalPosListOfBlocks(block_id)
            )
            my_poses_set = self.posblock_data[index]
            # len 比较可能比直接比较好?
            if len(pal_poses_set & my_poses_set) < len(my_poses_set):
                # print "======"
                # print "not equal:"
                # print len(pal_poses_set & my_poses_set), len(my_poses_set)
                # print block_ids
                # print ([
                #         (x - co_x, y, z - co_z)
                #         for block_id in block_ids
                #         for x, y, z in block_palette.GetLocalPosListOfBlocks(block_id)
                # ])
                # print my_poses_set.difference(pal_poses_set)
                return False
        return True

    def BlocksEnough(self, block_palette):
        # type: (BlockPaletteComponent) -> bool
        """
        判断方块调色板是否满足此结构所需方块数量。

        Args:
            block_palette (BlockPaletteComponent): 调色板
        """
        for block_id, count in self.require_blocks_count.items():
            if block_palette.GetBlockCountInBlockPalette(block_id) < count:
                print("BlocksNotEnough", block_id, count)
                return False
        return True

    def Rotate(self):
        # type: () -> StructureBlockPalette
        x1, _, z1 = rotate_90(self.min_x, self.min_z, 0, 0, self.min_y)
        x2, _, z2 = rotate_90(self.max_x, self.max_z, 0, 0, self.max_y)
        new_min_x = min(x1, x2)
        new_max_x = max(x1, x2)
        new_min_z = min(z1, z2)
        new_max_z = max(z1, z2)
        newPosBlockDat = {
            idx: set(rotate_90(x, z, 0, 0, y) for x, y, z in poses)
            for idx, poses in self.posblock_data.items()
        }
        return StructureBlockPalette(
            newPosBlockDat,
            self.palette_data,
            new_min_x,
            self.min_y,
            new_min_z,
            new_max_x,
            self.max_y,
            new_max_z,
            self.require_blocks_count,
            _rotation=self._rotation + 90,
        )


class MultiBlockStructure(BaseMachine):
    """
    多方块机器结构的基类。

    需要调用 `__init__()`

    覆写: `OnLoad`, `OnUnload`
    """

    structure_palette = None  # type: StructureBlockPalette | None
    functional_block_ids = set()  # type: set[str]

    def __init__(self, dim, x, y, z, block_entity_data):
        if self.structure_palette is None:
            raise ValueError("StructureBlockPalette: structure_palette is None")
        self._last_destroyed = False
        self._palette = self.structure_palette
        self.dim = dim
        self.x = x
        self.y = y
        self.z = z

    def OnLoad(self):
        self.area = DetectArea(self.dim, self.x, self.y, self.z, self)
        addDetectArea(self.dim, self.area)
        if self.area.Detect():
            self.area.bound.UnsetStructureDestroyed()
        else:
            self.area.bound.SetStructureDestroyed()

    def OnStructureChanged(self):
        "覆写方法用于结构变更的回调。"

    def OnUnload(self):
        removeDetectArea(self.dim, self.area)

    def SetStructureDestroyed(self):
        if not self._last_destroyed:
            self.SetDeactiveFlag(DEACTIVE_FLAG_STRUCTURE_BROKEN)
            self._last_destroyed = True
            if isinstance(self, GUIControl):
                self.OnSync()

    def UnsetStructureDestroyed(self):
        if self._last_destroyed:
            self.UnsetDeactiveFlag(DEACTIVE_FLAG_STRUCTURE_BROKEN)
            self._last_destroyed = False
            if isinstance(self, GUIControl):
                self.OnSync()

    def GetFunctionalBlockPoses(self):
        return self.area.functional_block_poses

    # StructureUtils

    def GetMachine(self, cls, block_id=None, index=0):
        # type: (type[MT], str | None, int) -> MT
        block_id = block_id or cls.block_name
        pos = self.GetFunctionalBlockPoses().get(block_id)
        if not pos:
            raise ValueError("Cannot find block: %s" % block_id)
        from ..pool import GetMachineStrict
        x, y, z = pos[index]
        machine = GetMachineStrict(self.dim, x, y, z)
        if not isinstance(machine, cls):
            raise ValueError(
                "({}, {}, {}): {} is not a {}".format(
                    x, y, z,
                    type(machine).__name__, cls.__name__
                )
            )
        return machine


def GenerateSimpleStructureTemplate(
    key,  # type: dict[str, str] | dict[str, str | set[str]]
    pattern,  # type: dict[int, list[str]]
    center_block_sign="#",  # type: str
    require_blocks_count=None,  # type: dict[str, int] | None
):
    # type: (...) -> StructureBlockPalette
    """
    key: 单字母键 -> 方块 ID
    """
    orig_posblock_data = {}  # type: dict[BLOCK_PAT_INDEX, POS_SET]
    palette_data = {}  # type: dict[int, str | set[str]]
    pat2idx = {}  # type: dict[str, int]
    offset_x = None  # type: int | None
    offset_y = None  # type: int | None
    offset_z = None  # type: int | None
    min_x = 999
    min_y = 999
    min_z = 999
    max_x = -999
    max_y = -999
    max_z = -999

    def get_index_by_pattern(pattern):
        # type: (str) -> BLOCK_PAT_INDEX
        if pattern not in pat2idx:
            idx = pat2idx[pattern] = len(pat2idx)
            palette_data[idx] = key[pattern]
        return pat2idx[pattern]

    for layer, platform in pattern.items():
        if layer < min_y:
            min_y = layer
        elif layer > max_y:
            max_y = layer
        for z, row_data in enumerate(platform):
            if z < min_z:
                min_z = z
            elif z > max_z:
                max_z = z
            for x, pat in enumerate(row_data):
                if pat == " ":
                    continue
                if x < min_x:
                    min_x = x
                elif x > max_x:
                    max_x = x
                if pat == center_block_sign:
                    offset_x = x
                    offset_y = layer
                    offset_z = z
                    continue
                idx = get_index_by_pattern(pat)
                orig_posblock_data.setdefault(idx, set()).add((x, layer, z))

    if offset_x is None or offset_y is None or offset_z is None:
        raise ValueError("Invalid pattern")

    posblock_data = {
        k: {(x - offset_x, y - offset_y, z - offset_z) for x, y, z in v}
        for k, v in orig_posblock_data.items()
    }
    return StructureBlockPalette(
        posblock_data,
        palette_data,
        min_x - offset_x,
        min_y - offset_y,
        min_z - offset_z,
        max_x - offset_x,
        max_y - offset_y,
        max_z - offset_z,
        require_blocks_count or {},
    )
