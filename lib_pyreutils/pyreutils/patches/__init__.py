from .target import *
from . import fix_repeat

# Apply the fix immediately when pyreutils is imported
fix_repeat.apply_patch()