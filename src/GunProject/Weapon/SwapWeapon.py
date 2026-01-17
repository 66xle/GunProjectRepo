from pyreutils.wrapper import * 

num_HotBarSlot   = local('num-HotBarSlot')
item_MainHand   = local('item-MainHand')
dict_GunTag     = local('dict-GunTag')
num_RecoilTime  = local('num-RecoilTime')

# ─── Local Vars ─────────────────────────────────────────────
num_HotBarSlot      = local('num-HotBarSlot')
item_MainHand       = local('item-MainHand')
dict_GunTag         = local('dict-GunTag')
num_RecoilTime      = local('num-RecoilTime')

# ─── Default (Global) Vars ──────────────────────────────────
bool_PlayingAnim    = game('%default bool-PlayingAnimation')
bool_CancelAnim     = game('%default bool-CancelAnimation')

def_item_MainHand   = game('%default item-MainHand')
def_num_HotbarSlot  = game('%default num-HotbarSlot')

def_num_Recoil      = game('%default num-Recoil')
def_num_GunID       = game('%default num-GunID')
def_num_RateOfFire  = game('%default num-GunRateOfFire')
def_num_Distance    = game('%default num-GunDistance')
def_num_Spread      = game('%default num-Spread')
def_num_AimSpread   = game('%default num-AimSpread')
def_num_AimRecoil   = game('%default num-AimRecoil')
def_num_HipRecoil   = game('%default num-HipRecoil')
def_num_IncreaseRec = game('%default num-IncreaseRecoil')
def_num_Damage      = game('%default num-Damage')
def_num_Bullets     = game('%default num-Bullets')

def_num_ReloadMDMax = game('%default num-ReloadModelDataMax')
def_num_AttackMDMax = game('%default num-AttackModelDataMax')
def_num_ReloadLoopS = game('%default num-ReloadLoopStart')
def_num_ReloadLoopE = game('%default num-ReloadLoopEnd')

def_str_GunName     = game('%default str-GunName')
def_str_Type        = game('%default str-Type')
def_str_FireType    = game('%default str-FireType')
def_str_ReloadType  = game('%default str-ReloadType')


with Function(
    'SwapWeapon',
    Parameter('bool-InitWeapon', ParameterType.NUMBER, optional=True, default_value=0)
) as f:

    # Resolve hotbar slot
    num_HotBarSlot.v = GameValue.EventHotbarSlot()

    with If.Equals(line('bool-InitWeapon'), 1):
        num_HotBarSlot.v = 1


    # Check if animation is playing
    with If.Equals(bool_PlayingAnim, 1):
        bool_CancelAnim.v = 1
        with Repeat.While(bool_PlayingAnim, 1, sub_action='='):
            Control.Wait()

    Control.Wait()

    # Fetch item from hotbar
    item_MainHand.v = SetV.GetListValue(GameValue.HotbarItems(), num_HotBarSlot)
    with If.ItemHasTag(item_MainHand, 'id', inverted=True):
        Control.Return()

    # Reset recoil + assign held item
    def_num_Recoil.v = 0
    def_item_MainHand.v = SetV.SetModelDataNums(1)
    Player.SetSlotItem(def_item_MainHand, def_num_HotbarSlot)

    def_item_MainHand.v  = item_MainHand
    def_num_HotbarSlot.v = GameValue.EventHotbarSlot()


    # Load gun tags
    dict_GunTag.v = SetV.GetAllItemTags(def_item_MainHand)

    def_num_GunID.v        = SetV.GetDictValue(dict_GunTag, 'id')
    def_num_RateOfFire.v   = SetV.GetDictValue(dict_GunTag, 'rof')
    def_num_Distance.v     = SetV.GetDictValue(dict_GunTag, 'dist')
    def_str_GunName.v     = SetV.GetDictValue(dict_GunTag, 'name')
    def_num_Damage.v      = SetV.GetDictValue(dict_GunTag, 'damage')
    def_num_Bullets.v     = SetV.GetDictValue(dict_GunTag, 'bullets')
    def_str_Type.v        = SetV.GetDictValue(dict_GunTag, 'type')
    def_str_FireType.v    = SetV.GetDictValue(dict_GunTag, 'fire_type')

    def_num_ReloadMDMax.v = SetV.GetDictValue(dict_GunTag, 'reload_modeldata_max')
    def_num_AttackMDMax.v = SetV.GetDictValue(dict_GunTag, 'attack_modeldata_max')
    def_str_ReloadType.v  = SetV.GetDictValue(dict_GunTag, 'reload_type')
    def_num_ReloadLoopS.v = SetV.GetDictValue(dict_GunTag, 'reload_loop_start')
    def_num_ReloadLoopE.v = SetV.GetDictValue(dict_GunTag, 'reload_loop_end')

    # Recoil calculations
    def_num_Spread.v       = SetV.GetDictValue(dict_GunTag, 'max_spread')
    def_num_AimSpread.v    = SetV.GetDictValue(dict_GunTag, 'aim_spread')
    num_RecoilTime.v       = SetV.GetDictValue(dict_GunTag, 'recoil_time')

    def_num_AimRecoil.v = def_num_AimSpread / num_RecoilTime * 20
    def_num_HipRecoil.v = def_num_Spread / num_RecoilTime * 20

    def_num_IncreaseRec.v = def_num_HipRecoil

    # Single fire handling
    Player.SetEquipment(Item('ender_eye'), equipment_slot='Off hand')

    with If.StringMatches(def_str_Type, ['sniper', 'shotgun']):
        Player.ClearItems(Item('ender_eye'))

f.build_and_send()

