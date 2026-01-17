from pyreutils.wrapper import *

# ─── Local Vars ─────────────────────────────────────────────
num_MaxClip      = local('num-MaxClip')
num_ClipDifference = local('num-ClipDifference')
num_ReloadLoop   = local('num-ReloadLoop')
num_CurrentAmmo  = local('num-CurrentAmmo')
num_CurrentClip  = local('num-CurrentClip')

# ─── Game Vars ──────────────────────────────────────────────
def_item_MainHand      = game('%default item-MainHand')
def_bool_PlayingAnim    = game('%default bool-PlayingAnimation')
def_bool_IsReloading    = game('%default bool-IsReloading')
def_bool_CancelReload   = game('%default bool-CancelReload')
def_bool_FinishReloading = game('%default bool-FinishReloading')
def_str_ReloadType      = game('%default str-ReloadType')
def_num_ReloadLoopStart = game('%default num-ReloadLoopStart')
def_num_ReloadLoopEnd   = game('%default num-ReloadLoopEnd')
def_num_ReloadModelDataMax = game('%default num-ReloadModelDataMax')
dict_CurrentClip        = game('dict-CurrentClip')
dict_MaxAmmo            = game('dict-MaxAmmo')
num_ID                  = game('%default num-GunID')

with Function('Reload') as f:

    # Check if main hand has a gun
    with IfVariable.ItemHasTag(GameValue('Main Hand Item'), 'id', inverted=True):
        Control.Return()

    # Return if animation playing
    with IfVariable.Equals(def_bool_PlayingAnim, 1):
        Control.Return()

    # Get ammo and clip info
    CallFunction('GetClipAmmo')

    # Return if no ammo left
    with IfVariable.LessEqual(num_CurrentAmmo, 0):
        Control.Return()

    # Get max clip for weapon
    SetVariable.GetItemTag(num_MaxClip, def_item_MainHand, 'clip')

    # Return if clip full
    with IfVariable.Equals(num_CurrentClip, num_MaxClip):
        Control.Return()

    # Calculate amount to reload
    SetVariable.Subtract(num_ClipDifference, [num_MaxClip, num_CurrentClip])

    # Adjust if ammo less than needed
    with IfVariable.LessThan(num_CurrentAmmo, num_ClipDifference):
        num_ClipDifference.v = num_CurrentAmmo

    # Start reload loop
    num_ReloadLoop.v = 1
    def_bool_IsReloading.v = 1
    CallFunction('ReloadStart')

    # Reload animation loop
    with Repeat.Multiple(num_ReloadLoop):
        Control.Wait(0)

        # Animate reload
        with IfVariable.StringMatches(def_str_ReloadType, 'bullet'):
            CallFunction('AnimModel', ('reload', def_num_ReloadLoopStart, def_num_ReloadLoopEnd))
        with Else():
            CallFunction('AnimModel', ('reload', 100, def_num_ReloadModelDataMax))

        # Handle cancel reload
        with IfVariable.Equals(def_bool_CancelReload, 1):
            def_bool_CancelReload.v = 0
            with IfVariable.StringMatches(def_str_ReloadType, 'bullet'):
                Control.StopRepeat()
            def_bool_IsReloading.v = 0
            Control.Return()

        # Update ammo counts
        num_CurrentAmmo -= num_ClipDifference
        num_CurrentClip += num_ClipDifference

        # Update dictionaries
        SetVariable.SetDictValue(dict_CurrentClip, '%var(num-ID)', num_CurrentClip)
        SetVariable.SetDictValue(dict_MaxAmmo, '%var(num-ID)', num_CurrentAmmo)

        # Finish reload if flagged
        with IfVariable.Equals(def_bool_FinishReloading, 1):
            def_bool_FinishReloading.v = 0
            Control.StopRepeat()

    # End reload
    CallFunction('ReloadEnd')
    def_bool_IsReloading.v = 0

f.build_and_send()
