# -*- coding: utf-8 -*-

from ...internal import ServerComp, ServerLevelId


_getRecipesByInput = ServerComp.CreateRecipe(ServerLevelId).GetRecipesByInput

def GetRecipesByInput(item_id, recipe_tag, aux_value=0, maxResultNum=-1):
    # type: (str, str, int, int) -> list[dict]
    return _getRecipesByInput(item_id, recipe_tag, aux_value, maxResultNum)


__all__ = [
    'GetRecipesByInput'
]
