from pyreutils.wrapper import *

# ─── Local Vars ─────────────────────────────────────────────
item_Weapon = local('item-Weapon')

# ─── Game Vars ──────────────────────────────────────────────
def_item_MainHand       = game('%default item-MainHand')
def_num_HotbarSlot      = game('%default num-HotbarSlot')
def_bool_PlayingAnim    = game('%default bool-PlayingAnimation')
def_num_ReloadLoopEnd   = game('%default num-ReloadLoopEnd')
def_num_ReloadModelDataMax = game('%default num-ReloadModelDataMax')
def_str_ReloadType      = game('%default str-ReloadType')

with Function('ReloadEnd') as f:

    # Only proceed if reload type is 'bullet'
    with If.StringMatches(def_str_ReloadType, 'bullet'):

        # Play final reload animation
        CallFunction(
            'AnimModel',
            ('reload', Number('%math(%var(%default num-ReloadLoopEnd) + 1)'), def_num_ReloadModelDataMax)
        )

        # Reset weapon model to idle
        item_Weapon.v = SetV.SetModelDataNums(def_item_MainHand, 1)
        Player.SetSlotItem(item_Weapon, def_num_HotbarSlot)

        # Mark animation as finished
        def_bool_PlayingAnim.v = 0

f.build_and_send()
