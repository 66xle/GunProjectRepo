from pyreutils.wrapper import *

loc_Position1    = local('loc-Position1')
loc_Position2    = local('loc-Position2')
num_Damage       = line('num-Damage')
num_YShootBullet = local('num-YShootBullet')
num_YPos1        = local('num-YPos1')
num_YPos2        = local('num-YPos2')
num_DealDMG      = local('num-DealDMG')
num_SetHealth    = local('num-SetHealth')
loc_Hit          = local('loc-Hit')

victim_location  = GameValue.Location(Target.SELECTION)
victim_health    = GameValue.CurrentHealth(Target.SELECTION)

with Function('025 DMGPlayer', Parameter('num-Damage', ParameterType.NUMBER)) as f:
    loc_Position1.v = SetVariable.ShiftAllAxes(victim_location, -0.5, 0, 0.5)
    loc_Position2.v = SetVariable.ShiftAllAxes(victim_location, 0.5, 1.8, -0.5)

    with IfPlayer.IsSneaking(target=Target.SELECTION):
        loc_Position2.v = SetVariable.ShiftY(-0.3)

    num_YShootBullet.v = SetVariable.GetCoordY(loc_Hit)
    num_YPos1.v = SetVariable.GetCoordY(loc_Position1)
    num_YPos2.v = SetVariable.GetCoordY(loc_Position2)

    with IfVariable.InRange(num_YShootBullet, num_YPos1, num_YPos2):

        num_YShootBullet.v += 1.5

        with IfPlayer.IsSneaking(target=Target.SELECTION):
            loc_Position1.v = SetVariable.ShiftY(-0.3)
            loc_Position2.v = SetVariable.ShiftY(-0.3)

        num_DealDMG.v = num_Damage

        with IfVariable.InRange(num_YShootBullet, num_YPos1, num_YPos2):
            num_DealDMG.v *= 2.5

        PlayerAction.PlaySound(Sound('Item Frame Add Item', 2.0, 2.0), target=Target.DEFAULT)
        num_SetHealth.v = victim_health - num_DealDMG
        PlayerAction.PlaySound(Sound('Player Hurt', 1.0, 2.0), target=Target.SELECTION)
        PlayerAction.HurtAnimation(target=Target.SELECTION)

        with IfVariable.LessEqual(num_SetHealth, 0):
            num_SetHealth.v = 20
            PlayerAction.SendMessage(Text('<dark_green>%default </dark_green><yellow>killed </yellow><red>%selected'), target=Target.ALL_PLAYERS)
            PlayerAction.SendTitle(Text('<red>'), Text('<gray>[<dark_green> ⚔ </dark_green>]<gray>'), 10, 0, 0, target=Target.DEFAULT)
            PlayerAction.PlaySound(Sound('Experience Orb Pickup', 1.0, 2.0), target=Target.DEFAULT)
            
        PlayerAction.SetHealth(num_SetHealth, target=Target.SELECTION)
        SelectObject.Reset()
    
f.build_and_send()