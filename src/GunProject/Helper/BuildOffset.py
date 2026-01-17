from pyreutils.wrapper import *

# ─── Local Vars ─────────────────────────────────────────────
txt_Translate       = local('txt-Translate')
txt_TranslateOffset = local('txt-TranslateOffset')
str_Test            = local('str-Test')

# ─── Line Vars ─────────────────────────────────────────────
num_Offset = line('num-Offset')

with Function('BuildOffset', Parameter('num-Offset', ParameterType.NUMBER)) as f:

    txt_Translate.v = Text('<translate:space.100>')

    with If.LessThan(num_Offset, 0):
        num_Offset.v = SetV.AbsoluteValue(num_Offset)
        txt_Translate.v = Text('<translate:space.-100>')

    with If.GreaterThan(num_Offset, 0):
        txt_TranslateOffset.v = txt_Translate
        with Repeat.Multiple(number=Number('%math(%var(num-Offset) - 1)')):
            Control.Wait(0)
            txt_TranslateOffset = SetV.StyledText([txt_TranslateOffset, txt_Translate])
            str_Test = SetV.GetMiniMessageExpr(txt_TranslateOffset)

    with Else():
        txt_TranslateOffset.v = Text('<translate:space.0>')

f.build_and_send()
