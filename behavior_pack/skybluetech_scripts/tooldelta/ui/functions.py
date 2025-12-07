from ..no_runtime_typing import TYPE_CHECKING

# TYPE_CHECKING
if TYPE_CHECKING:
    from mod.client.ui.screenNode import ScreenNode
    from mod.client.ui.controls.baseUIControl import BaseUIControl
# TYPE_CHECKING END

def addElement(screen, element_def_name, element_name, parent, force_update=True):
    # type: (ScreenNode, str, str, BaseUIControl, bool) -> BaseUIControl
    return screen.CreateChildControl(element_def_name, element_name, parent, force_update)

def removeElement(screen, element):
    # type: (ScreenNode, BaseUIControl) -> bool
    return screen.RemoveChildControl(element)
