from dfpyre import *

Function('ShowAmmo', codeblocks=[
    IfVariable.ItemHasTag(GameValue('Main Hand Item'), 'id', inverted=True, codeblocks=[
        Control.Return()
    ]),
    CallFunction('GetClipAmmo'),
    PlayerAction.ActionBar(
        Variable('%uuid txt-UIAmmoOffset', 'saved'), 
        Text('<font:minecraft:reservenumbers:custom_font>%var(num-CurrentClip)', None), 
        Text('<font:minecraft:reservenumbers:custom_font>;/;', None), 
        Text('<font:minecraft:reservenumbers:custom_font>%var(num-CurrentAmmo)', None))
]).build_and_send()