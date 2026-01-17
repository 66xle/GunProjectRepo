from pyreutils.wrapper import *

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
    SetVariable.GetCoord(num_Pitch, loc_Hit, coordinate='Pitch')
    SetVariable.GetCoord(num_Yaw, loc_Hit, coordinate='Yaw')

    with IfVariable.Equals(num_Pitch, 0):
        SetVariable.AlignLoc(loc_CenterXZ, loc_Hit, coordinates='X and Z')

        with IfVariable.Equals(num_Yaw, [90, -90]):
            SetVariable.GetCoord(num_X, loc_CenterXZ)
            SetVariable.SetCoord(loc_Hit, num_X)
        with Else():
            SetVariable.GetCoord(num_Z, loc_CenterXZ, coordinate='Z')
            SetVariable.SetCoord(loc_Hit, num_Z, coordinate='Z')

    with Else():
        SetVariable.AlignLoc(loc_Hit, coordinates='Only Y')

    # Shift block slightly in direction
    SetVariable.ShiftInDirection(loc_Hit, 0.501)

    # Spawn the bullet block
    GameAction.SpawnBlockDisp(loc_Hit, Item('black_concrete'))

    # Adjust entity display scale and translation based on orientation
    with IfVariable.Equals(num_Pitch, 0):
        with IfVariable.Equals(num_Yaw, [90, -90]):
            EntityAction.DisplayScale(0.001, 0.075, 0.075)
            EntityAction.DispTranslation(0, -0.0375, -0.0375)
        with Else():
            EntityAction.DisplayScale(0.075, 0.075, 0.001)
            EntityAction.DispTranslation(-0.0375, -0.0375, 0)
    with Else():
        EntityAction.DisplayScale(0.075, 0.001, 0.075)
        EntityAction.DispTranslation(-0.0375, 0, -0.0375)

    # Store UUID for removal later
    SetVariable.Assign(str_BulletUUID, GameValue('UUID', 'LastEntity'))

    Control.Wait(5, time_unit='Seconds')

    # Remove bullet entity
    SelectObject.EntityName(str_BulletUUID)
    EntityAction.Remove()

p.build_and_send()
