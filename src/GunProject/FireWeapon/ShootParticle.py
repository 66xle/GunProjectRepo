from pyreutils.wrapper import *

# region NOTE
# MANUALLY ADD PARTICLE AFTER BUILDING


# ─── Local Vars ─────────────────────────────────────────────
vec_Direction      = local('vec-Direction')
vec_Shift          = local('vec-Shift')
loc_BulletStart    = local('loc-BulletStart')
loc_RaycastOrigin  = local('loc-RaycastOrigin')
loc_End            = local('loc-End')
loc_EndPoint       = local('loc-EndPoint')
loc_Hit            = local('loc-Hit')

num_Min            = local('num-Min')
num_Random1        = local('num-Random1')
num_Random2        = local('num-Random2')
num_ParticleLength = local('num-ParticleLength')

bool_HitPlayer     = local('bool-HitPlayer')
txt_MobDamage      = local('txt-MobDamage')
txt_Player         = local('txt-Player')
str_Block          = local('str-Block')

# ─── Default (Global) Vars ──────────────────────────────────
def_num_Damage        = game('%default num-Damage')
def_num_Recoil        = game('%default num-Recoil')
def_num_Spread        = game('%default num-Spread')
def_num_AimSpread     = game('%default num-AimSpread')
def_num_IncreaseRec   = game('%default num-IncreaseRecoil')
bool_HitScan          = game('%default bool-HitScan')
def_str_EntityHitUUID = game('%default str-EntityHitUUID')
def_str_PlayerHitUUID = game('%default str-PlayerHitUUID')
def_num_GunDistance   = game('%default num-GunDistance')


with Function('ShootParticle') as f:

    # Bullet direction and starting position
    vec_Direction.v = SetVariable.SetVectorLength(GameValue('Direction'), 1.7)
    vec_Shift.v = SetVariable.RotateAroundAxis(vec_Direction, -25, axis='Y')
    loc_BulletStart.v = SetVariable.ShiftOnVector(GameValue('Eye Location'), vec_Shift)
    loc_BulletStart.v = SetVariable.ShiftOnAxis(loc_BulletStart, -0.5, coordinate='Y')

    loc_RaycastOrigin.v = SetVariable.ShiftOnVector(GameValue('Eye Location'), GameValue('Direction'))
    loc_End.v = SetVariable.ShiftInDirection(loc_RaycastOrigin, 50)

    # Random spread
    num_Min.v = def_num_Recoil * -1
    num_Random1.v = SetVariable.RandomNumber(num_Min, def_num_Recoil, rounding_mode='Decimal number')
    num_Random2.v = SetVariable.RandomNumber(num_Min, def_num_Recoil, rounding_mode='Decimal number')
    loc_End.v = SetVariable.ShiftAllDirections(loc_End, 0, num_Random1, num_Random2)

    SetVariable.FaceLocation(loc_RaycastOrigin, loc_End)

    # HitScan logic
    with IfVariable.Equals(bool_HitScan, 1):
        bool_HitScan.v = 0
        bool_HitPlayer.v = 0

        SelectObject.EntityName(def_str_EntityHitUUID)
        with IfVariable.Equals(GameValue('Selection Size'), 0):
            SelectObject.PlayerName(def_str_PlayerHitUUID)
            bool_HitPlayer.v = 1

        num_ParticleLength.v = SetVariable.Distance(loc_RaycastOrigin, GameValue('Midpoint Location', 'Selection'))
        loc_EndPoint.v = SetVariable.ShiftInDirection(loc_RaycastOrigin, num_ParticleLength)
        loc_Hit.v = loc_EndPoint

        with IfVariable.Equals(bool_HitPlayer, 0):
            CallFunction('026 DMGMob', (def_num_Damage))
        with Else():
            Control.PrintDebug([Text('%selected updated loc'), GameValue('Location', 'Selection')])
            CallFunction('025 DMGPlayer', (def_num_Damage))

        PlayerAction.ParticleLineA(
            #Particle.Trail(1, 0.0, 0.0, color=(175, 155, 96), color_variation=0),
            loc_BulletStart, loc_EndPoint, 0.1, 5, target=Target.ALL_PLAYERS
        )

    # Non-hitScan logic
    with Else():
        # Damage mobs
        SelectObject.AllEntities()
        SelectObject.FilterRay(loc_Hit, loc_RaycastOrigin, def_num_GunDistance)
        SelectObject.Reset()
        str_Block.v = SetVariable.GetBlockType(loc_Hit)

        with IfVariable.StringMatches(str_Block, 'air'):
            SelectObject.AllEntities()
            SelectObject.FilterDistance(loc_Hit, 1.5)
            txt_MobDamage.v = GameValue('Selection Target UUIDs')
            with IfVariable.NotEqual(txt_MobDamage, 0):
                CallFunction('026 DMGMob', (def_num_Damage))
            SelectObject.Reset()

        # Damage players
        SelectObject.PlayerName('%default')
        SelectObject.FilterRay(loc_Hit, loc_RaycastOrigin, def_num_GunDistance)
        SelectObject.Reset()
        str_Block.v = SetVariable.GetBlockType(loc_Hit)

        with IfVariable.StringMatches(str_Block, 'air'):
            SelectObject.AllPlayers()
            SelectObject.FilterDistance(loc_Hit, 1.5)
            txt_Player.v = GameValue('Selection Target UUIDs')
            with IfVariable.NotEqual(txt_Player, 0):
                CallFunction('025 DMGPlayer', (def_num_Damage))
            SelectObject.Reset()

        with IfGame.InBlock(loc_Hit):
            StartProcess('BulletHole', tags={'Local Variables':'Copy'})

        PlayerAction.ParticleLineA(
            #Particle.Trail(1, 0.0, 0.0, color=(175, 155, 96), color_variation=0),
            loc_BulletStart, loc_Hit, 0.1, 5, target=Target.ALL_PLAYERS
        )

    # Recoil handling
    with IfPlayer.IsSneaking():
        with IfVariable.GreaterThan(def_num_Recoil, def_num_AimSpread):
            SetVariable.Decrement(def_num_Recoil, def_num_IncreaseRec)
            SetVariable.ClampNumber(def_num_Recoil, def_num_Recoil, def_num_AimSpread, 100)
            Control.Return()

    SetVariable.Increment(def_num_Recoil, def_num_IncreaseRec)
    SetVariable.ClampNumber(def_num_Recoil, 0, def_num_Spread)

f.build_and_send()
