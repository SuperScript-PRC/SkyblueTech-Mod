# -*- coding: utf-8 -*-
#
import time
from skybluetech_scripts.tooldelta.events.client.item import (
    ClientItemTryUseEvent,
    ClientItemUseOnEvent,
)
from .register import item_pre_use_cbs, item_pre_use_on_block_cbs

last_item_use_time = 0

@ClientItemTryUseEvent.Listen(1000)
def onItemTryUse(event):
    # type: (ClientItemTryUseEvent) -> None
    global last_item_use_time
    if event.item.id not in item_pre_use_cbs:
        return
    nowtime = time.time()
    if nowtime - last_item_use_time < 0.2:
        event.cancel()
        return
    last_item_use_time = nowtime

@ClientItemUseOnEvent.Listen(1000)
def onItemTryUseOn(event):
    # type: (ClientItemUseOnEvent) -> None
    global last_item_use_time
    if event.item.id not in item_pre_use_on_block_cbs:
        return
    nowtime = time.time()
    if nowtime - last_item_use_time < 0.2:
        event.cancel()
        return
    last_item_use_time = nowtime
