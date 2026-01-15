from dfpyre import *

Function('GenID', codeblocks=[
    Repeat.ForEach(Variable('item-Weapon', 'local', slot=0), Variable('list-Weapons', slot=1), codeblocks=[
        Control.Wait(Number(0, slot=0)),
        SetVariable.GetItemTag(Variable('num-Clip', 'local', slot=0), Variable('item-Weapon', 'local', slot=1), String('clip', slot=2)),
        SetVariable.GetItemTag(Variable('num-Ammo', 'local', slot=0), Variable('item-Weapon', 'local', slot=1), String('ammo', slot=2)),
        SetVariable.Increment(Variable('num-ID', slot=0), Number(1, slot=1)),
        SetVariable.SetDictValue(Variable('dict-CurrentClip', slot=0), String('%var(num-ID)', slot=1), Variable('num-Clip', 'local', slot=2)),
        SetVariable.SetDictValue(Variable('dict-MaxAmmo', slot=0), String('%var(num-ID)', slot=1), Variable('num-Ammo', 'local', slot=2)),
        SetVariable.SetItemTag(Variable('item-Weapon', 'local', slot=0), String('id', slot=1), Variable('num-ID', slot=2))
    ])
]).build_and_send()