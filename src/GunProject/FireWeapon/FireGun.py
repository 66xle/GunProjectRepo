from pyreutils.wrapper import *

# ─── Local Vars ─────────────────────────────────────────────
num_CurrentClip   = local('num-CurrentClip')
num_Wait          = local('num-Wait')

snd_Shoot         = local('snd-Shoot')
loc_FarSound      = local('loc-FarSound')

# ─── Default (Global) Vars ──────────────────────────────────
def_item_MainHand       = game('%default item-MainHand')

bool_PlayingAnim        = game('%default bool-PlayingAnimation')
bool_IsReloading        = game('%default bool-IsReloading')
bool_FinishReloading    = game('%default bool-FinishReloading')

def_num_Bullets         = game('%default num-Bullets')
def_num_GunRateOfFire   = game('%default num-GunRateOfFire')
def_num_AttackMDMax     = game('%default num-AttackModelDataMax')

def_str_GunName         = game('%default str-GunName')
def_str_FireType        = game('%default str-FireType')
def_str_ReloadType      = game('%default str-ReloadType')


with Function('FireGun',Parameter('num-WaitForFireModel', ParameterType.NUMBER)) as f:

    # Ensure holding a gun
    with If.ItemHasTag(GameValue.MainHandItem(), 'id', inverted=True):
        Control.Return()


    # Block while animation is playing
    with If.Equals(bool_PlayingAnim, 1):
        with If.Equals(bool_IsReloading, 1):
            with If.StringMatches(def_str_ReloadType, 'bullet'):
                bool_FinishReloading.v = 1
                Control.Return()
            Control.Return()
        Control.Return()


    # Ammo checks
    CallFunction('GetClipAmmo')

    with If.LessEqual(num_CurrentClip, 0):
        CallFunction('Reload')
        Control.Return()


    # Fire bullets
    with Repeat.Multiple(def_num_Bullets):
        CallFunction('ShootParticle')


    # Shooting sound (near + far)
    snd_Shoot.v = SetV.SetCustomSound(
        Sound('Cherry Wood Place', 1.0, 2.0),
        'custom.ranged.%var(%default str-GunName).shoot'
    )

    loc_FarSound.v = SetV.ShiftY(GameValue.Location(), 0)

    Player.PlaySound(snd_Shoot, target=Target.DEFAULT)

    Select.PlayersCond('%default', sub_action='PNameEquals', inverted=True)
    snd_Shoot.v = SetV.SetSoundVolume(0.5)
    Player.PlaySound(snd_Shoot, loc_FarSound, target=Target.SELECTION)
    Select.Reset()


    # Cooldown + ammo reduction
    Player.SetItemCooldown(def_item_MainHand, def_num_GunRateOfFire)
    CallFunction('ReduceClip')

    # Fire mode handling
    with If.StringMatches(def_str_FireType, 'auto'):
        num_Wait.v = line('num-WaitForFireModel')
        StartProcess('FireModel', tags={'Local Variables':'Copy'})
    with Else():
        CallFunction('AnimModel', 'attack', 2, def_num_AttackMDMax)

f.build_and_send()
