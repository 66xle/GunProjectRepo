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

Function('ShowAmmo', codeblocks=[
    IfVariable.ItemHasTag(GameValue('Main Hand Item'), 'id', inverted=True, codeblocks=[
        Control.Return()
    ]),
    CallFunction('GetClipAmmo'),
    PlayerAction.ActionBar(
        [Variable('%uuid txt-UIAmmoOffset', 'saved'), 
        Text('<font:minecraft:reservenumbers:custom_font>%var(num-CurrentClip)'), 
        Text('<font:minecraft:reservenumbers:custom_font>;/;'), 
        Text('<font:minecraft:reservenumbers:custom_font>%var(num-CurrentAmmo)')])
]).build_and_send()