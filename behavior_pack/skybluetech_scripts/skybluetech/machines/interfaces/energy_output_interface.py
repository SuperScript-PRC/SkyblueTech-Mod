# coding=utf-8
#
from mod.server.blockEntityData import BlockEntityData
from ..basic import BaseMachine
from ..basic.register import RegisterMachine

REG_BLOCK_IDS = (   
)


@RegisterMachine
class EnergyOutputInterface(BaseMachine):
    store_rf_max = 160000
    extra_block_names = REG_BLOCK_IDS

    def __init__(self, dim, x, y, z, block_entity_data):
        # type: (int, int, int, int, BlockEntityData) -> None
        BaseMachine.__init__(self, dim, x, y, z, block_entity_data)
