from pyreutils import *
from dfpyre import *

txt_UIAmmoOffset = Variable('%uuid txt-UIAmmoOffset', 'saved')
reserve_numbers_font = '<font:minecraft:reservenumbers:custom_font>'

Function('ShowAmmo', codeblocks=[
    IfVariable.ItemHasTag(GameValue('Main Hand Item'), 'id', inverted=True, codeblocks=[
        Control.Return()
    ]),
    CallFunction('GetClipAmmo'),
    PlayerAction.ActionBar(
        [txt_UIAmmoOffset, 
        Text(f'{reserve_numbers_font}%var(num-CurrentClip)'), 
        Text(f'{reserve_numbers_font};/;'), 
        Text(f'{reserve_numbers_font}%var(num-CurrentAmmo)')])
]).build_and_send()