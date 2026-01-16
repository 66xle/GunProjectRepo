from dfpyre import *

Function('SwapWeapon', Parameter('bool-InitWeapon', ParameterType.NUMBER, optional=True, default_value=0, slot=0), codeblocks=[
    SetVariable.Assign(Variable('num-HotBarSlot', 'local', slot=0), GameValue('Event Hotbar Slot', slot=1)),
    IfVariable.Equals(Variable('bool-InitWeapon', 'line', slot=0), Number(1, slot=1), codeblocks=[
        SetVariable.Assign(Variable('num-HotBarSlot', 'local', slot=0), Number(1, slot=1))
    ]),
    IfVariable.Equals(Variable('%default bool-PlayingAnimation', slot=0), Number(1, slot=1), codeblocks=[
        SetVariable.Assign(Variable('%default bool-CancelAnimation', slot=0), Number(1, slot=1), Variable('num-HotBarSlot', 'local', slot=2)),
        Repeat.While(Variable('%default bool-PlayingAnimation', slot=0), Number(1, slot=1), sub_action='=', codeblocks=[
            Control.Wait()
        ])
    ]),
    Control.Wait(),
    SetVariable.GetListValue(Variable('item-MainHand', 'local', slot=0), GameValue('Hotbar Items', slot=1), Variable('num-HotBarSlot', 'local', slot=2)),
    IfVariable.ItemHasTag(Variable('item-MainHand', 'local', slot=0), String('id', slot=1), inverted=True, codeblocks=[
        Control.Return()
    ]),
    SetVariable.Assign(Variable('%default num-Recoil', slot=0), Number(0, slot=1)),
    SetVariable.SetModelDataNums(Variable('%default item-MainHand', slot=0), Number(1, slot=1)),
    PlayerAction.SetSlotItem(Variable('%default item-MainHand', slot=0), Variable('%default num-HotbarSlot', slot=1)),
    SetVariable.Assign(Variable('%default item-MainHand', slot=0), Variable('item-MainHand', 'local', slot=1)),
    SetVariable.Assign(Variable('%default num-HotbarSlot', slot=0), GameValue('Event Hotbar Slot', slot=1)),
    SetVariable.GetAllItemTags(Variable('dict-GunTag', 'local', slot=0), Variable('%default item-MainHand', slot=1)),
    SetVariable.GetDictValue(Variable('%default num-GunID', slot=0), Variable('dict-GunTag', 'local', slot=1), String('id', slot=2)),
    SetVariable.GetDictValue(Variable('%default num-GunRateOfFire', slot=0), Variable('dict-GunTag', 'local', slot=1), String('rof', slot=2)),
    SetVariable.GetDictValue(Variable('%default num-GunDistance', slot=0), Variable('dict-GunTag', 'local', slot=1), String('dist', slot=2)),
    SetVariable.GetDictValue(Variable('%default num-Spread', slot=0), Variable('dict-GunTag', 'local', slot=1), String('max_spread', slot=2)),
    SetVariable.GetDictValue(Variable('%default num-AimSpread', slot=0), Variable('dict-GunTag', 'local', slot=1), String('aim_spread', slot=2)),
    SetVariable.GetDictValue(Variable('num-RecoilTime', 'local', slot=0), Variable('dict-GunTag', 'local', slot=1), String('recoil_time', slot=2)),
    SetVariable.Assign(Variable('%default num-AimRecoil', slot=0), Number('%math(%var(%default num-AimSpread) / %math(%var(num-RecoilTime) * 20))', slot=1)),
    SetVariable.Assign(Variable('%default num-HipRecoil', slot=0), Number('%math(%var(%default num-Spread) / %math(%var(num-RecoilTime) * 20))', slot=1)),
    SetVariable.Assign(Variable('%default num-IncreaseRecoil', slot=0), Variable('%default num-HipRecoil', slot=1)),
    SetVariable.GetDictValue(Variable('%default str-GunName', slot=0), Variable('dict-GunTag', 'local', slot=1), String('name', slot=2)),
    SetVariable.GetDictValue(Variable('%default num-Damage', slot=0), Variable('dict-GunTag', 'local', slot=1), String('damage', slot=2)),
    SetVariable.GetDictValue(Variable('%default num-ReloadModelDataMax', slot=0), Variable('dict-GunTag', 'local', slot=1), String('reload_modeldata_max', slot=2)),
    SetVariable.GetDictValue(Variable('%default num-AttackModelDataMax', slot=0), Variable('dict-GunTag', 'local', slot=1), String('attack_modeldata_max', slot=2)),
    SetVariable.GetDictValue(Variable('%default num-Bullets', slot=0), Variable('dict-GunTag', 'local', slot=1), String('bullets', slot=2)),
    SetVariable.GetDictValue(Variable('%default str-Type', slot=0), Variable('dict-GunTag', 'local', slot=1), String('type', slot=2)),
    SetVariable.GetDictValue(Variable('%default str-FireType', slot=0), Variable('dict-GunTag', 'local', slot=1), String('fire_type', slot=2)),
    SetVariable.GetDictValue(Variable('%default str-ReloadType', slot=0), Variable('dict-GunTag', 'local', slot=1), String('reload_type', slot=2)),
    SetVariable.GetDictValue(Variable('%default num-ReloadLoopStart', slot=0), Variable('dict-GunTag', 'local', slot=1), String('reload_loop_start', slot=2)),
    SetVariable.GetDictValue(Variable('%default num-ReloadLoopEnd', slot=0), Variable('dict-GunTag', 'local', slot=1), String('reload_loop_end', slot=2)),
    PlayerAction.SetEquipment(Item('ender_eye', slot=0), equipment_slot='Off hand'),
    IfVariable.StringMatches(Variable('%default str-Type', slot=0), String('sniper', slot=1), codeblocks=[
        PlayerAction.ClearItems(Item('ender_eye', slot=0))
    ])
]).build_and_send()