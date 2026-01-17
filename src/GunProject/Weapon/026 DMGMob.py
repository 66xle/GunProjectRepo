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

mob_location  = GameValue.Location(Target.SELECTION)
mob_health    = GameValue.CurrentHealth(Target.SELECTION)

with Function('026 DMGMob', Parameter('num-Damage', ParameterType.NUMBER)) as f:
    loc_Position1.v = SetV.ShiftAllAxes(mob_location, -0.5, 0, 0.5)
    loc_Position2.v = SetV.ShiftAllAxes(mob_location, 0.5, 2, -0.5)
    num_YMob.v      = SetV.GetCoordY(loc_Hit)
    num_YMobPos1.v  = SetV.GetCoordY(loc_Position1)
    num_YMobPos2.v  = SetV.GetCoordY(loc_Position2)

    with If.InRange(num_YMob, num_YMobPos1, num_YMobPos2):
        num_YMobPos1.v += 1.5
        num_DMGDealt.v = num_Damage

        with If.InRange(num_YMob, num_YMobPos1, num_YMobPos2):
            num_DMGDealt.v *= 2.5

        Player.PlaySound(Sound('Item Frame Add Item', 2.0, 2.0), target=Target.DEFAULT)
        Player.SendMessage(Text('hit'), target=Target.DEFAULT)
        Entity.Damage(num_DMGDealt, target=Target.SELECTION)
        Entity.SetInvulTicks(0, target=Target.SELECTION)
        num_Health.v = mob_health
        Entity.SetName(Text('%var(num-Health)'), target=Target.SELECTION)

        with If.LessEqual(mob_health, 100):
            Entity.Remove()

        Select.Reset()

f.build_and_send()
