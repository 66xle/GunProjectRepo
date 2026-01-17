from pyreutils.wrapper import *

BULLET_SCALE = 0.075
BULLET_3D_SCALE = 0.001

# ─── Local Vars ─────────────────────────────────────────────
num_Pitch   = local('num-Pitch')
num_Yaw     = local('num-Yaw')
num_X       = local('num-X')
num_Z       = local('num-Z')
loc_Hit     = local('loc-Hit')
loc_CenterXZ = local('loc-CenterXZ')
str_BulletUUID = local('str-BulletUUID')

with Process('BulletHole') as p:
    # Get hit orientation
    num_Pitch.v = SetV.GetPitch(loc_Hit)
    num_Yaw.v = SetV.GetYaw(loc_Hit)

    with If.Equals(num_Pitch, 0):
        loc_CenterXZ.v = SetV.AlignXZ(loc_Hit)

        with If.Equals(num_Yaw, [90, -90]):
            num_X.v = SetV.GetCoordX(loc_CenterXZ)
            loc_Hit.v = SetV.SetCoordX(loc_Hit, num_X)
        with Else():
            num_Z.v = SetV.GetCoordZ(loc_CenterXZ)
            loc_Hit.v = SetV.SetCoordZ(loc_Hit, num_Z)

    with Else():
        loc_Hit.v = SetV.AlignY(loc_Hit)

    # Shift block slightly in direction
    loc_Hit.v = SetV.ShiftInDirection(loc_Hit, 0.501)

    # Spawn the bullet block
    Game.SpawnBlockDisp(loc_Hit, Item('black_concrete'))

    # Adjust entity display scale and translation based on orientation
    with If.Equals(num_Pitch, 0):
        with If.Equals(num_Yaw, [90, -90]):
            Entity.DisplayScale(BULLET_3D_SCALE, BULLET_SCALE, BULLET_SCALE)
            Entity.DispTranslation(0, -BULLET_SCALE/2, -BULLET_SCALE/2)
        with Else():
            Entity.DisplayScale(BULLET_SCALE, BULLET_SCALE, BULLET_3D_SCALE)
            Entity.DispTranslation(-BULLET_SCALE/2, -BULLET_SCALE/2, 0)
    with Else():
        Entity.DisplayScale(BULLET_SCALE, BULLET_3D_SCALE, BULLET_SCALE)
        Entity.DispTranslation(-BULLET_SCALE/2, 0, -BULLET_SCALE/2)

    # Store UUID for removal later
    str_BulletUUID.v = GameValue.UUID(Target.LAST_ENTITY)

    Control.WaitSeconds(5)

    # Remove bullet entity
    Select.EntityName(str_BulletUUID)
    Entity.Remove()

p.build_and_send()
