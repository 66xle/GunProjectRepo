from .target import *
from . import repeat
from . import select
from . import particle

# Apply the fix immediately when pyreutils is imported
repeat.apply_patch()
select.apply_patch()
particle.apply_patch()