from dfpyre import CodeBlock, Repeat
# You might need to adjust this import depending on where add_brackets lives in dfpyre
# It is often in dfpyre.pyre or dfpyre.utils
from dfpyre.export.block_functions import add_brackets 

def fixed_range(*args, tags={}, sub_action=None, inverted=False, codeblocks=[]):
    """
    Patched implementation of Range.
    Fixes the issue where the action was incorrectly set to 'While' instead of 'Range'.
    """
    # FIX: Changed 'While' to 'Range'
    return add_brackets(CodeBlock.new_subaction_block('repeat', 'Range', args, tags, sub_action, inverted), codeblocks, 'repeat')

def apply_patch():
    # Overwrite the broken method on the Repeat class
    # We use staticmethod() because the original was a @staticmethod
    Repeat.Range = staticmethod(fixed_range)