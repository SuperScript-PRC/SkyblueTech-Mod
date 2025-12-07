from skybluetech_scripts.tooldelta.ui.elem_comp import UBaseUI
from skybluetech_scripts.tooldelta.api.client.item import GetItemHoverName
from ..utils.fmt import FormatRF as _formatRF, FormatFluidVolume as _formatFluidVolume
from ..define.fluids import texture as fluid_texture
from ..ui_sync.machines.basic_machine_ui_sync import FluidSlotSync

# TYPE_CHECKING
if 0:
    from typing import Callable, TypeVar
    T = TypeVar("T")
    BtnCb = Callable[[], T]
# TYPE_CHECKING END

INFINITY = float("inf")

def UpdatePowerBar(ui, rf_now, rf_max):
    # type: (UBaseUI, int, int) -> None
    if rf_max <= 0:
        return
    top = ui["bar/mask"]
    label = ui["label"]
    top.SetFullSize("y", {"followType": "parent", "relativeValue": min(2, float(rf_now) / rf_max)})
    label.AsLabel().SetText(_formatRF(rf_now))

def UpdateFlame(ui, percent):
    # type: (UBaseUI, float) -> None
    ui["mask"].AsImage().SetSpriteClipRatio("fromTopToBottom", 1 - percent)

def UpdateGenericProgressL2R(ui, percent):
    # type: (UBaseUI, float) -> None
    ui["mask"].AsImage().SetSpriteClipRatio("fromRightToLeft", 1 - percent)

def UpdateFluidDisplay(ui, fluid_id, fluid_volume, max_volume):
    # type: (UBaseUI, str | None, float, float) -> None
    fluid_img = ui["fluid"].AsImage()
    volume_disp = ui["text"].AsLabel()
    if fluid_id is None:
        fluid_img.SetFullSize("y", {"followType": "parent", "relativeValue": 0})
    else:
        texture, color = fluid_texture.getBaseTexture(fluid_id)
        texture_path = texture
        fluid_img.SetSprite(texture_path)
        if color is not None:
            r, g, b = color
            color = (float(r) / 255, float(g) / 255, float(b) / 255)
            fluid_img.SetSpriteColor(color)
    if fluid_volume == INFINITY:
        prgs = 1
    elif max_volume == INFINITY:
        prgs = 0
    else:
        prgs = float(fluid_volume) / max_volume
    volume_disp.SetText("%s / %s" % (_formatFluidVolume(fluid_volume), _formatFluidVolume(max_volume)))
    fluid_img.SetFullSize("y", {"followType": "parent", "relativeValue": min(2, prgs)})

def InitFluidDisplay(ui, data_cb):
    # type: (UBaseUI, BtnCb[tuple[str | None, float, float]]) -> Callable[[], None]
    btn = ui["data_btn"].AsButton()
    _databoard = [None] # type: list[UBaseUI | None]
    _opened = [False]
    def _updateHook():
        elem = _databoard[0]
        if elem is None:
            return
        fluid_id, fluid_vol, max_vol = data_cb()
        (elem / "image/label").AsLabel().SetText(
            "§d流体类型： §f"
            + ((GetItemHoverName(fluid_id) or fluid_id) if fluid_id is not None and fluid_id != "加载中.." else "空")
            + "\n"
            + "§a体积： §f"
            + _formatFluidVolume(fluid_vol)
            + "\n"
            + "§6容器体积： §f"
            + _formatFluidVolume(max_vol)
        )
    def onRollOver(params):
        if _opened[0]:
            return
        prev_board = ui._vars.get("disp_fluid_databoard")
        if prev_board is not None:
            prev_board.Remove()
        if _databoard[0] is not None:
            return
        e = ui.AddElement("BasicDataScreen.DataTextScreen", "fluid_hover_text")
        e.SetLayer(100)
        _databoard[0] = e
        _opened[0] = True
        ui._vars["disp_fluid_databoard"] = e
        _updateHook()
    def onRollOut(params):
        if _databoard[0] is not None:
            ok = _databoard[0].Remove()
            if not ok:
                print("[WARNING] element remove failed")
            _databoard[0] = None
            ui._vars["disp_fluid_databoard"] = None
            _opened[0] = False
    btn.SetOnRollOverCallback(onRollOver)
    btn.SetOnRollOutCallback(onRollOut)
    return _updateHook


def InitFluidsDisplay(ui, fluid_slots, index):
    # type: (UBaseUI, list[FluidSlotSync], int) -> Callable[[], None]
    def get_data():
        if len(fluid_slots) == 0:
            fluid_id = "加载中.."
            fluid_volume = 0
            max_volume = 0
        elif len(fluid_slots) <= index:
            fluid_id = None
            fluid_volume = -128
            max_volume = -128
        else:
            fluid = fluid_slots[index]
            fluid_id = fluid.fluid_id
            fluid_volume = fluid.volume
            max_volume = fluid.max_volume
        return fluid_id, fluid_volume, max_volume
    return InitFluidDisplay(ui, get_data)