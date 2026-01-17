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
    vec_Direction.v = SetV.SetVectorLength(GameValue.Direction(), 1.7)
    vec_Shift.v = SetV.RotateAroundAxisY(vec_Direction, -25)
    loc_BulletStart.v = SetV.ShiftOnVector(GameValue.EyeLocation(), vec_Shift)
    loc_BulletStart.v = SetV.ShiftY(loc_BulletStart, -0.5)

    loc_RaycastOrigin.v = SetV.ShiftOnVector(GameValue.EyeLocation(), GameValue.Direction())
    loc_End.v = SetV.ShiftInDirection(loc_RaycastOrigin, 50)

    # Random spread
    num_Min.v = def_num_Recoil * -1
    num_Random1.v = SetV.RandomNumber(num_Min, def_num_Recoil, rounding_mode='Decimal number')
    num_Random2.v = SetV.RandomNumber(num_Min, def_num_Recoil, rounding_mode='Decimal number')
    loc_End.v = SetV.ShiftAllDirections(loc_End, 0, num_Random1, num_Random2)

    loc_RaycastOrigin.v = SetV.FaceLocation(loc_End)

    # HitScan logic
    with If.Equals(bool_HitScan, 1):
        bool_HitScan.v = 0
        bool_HitPlayer.v = 0

        Select.EntityName(def_str_EntityHitUUID)
        with If.Equals(GameValue.SelectionSize(), 0):
            Select.PlayerName(def_str_PlayerHitUUID)
            bool_HitPlayer.v = 1

        num_ParticleLength.v = SetV.Distance(loc_RaycastOrigin, GameValue.MidpointLocation(Target.SELECTION))
        loc_EndPoint.v = SetV.ShiftInDirection(loc_RaycastOrigin, num_ParticleLength)
        loc_Hit.v = loc_EndPoint

        with If.Equals(bool_HitPlayer, 0):
            CallFunction('026 DMGMob', (def_num_Damage))
        with Else():
            Control.PrintDebug([Text('%selected updated loc'), GameValue.Location(Target.SELECTION)])
            CallFunction('025 DMGPlayer', (def_num_Damage))

        Player.ParticleLineA(
            #Particle.Trail(1, 0.0, 0.0, color=(175, 155, 96), color_variation=0),
            loc_BulletStart, loc_EndPoint, 0.1, 5, target=Target.ALL_PLAYERS
        )

    # Non-hitScan logic
    with Else():
        # Damage mobs
        Select.AllEntities()
        Select.FilterRay(loc_Hit, loc_RaycastOrigin, def_num_GunDistance)
        Select.Reset()
        str_Block.v = SetV.GetBlockType(loc_Hit)

        with If.StringMatches(str_Block, 'air'):
            Select.AllEntities()
            Select.FilterDistance(loc_Hit, 1.5)
            txt_MobDamage.v = GameValue.SelectionTargetUUIDs()
            with If.NotEqual(txt_MobDamage, 0):
                CallFunction('026 DMGMob', (def_num_Damage))
            Select.Reset()

        # Damage players
        Select.PlayerName('%default')
        Select.FilterRay(loc_Hit, loc_RaycastOrigin, def_num_GunDistance)
        Select.Reset()
        str_Block.v = SetV.GetBlockType(loc_Hit)

        with If.StringMatches(str_Block, 'air'):
            Select.AllPlayers()
            Select.FilterDistance(loc_Hit, 1.5)
            txt_Player.v = GameValue.SelectionTargetUUIDs()
            with If.NotEqual(txt_Player, 0):
                CallFunction('025 DMGPlayer', (def_num_Damage))
            Select.Reset()

        with IfGame.InBlock(loc_Hit):
            StartProcess('BulletHole', tags={'Local Variables':'Copy'})

        Player.ParticleLineA(
            #Particle.Trail(1, 0.0, 0.0, color=(175, 155, 96), color_variation=0),
            loc_BulletStart, loc_Hit, 0.1, 5, target=Target.ALL_PLAYERS
        )

    # Recoil handling
    with IfPlayer.IsSneaking():
        with If.GreaterThan(def_num_Recoil, def_num_AimSpread):
            def_num_Recoil.v -= def_num_IncreaseRec
            def_num_Recoil.v = SetV.ClampNumber(def_num_Recoil, def_num_AimSpread, 100)
            Control.Return()

    def_num_Recoil.v += def_num_IncreaseRec
    def_num_Recoil.v = SetV.ClampNumber(0, def_num_Spread)

f.build_and_send()
