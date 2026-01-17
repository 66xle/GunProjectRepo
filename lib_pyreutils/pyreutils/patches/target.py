from enum import Enum
import dfpyre  # Import the module so we can patch it
from dfpyre.core.codeblock import TARGETS

# 1. Define the replacement class
class _Target(Enum):
    SELECTION = 0
    DEFAULT = 1
    KILLER = 2
    DAMAGER = 3
    SHOOTER = 4
    VICTIM = 5
    ALL_PLAYERS = 6
    PROJECTILE = 7
    ALL_ENTITIES = 8
    ALL_MOBS = 9
    LAST_ENTITY = 10
    NONE = 11

    def get_string_value(self):
            return TARGETS[self.value]

# 2. Apply the Patch
# This overwrites the class in the original library's memory
dfpyre.Target = _Target

# 3. Update the default variable to use your new NONE value
dfpyre.DEFAULT_TARGET = _Target.NONE