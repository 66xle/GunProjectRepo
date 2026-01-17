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

    num_HotBarSlot.v = GameValue('Event Hotbar Slot')

    with IfVariable.Equals(line('bool-InitWeapon'), 1):
        num_HotBarSlot.v = 1


    # Check If playing animation
    with IfVariable.Equals(bool_PlayingAnim, 1):
        bool_CancelAnim.v = 1
        with Repeat.While(bool_PlayingAnim, 1, sub_action='='):
            Control.Wait()

    Control.Wait()

    item_MainHand.v = SetVariable.GetListValue(GameValue('Hotbar Items'), num_HotBarSlot)
    with IfVariable.ItemHasTag(item_MainHand, 'id', inverted=True):
        Control.Return()


    def_num_Recoil.v = 0
    SetVariable.SetModelDataNums(def_item_MainHand, 1)
    PlayerAction.SetSlotItem(def_item_MainHand, def_num_HotbarSlot)

    def_item_MainHand.v  = item_MainHand
    def_num_HotbarSlot.v = GameValue('Event Hotbar Slot')


    dict_GunTag.v = SetVariable.GetAllItemTags(def_item_MainHand)

    def_num_GunID.v        = SetVariable.GetDictValue(dict_GunTag, 'id')
    def_num_RateOfFire.v   = SetVariable.GetDictValue(dict_GunTag, 'rof')
    def_num_Distance.v     = SetVariable.GetDictValue(dict_GunTag, 'dist')
    def_str_GunName.v     = SetVariable.GetDictValue(dict_GunTag, 'name')
    def_num_Damage.v      = SetVariable.GetDictValue(dict_GunTag, 'damage')
    def_num_Bullets.v     = SetVariable.GetDictValue(dict_GunTag, 'bullets')
    def_str_Type.v        = SetVariable.GetDictValue(dict_GunTag, 'type')
    def_str_FireType.v    = SetVariable.GetDictValue(dict_GunTag, 'fire_type')

    def_num_ReloadMDMax.v = SetVariable.GetDictValue(dict_GunTag, 'reload_modeldata_max')
    def_num_AttackMDMax.v = SetVariable.GetDictValue(dict_GunTag, 'attack_modeldata_max')
    def_str_ReloadType.v  = SetVariable.GetDictValue(dict_GunTag, 'reload_type')
    def_num_ReloadLoopS.v = SetVariable.GetDictValue(dict_GunTag, 'reload_loop_start')
    def_num_ReloadLoopE.v = SetVariable.GetDictValue(dict_GunTag, 'reload_loop_end')


    def_num_Spread.v       = SetVariable.GetDictValue(dict_GunTag, 'max_spread')
    def_num_AimSpread.v    = SetVariable.GetDictValue(dict_GunTag, 'aim_spread')
    num_RecoilTime.v       = SetVariable.GetDictValue(dict_GunTag, 'recoil_time')

    def_num_AimRecoil.v = Number(
        '%math(%var(%default num-AimSpread) / %math(%var(num-RecoilTime) * 20))'
    )
    def_num_HipRecoil.v = Number(
        '%math(%var(%default num-Spread) / %math(%var(num-RecoilTime) * 20))'
    )
    def_num_IncreaseRec.v = def_num_HipRecoil


    PlayerAction.SetEquipment(Item('ender_eye'), equipment_slot='Off hand')

    with IfVariable.StringMatches(def_str_Type, 'sniper'):
        PlayerAction.ClearItems(Item('ender_eye'))

f.build_and_send()

