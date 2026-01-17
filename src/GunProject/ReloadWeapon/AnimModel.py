from pyreutils.wrapper import *

# ─── Local Vars ─────────────────────────────────────────────
num_ModelID    = local('num-ModelID')
list_ModelData = local('list-ModelData')
num_ListIndex  = local('num-ListIndex')
str_SoundRef   = local('str-SoundRef')
snd_CustomSound = local('snd-CustomSound')
item_Weapon    = local('item-Weapon')

list_Sounds    = local('list-Sounds')

# ─── Game Vars ──────────────────────────────────────────────
def_item_MainHand     = game('%default item-MainHand')
def_num_HotbarSlot    = game('%default num-HotbarSlot')
def_bool_PlayingAnim   = game('%default bool-PlayingAnimation')
def_bool_CancelAnim    = game('%default bool-CancelAnimation')
def_bool_CancelReload  = game('%default bool-CancelReload')
def_str_GunName        = game('%default str-GunName')
def_str_ReloadType     = game('%default str-ReloadType')

with Function(
    'AnimModel',
    Parameter('str-Type', ParameterType.STRING, note='attack/reload'),
    Parameter('num-MinAnimModelData', ParameterType.NUMBER),
    Parameter('num-MaxAnimModelData', ParameterType.NUMBER)
) as f:

    # Get the sounds for this animation type
    CallFunction('GetSounds', (line('str-Type')))

    # Mark animation playing if reload type is 'clip'
    with If.StringMatches(def_str_ReloadType, 'clip'):
        def_bool_PlayingAnim.v = 1

    # Animate through the model data range
    with Repeat.Range((line('num-ModelID'), line('num-MinAnimModelData'), line('num-MaxAnimModelData'))):

        Control.Wait()

        # Play sound if model data exists in list
        with If.ListContains(list_ModelData, '%var(num-ModelID)'):
            num_ListIndex.v = SetVariable.GetValueIndex(list_ModelData, '%var(num-ModelID)')
            str_SoundRef.v = SetVariable.GetListValue(list_Sounds, num_ListIndex)
            snd_CustomSound.v = SetVariable.SetCustomSound(
                Sound('Pling', 1.0, 2.0),
                'custom.ranged.%var(%default str-GunName).%var(str-Type)_%var(str-SoundRef)'
            )
            PlayerAction.PlaySound(snd_CustomSound)

        # Stop animation if cancel flag is set
        with If.Equals(def_bool_CancelAnim, 1):
            def_bool_CancelAnim.v = 0
            with If.StringMatches(line('str-Type'), 'reload'):
                def_bool_CancelReload.v = 1
            Control.StopRepeat()

        # Set the model data and slot item for the current frame
        item_Weapon = SetVariable.SetModelDataNums(def_item_MainHand, line('num-ModelID'))
        PlayerAction.SetSlotItem(item_Weapon, def_num_HotbarSlot)

    Control.Wait()

    # Reset animation state if reload type is 'clip'
    with If.StringMatches(def_str_ReloadType, 'clip'):
        item_Weapon.v = SetVariable.SetModelDataNums(def_item_MainHand, 1)
        PlayerAction.SetSlotItem(item_Weapon, def_num_HotbarSlot)
        def_bool_PlayingAnim.v = 0

f.build_and_send()
