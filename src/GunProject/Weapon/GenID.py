from pyreutils.wrapper import *

item_Weapon      = local('item-Weapon')
num_Clip         = local('num-Clip')
num_Ammo         = local('num-Ammo')
num_ID           = local('num-ID')
dict_CurrentClip = local('dict-CurrentClip')
dict_MaxAmmo     = local('dict-MaxAmmo')

list_Weapons = game('list-Weapons')

with Function('GenID') as f:
    with Repeat.ForEach(item_Weapon, list_Weapons):
        Control.Wait(0)
        num_Clip.v = SetV.GetItemTag(item_Weapon, 'clip')
        num_Ammo.v = SetV.GetItemTag(item_Weapon, 'ammo')
        num_ID.v += 1
        dict_CurrentClip.v = SetV.SetDictValue('%var(num-ID)', num_Clip)
        dict_MaxAmmo.v = SetV.SetDictValue('%var(num-ID)', num_Ammo)
        item_Weapon.v = SetV.SetItemTag('id', num_ID)

f.build_and_send()
