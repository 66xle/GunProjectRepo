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
    str_Sounds.v = SetV.GetItemTag(def_item_MainHand, '%var(str-Type)_sounds')
    str_ModelData.v = SetV.GetItemTag(def_item_MainHand, '%var(str-Type)_modeldata')

    # Split strings into lists
    list_Sounds.v = SetV.SplitString(str_Sounds, '-')
    list_ModelData.v = SetV.SplitString(str_ModelData, '-')

f.build_and_send()
