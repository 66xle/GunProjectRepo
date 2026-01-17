from dfpyre import *

Function('FireGun', Parameter('num-WaitForFireModel', ParameterType.NUMBER), codeblocks=[
    IfVariable.ItemHasTag(GameValue('Main Hand Item'), 'id', inverted=True, codeblocks=[
        Control.Return()
    ]),
    IfVariable.Equals(Variable('%default bool-PlayingAnimation'), 1, codeblocks=[
        IfVariable.Equals(Variable('%default bool-IsReloading'), 1, codeblocks=[
            IfVariable.StringMatches(Variable('%default str-ReloadType'), 'bullet', codeblocks=[
                SetVariable.Assign(Variable('%default bool-FinishReloading'), 1),
                Control.Return()
            ]),
            Control.Return()
        ]),
        Control.Return()
    ]),
    CallFunction('GetClipAmmo'),
    IfVariable.LessEqual(Variable('num-CurrentClip', 'local'), 0, codeblocks=[
        CallFunction('Reload'),
        Control.Return()
    ]),
    Repeat.Multiple(Variable('%default num-Bullets'), codeblocks=[
        CallFunction('ShootParticle')
    ]),
    SetVariable.SetCustomSound(Variable('snd-Shoot', 'local'), Sound('Cherry Wood Place', 1.0, 2.0), 'custom.ranged.%var(%default str-GunName).shoot'),
    SetVariable.ShiftOnAxis(Variable('loc-FarSound', 'local'), GameValue('Location'), 0, coordinate='Y'),
    PlayerAction.PlaySound(Variable('snd-Shoot', 'local'), target=Target.DEFAULT),
    SelectObject.PlayersCond('%default', sub_action='PNameEquals', inverted=True),
    SetVariable.SetSoundVolume(Variable('snd-Shoot', 'local'), 0.5),
    PlayerAction.PlaySound(Variable('snd-Shoot', 'local'), Variable('loc-FarSound', 'local')),
    SelectObject.Reset(),
    PlayerAction.SetItemCooldown(Variable('%default item-MainHand'), Variable('%default num-GunRateOfFire'), target=Target.NONE),
    CallFunction('ReduceClip'),
    IfVariable.StringMatches(Variable('%default str-FireType'), 'auto', codeblocks=[
        SetVariable.Assign(Variable('num-Wait', 'local'), Variable('num-WaitForFireModel', 'line')),
        StartProcess('FireModel', local_variables='Copy')
    ]),
    Else([
        CallFunction('AnimModel', 'attack', 2, Variable('%default num-AttackModelDataMax'))
    ])
]).build_and_send()