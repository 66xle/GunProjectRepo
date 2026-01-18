from pyreutils.wrapper import *

# ─── Default (Global) Vars ──────────────────────────────────
def_num_Damage        = game('%default num-Damage')
def_num_Recoil        = game('%default num-Recoil')
def_num_Spread        = game('%default num-Spread')
def_num_AimSpread     = game('%default num-AimSpread')
def_num_IncreaseRec   = game('%default num-IncreaseRecoil')
def_bool_HitScan      = game('%default bool-HitScan')
def_str_EntityHitUUID = game('%default str-EntityHitUUID')
def_str_PlayerHitUUID = game('%default str-PlayerHitUUID')
def_num_GunDistance   = game('%default num-GunDistance')


def damage_target(select_target, func_name, loc_RaycastOrigin, loc_Hit):
    """
    Apply damage to entities/players hit by raycast.
    """
    # Init Variables
    txt_TargetUUID     = local('txt-TargetUUID')
    str_Block          = local('str-Block')
    
    select_target()
    loc_Hit.v = Select.FilterRay(loc_RaycastOrigin, def_num_GunDistance)
    Select.Reset()
    str_Block.v = SetV.GetBlockType(loc_Hit)

    with If.StringMatches(str_Block, 'air'):
        select_target()
        Select.FilterDistance(loc_Hit, 1.5)
        txt_TargetUUID.v = GameValue.SelectionTargetUUIDs()
        with If.NotEqual(txt_TargetUUID, 0):
            CallFunction(func_name, (def_num_Damage))
        Select.Reset()
        
def recoil():
    with IfPlayer.IsSneaking():
        with If.GreaterThan(def_num_Recoil, def_num_AimSpread):
            def_num_Recoil.v = SetV.ClampNumber(def_num_Recoil - def_num_IncreaseRec, def_num_AimSpread, 100)
            Control.Return()
    
    def_num_Recoil.v = SetV.ClampNumber(def_num_Recoil + def_num_IncreaseRec, 0, def_num_Spread)
    
def random_spread(raycast_origin):
    # Init Variables
    num_Min     = local('num-Min')
    num_Random1 = local('num-Random1')
    num_Random2 = local('num-Random2')
    loc_End     = local('loc-End')
    
    num_Min.v = def_num_Recoil * -1
    num_Random1.v = SetV.RandomNumber(num_Min, def_num_Recoil, rounding_mode='Decimal number')
    num_Random2.v = SetV.RandomNumber(num_Min, def_num_Recoil, rounding_mode='Decimal number')
    loc_End.v = SetV.ShiftInDirection(raycast_origin, 50)
    loc_End.v = SetV.ShiftAllDirections(loc_End, 0, num_Random1, num_Random2)

    return SetV.FaceLocation(loc_End)

def get_shoot_position():
    '''
    Bullet direction and starting position
    '''
    # Init Variables
    vec_Direction      = local('vec-Direction')
    vec_Shift          = local('vec-Shift')
    loc_BulletStart    = local('loc-BulletStart')
    
    vec_Direction.v = SetV.SetVectorLength(GameValue.Direction(), 1.7)
    vec_Shift.v = SetV.RotateAroundAxisY(vec_Direction, -25)
    loc_BulletStart.v = SetV.ShiftOnVector(GameValue.EyeLocation(), vec_Shift)
    loc_BulletStart.v = SetV.ShiftY(loc_BulletStart, -0.5)

    return loc_BulletStart

def hitscan(loc_RaycastOrigin, loc_Hit):
    bool_HitPlayer     = local('bool-HitPlayer')
    num_ParticleLength = local('num-ParticleLength')
    
    def_bool_HitScan.v = 0
    bool_HitPlayer.v = 0

    Select.EntityName(def_str_EntityHitUUID)
    with If.Equals(GameValue.SelectionSize(), 0):
        Select.PlayerName(def_str_PlayerHitUUID)
        bool_HitPlayer.v = 1

    num_ParticleLength.v = SetV.Distance(loc_RaycastOrigin, GameValue.MidpointLocation(Target.SELECTION))
    loc_Hit.v = SetV.ShiftInDirection(loc_RaycastOrigin, num_ParticleLength)

    # Pass loc_Hit to these functions
    with If.Equals(bool_HitPlayer, 0):
        CallFunction('026 DMGMob', (def_num_Damage))
    with Else():
        Control.PrintDebug([Text('%selected updated loc'), GameValue.Location(Target.SELECTION)])
        CallFunction('025 DMGPlayer', (def_num_Damage))


def main():
    # Init Variables
    loc_RaycastOrigin  = local('loc-RaycastOrigin')
    loc_Hit            = local('loc-Hit')
    
    with Function('ShootParticle') as f:
        # Get raycast origin
        loc_RaycastOrigin.v = SetV.ShiftOnVector(GameValue.EyeLocation(), GameValue.Direction())

        # Apply random spread
        loc_RaycastOrigin.v = random_spread(loc_RaycastOrigin)

        # HitScan logic
        with If.Equals(def_bool_HitScan, 1):
            hitscan(loc_RaycastOrigin, loc_Hit)

        # Non-hitScan logic
        with Else():
            # Damage mobs
            damage_target(Select.AllEntities, '026 DMGMob', loc_RaycastOrigin, loc_Hit)

            # Damage players
            damage_target(lambda: Select.PlayerName('%default', inverted=True), '025 DMGPlayer', loc_RaycastOrigin, loc_Hit)

            # Set bullet holes
            with IfGame.InBlock(loc_Hit):
                StartProcess('BulletHole', tags={'Local Variables':'Copy'})

        # Bullet Animation
        Player.ParticleLineA(
            Particle.Trail(1, 0.0, 0.0, color=(175, 155, 96), color_variation=0, duration=1),
            get_shoot_position(), loc_Hit, 0.1, 5, target=Target.ALL_PLAYERS
        )

        # Recoil handling
        recoil()

    f.build_and_send()

main()