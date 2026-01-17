from pyreutils.wrapper import *

# ─── Local Vars ─────────────────────────────────────────────
str_Sounds     = local('str-Sounds')
str_ModelData  = local('str-ModelData')
list_Sounds    = local('list-Sounds')
list_ModelData = local('list-ModelData')

# ─── Game Vars ──────────────────────────────────────────────
def_item_MainHand = game('%default item-MainHand')

with Function('GetSounds', Parameter('str-Type', ParameterType.STRING)) as f:

    # Get sounds and model data from main hand item
    SetVariable.GetItemTag(str_Sounds, def_item_MainHand, '%var(str-Type)_sounds')
    SetVariable.GetItemTag(str_ModelData, def_item_MainHand, '%var(str-Type)_modeldata')

    # Split strings into lists
    SetVariable.SplitString(list_Sounds, str_Sounds, '-')
    SetVariable.SplitString(list_ModelData, str_ModelData, '-')

f.build_and_send()
