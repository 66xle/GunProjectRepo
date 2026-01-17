from pyreutils.wrapper import *

# ─── Local Vars ─────────────────────────────────────────────
txt_Translate       = local('txt-Translate')
txt_TranslateOffset = local('txt-TranslateOffset')
str_Test            = local('str-Test')

with Function('BuildOffset', Parameter('num-Offset', ParameterType.NUMBER)) as f:

    txt_Translate.v = Text('<translate:space.100>')

    with IfVariable.LessThan(line('num-Offset'), 0):
        SetVariable.AbsoluteValue(line('num-Offset'), line('num-Offset'))
        txt_Translate.v = Text('<translate:space.-100>')

    with IfVariable.GreaterThan(line('num-Offset'), 0):
        txt_TranslateOffset.v = txt_Translate
        with Repeat.Multiple(number=Number('%math(%var(num-Offset) - 1)')):
            Control.Wait(0)
            SetVariable.StyledText(txt_TranslateOffset, [txt_TranslateOffset, txt_Translate])
            SetVariable.GetMiniMessageExpr(str_Test, txt_TranslateOffset)

    with Else():
        txt_TranslateOffset.v = Text('<translate:space.0>')

f.build_and_send()
