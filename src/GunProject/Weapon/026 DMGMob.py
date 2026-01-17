from pyreutils.wrapper import *

loc_Position1 = local('loc-Position1')
loc_Position2 = local('loc-Position2')
num_YMob      = local('num-YMob')
num_YMobPos1  = local('num-YMobPos1')
num_YMobPos2  = local('num-YMobPos2')
num_DMGDealt  = local('num-DMGDealt')
num_Damage    = line('num-Damage')
num_Health    = local('num-Health')
loc_Hit       = local('loc-Hit')
loc_ShootBullet = local('loc-ShootBullet')

mob_location  = GameValue('Location', 'Selection')
mob_health    = GameValue('Current Health', 'Selection')

with Function('026 DMGMob', Parameter('num-Damage', ParameterType.NUMBER)) as f:
    loc_Position1.v = SetVariable.ShiftAllAxes(mob_location, -0.5, 0, 0.5)
    loc_Position2.v = SetVariable.ShiftAllAxes(mob_location, 0.5, 2, -0.5)
    num_YMob.v      = SetVariable.GetCoordY(loc_Hit)
    num_YMobPos1.v  = SetVariable.GetCoordY(loc_Position1)
    num_YMobPos2.v  = SetVariable.GetCoordY(loc_Position2)

    with If.InRange(num_YMob, num_YMobPos1, num_YMobPos2):
        num_YMobPos1.v += 1.5
        num_DMGDealt.v = num_Damage

        with If.InRange(num_YMob, num_YMobPos1, num_YMobPos2):
            num_DMGDealt.v *= 2.5

        PlayerAction.PlaySound(Sound('Item Frame Add Item', 2.0, 2.0), target=Target.DEFAULT)
        PlayerAction.SendMessage(Text('hit'), target=Target.DEFAULT)
        EntityAction.Damage(num_DMGDealt, target=Target.SELECTION)
        EntityAction.SetInvulTicks(0, target=Target.SELECTION)
        num_Health.v = mob_health
        EntityAction.SetName(Text('%var(num-Health)'), target=Target.SELECTION)

        with If.LessEqual(mob_health, 100):
            EntityAction.Remove()

        SelectObject.Reset()

f.build_and_send()
