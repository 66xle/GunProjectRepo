# region Util Imports
import sys
import os

# Add the parent directory to Python's search path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from Utils.alias import *

# endregion

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