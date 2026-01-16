from pyreutils import *

loc_Position1 = Var('loc-Position1', 'local')
loc_Position2 = Var('loc-Position2', 'local')
num_Damage = Var('num-Damage', 'line')
num_YShootBullet = Var('num-YShootBullet', 'local')
num_YPos1 = Var('num-YPos1', 'local')
num_YPos2 = Var('num-YPos2', 'local')
num_DealDMG = Var('num-DealDMG', 'local')
num_SetHealth = Var('num-SetHealth', 'local')
loc_Hit = Var('loc-Hit', 'local')

victim_location = GameValue('Location', 'Selection')
victim_health = GameValue('Current Health', 'Selection')

Function('025 DMGPlayer', Parameter('num-Damage', ParameterType.NUMBER), codeblocks=[
    SetVariable.ShiftAllAxes(loc_Position1, victim_location, -0.5, 0, 0.5),
    SetVariable.ShiftAllAxes(loc_Position2, victim_location, 0.5, 1.8, -0.5),
    IfPlayer.IsSneaking(target=Target.SELECTION, codeblocks=[
        SetVariable.ShiftY(loc_Position2, -0.3),
    ]),
    SetVariable.GetCoordY(num_YShootBullet, loc_Hit),
    SetVariable.GetCoordY(num_YPos1, loc_Position1),
    SetVariable.GetCoordY(num_YPos2, loc_Position2),
    IfVariable.InRange(num_YShootBullet, num_YPos1, num_YPos2, codeblocks=[
        SetVariable.Increment(num_YShootBullet, 1.5),
        IfPlayer.IsSneaking(target=Target.SELECTION, codeblocks=[
            SetVariable.ShiftY(loc_Position1, -0.3),
            SetVariable.ShiftY(loc_Position2, -0.3)
        ]),
        SetVariable.Assign(num_DealDMG, num_Damage),
        IfVariable.InRange(num_YShootBullet, num_YPos1, num_YPos2, codeblocks=[
            SetVariable.Multiply(num_DealDMG, [num_Damage, 2.5])
        ]),
        PlayerAction.PlaySound(Sound('Item Frame Add Item', 2.0, 2.0), target=Target.DEFAULT),
        SetVariable.Subtract(num_SetHealth, [victim_health, num_DealDMG]),
        PlayerAction.PlaySound(Sound('Player Hurt', 1.0, 2.0), target=Target.SELECTION),
        PlayerAction.HurtAnimation(target=Target.SELECTION),
        IfVariable.LessEqual(num_SetHealth, 0, codeblocks=[
            SetVariable.Assign(num_SetHealth, 20),
            PlayerAction.SendMessage(Text('<dark_green>%default </dark_green><yellow>killed </yellow><red>%selected'), target=Target.ALL_PLAYERS),
            PlayerAction.SendTitle(Text('<red>'), Text('<gray>[<dark_green> ⚔ </dark_green>]<gray>'), 10, 0, 0, target=Target.DEFAULT),
            PlayerAction.PlaySound(Sound('Experience Orb Pickup', 1.0, 2.0), target=Target.DEFAULT)
        ]),
        PlayerAction.SetHealth(num_SetHealth, target=Target.SELECTION),
        SelectObject.Reset()
    ])
]).build_and_send()