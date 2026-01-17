from pyreutils.wrapper import *

item_Weapon     = local('item-Weapon')
num_Clip        = local('num-Clip')
num_Ammo        = local('num-Ammo')
num_ID          = local('num-ID')
dict_CurrentClip = local('dict-CurrentClip')
dict_MaxAmmo     = local('dict-MaxAmmo')

list_Weapons = Variable('list-Weapons')

with Function('GenID') as f:
    with Repeat.ForEach(item_Weapon, list_Weapons):
        Control.Wait(Number(0))
        num_Clip.v = SetVariable.GetItemTag(item_Weapon, String('clip'))
        num_Ammo.v = SetVariable.GetItemTag(item_Weapon, String('ammo'))
        num_ID.v  += 1
        SetVariable.SetDictValue(dict_CurrentClip, String('%var(num-ID)'), num_Clip)
        SetVariable.SetDictValue(dict_MaxAmmo, String('%var(num-ID)'), num_Ammo)
        SetVariable.SetItemTag(item_Weapon, String('id'), num_ID)

f.build_and_send()
