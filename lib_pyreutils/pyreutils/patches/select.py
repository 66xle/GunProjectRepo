from dfpyre import CodeBlock, SelectObject, String as DFString

def fixed_playername(texts: list[DFString] | DFString, inverted: bool=False):
    """
    Patched implementation of Player Select.
    Fixes the issue where the invert argument is missing.
    """
    return CodeBlock.new_subaction_block('select_obj', 'PlayerName', (texts,), {}, '', inverted)

def apply_patch():
    SelectObject.PlayerName = staticmethod(fixed_playername)