from .target import *
from . import repeat
from . import select

# Apply the fix immediately when pyreutils is imported
repeat.apply_patch()
select.apply_patch()