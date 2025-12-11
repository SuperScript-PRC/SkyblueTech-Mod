# coding=utf-8
#
from ....tooldelta.no_runtime_typing import TYPE_CHECKING

# TYPE_CHECKING
if TYPE_CHECKING:
    PosData = tuple[int, int, int, int]
# TYPE_CHECKING END


class CableNetwork:
    def __init__(self, dim, group_inputs, group_outputs, cable_level=0):
        # type: (int, set[PosData], set[PosData], int) -> None
        self.dim = dim
        self.group_inputs = group_inputs
        self.group_outputs = group_outputs
        self.cable_level = cable_level
        self.inited_containers = 0
        self.all_containers = 0
        self.wire_nodes = set() # type: set[tuple[int, int, int]] # not_set_yet

    def AllContainersInited(self):
        return self.inited_containers == self.all_containers

    def AddAwakeNum(self):
        # if not self.AllDevicesInited():
        #     self.inited_tanks += 1
        self.inited_containers += 1
        if self.inited_containers > self.all_containers:
            print ("[ERROR] inited_tanks > all_containers", self.inited_containers, self.all_containers)

    def AddCableNode(self, xyz):
        # type: (tuple[int, int, int]) -> None
        self.wire_nodes.add(xyz)

    def __repr__(self):
        return "CableNetwork({}, {})".format(self.group_inputs, self.group_outputs)
            

    def __hash__(self):
        return hash((tuple(self.group_inputs), tuple(self.group_outputs)))

    def same(self, other):
        # type: (CableNetwork) -> bool
        return self.group_inputs == other.group_inputs and self.group_outputs == other.group_outputs


