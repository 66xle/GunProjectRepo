from pyreutils.wrapper import *

# ─── Local Vars ─────────────────────────────────────────────
num_ID         = local('num-ID')
num_CurrentClip = local('num-CurrentClip')
num_CurrentAmmo = local('num-CurrentAmmo')

dict_CurrentClip = local('dict-CurrentClip')
dict_MaxAmmo = local('dict-MaxAmmo')

with Function('GetClipAmmo') as f:

    # Get weapon ID from main hand item
    num_ID.v = SetV.GetItemTag('%default item-MainHand', 'id')

    # Get current clip and max ammo from dicts using weapon ID
    num_CurrentClip.v = SetV.GetDictValue(dict_CurrentClip, '%var(num-ID)')
    num_CurrentAmmo.v = SetV.GetDictValue(dict_MaxAmmo, '%var(num-ID)')

f.build_and_send()
