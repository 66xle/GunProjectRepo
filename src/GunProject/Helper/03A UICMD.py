from pyreutils.wrapper import *

# ─── Local Vars ─────────────────────────────────────────────
num_Length    = local('num-Length')
str_Offset    = local('str-Offset')
num_Offset    = local('num-Offset')
txt_TranslateOffset = local('txt-TranslateOffset')

# ─── Saved Vars ─────────────────────────────────────────────
txt_UIAmmoOffset = save('%uuid txt-UIAmmoOffset')

with Function('03A UICMD') as f:

    with IfGame.CommandEquals('uiammo', check_mode='Check beginning'):
        num_Length.v = SetVariable.ListLength(GameValue('Event Command Arguments'))

        with IfVariable.NotEqual(num_Length, 2):
            PlayerAction.SendMessage(Text('Invalid arguments'))
            Control.End()

        str_Offset.v = SetVariable.GetListValue(GameValue('Event Command Arguments'), 2)
        num_Offset.v = SetVariable.ParseNumber(str_Offset)

        CallFunction('BuildOffset', (num_Offset))
        
        txt_UIAmmoOffset.v = txt_TranslateOffset

        PlayerAction.SendMessage([Text('Offset set to:'), num_Offset])
        Control.End()

f.build_and_send()