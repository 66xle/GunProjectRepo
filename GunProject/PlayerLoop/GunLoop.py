from dfpyre import *


# numeric
default_numGunCooldown = Variable("%default num-GunCooldown")
default_numRecoil = Variable("%default num-Recoil")
default_numSpread = Variable("%default num-Spread")
default_numAimSpread = Variable("%default num-AimSpread")

# bool
default_boolFirstShot = Variable("%default bool-FirstShot")

# string
default_strType = Variable("%default str-Type")

# item
default_itemMainHand = Variable("%default item-MainHand")   

item_EnderEye = Item("ender_eye")

Function("GunLoop", codeblocks=[
    SetVariable.Decrement(default_numGunCooldown, 1),

    IfPlayer.IsUsingItem(item_EnderEye, codeblocks=[
        IfPlayer.NoItemCooldown(default_itemMainHand, codeblocks=[
            IfVariable.Equals(default_boolFirstShot, 1, codeblocks=[
                CallFunction("FireGun", 1)
            ])
        ])
    ]),
    Else([
        SetVariable.Assign(default_boolFirstShot, 0),
        SetVariable.Decrement(default_numRecoil, 0.3),
        SetVariable.ClampNumber(default_numRecoil, 0, 100)
    ]),

    IfVariable.StringMatches(
        default_strType,
        ["shotgun", "sniper"],
        codeblocks=[
            SetVariable.Assign(default_numRecoil, default_numSpread),
            IfPlayer.IsSneaking(codeblocks=[
                SetVariable.Assign(default_numRecoil, default_numAimSpread)
            ])
        ]
    )
]).build_and_send()

