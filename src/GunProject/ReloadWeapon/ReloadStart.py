from pyreutils.wrapper import *

# ─── Local Vars ─────────────────────────────────────────────
num_ReloadLoop     = local('num-ReloadLoop')
num_ClipDifference = local('num-ClipDifference')

# ─── Game Vars ──────────────────────────────────────────────
def_bool_PlayingAnim   = game('%default bool-PlayingAnimation')
def_str_ReloadType     = game('%default str-ReloadType')
def_num_ReloadLoopStart = game('%default num-ReloadLoopStart')

with Function('ReloadStart') as f:

    # Only proceed if reload type is 'bullet'
    with IfVariable.StringMatches(def_str_ReloadType, 'bullet'):

        # Setup reload loop
        num_ReloadLoop.v = local('num-ClipDifference')  # store original clip difference in loop count
        num_ClipDifference.v = 1
        def_bool_PlayingAnim.v = 1

        # Debug print
        Control.PrintDebug(
            Number('%math(%default num-ReloadLoopStart - 1)'),
            sound='Success'
        )

        # Play initial reload animation
        CallFunction('AnimModel', ('reload', 100, Number('%math(%var(%default num-ReloadLoopStart) - 1)')))

f.build_and_send()
