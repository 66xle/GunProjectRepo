from typing import TYPE_CHECKING
from dfpyre import Function as DFFunction
from dfpyre import Process as DFProcess
from dfpyre import PlayerEvent as _PlayerEvent
from dfpyre import EntityEvent as _EntityEvent
from dfpyre import *

from ..alias.SetVariable import SetVariable as _SetVariable
from ..alias import *

from .context import ContextBlock
from .emitter import AutoEmitter, HeaderEmitter
from .smart_wrapper import SmartSetVariableWrapper
from .magic_handler import MagicVarHandler
from .math_ops import MathOp 

if TYPE_CHECKING:
    SetVariable = _SetVariable
    PlayerAction = PlayerAction
    IfPlayer = IfPlayer
    GameAction = GameAction
    IfGame = IfGame
    EntityAction = EntityAction
    IfEntity = IfEntity
    SelectObject = SelectObject
    Repeat = Repeat
    
    # Events (Type Checking)
    PlayerEvent = _PlayerEvent
    EntityEvent = _EntityEvent
else:
    SetVariable = SmartSetVariableWrapper()
    PlayerAction = AutoEmitter(PlayerAction)
    GameAction = AutoEmitter(GameAction)
    EntityAction = AutoEmitter(EntityAction)
    SelectObject = AutoEmitter(SelectObject)
    IfPlayer = AutoEmitter(IfPlayer)
    IfVariable = AutoEmitter(IfVariable)
    IfGame = AutoEmitter(IfGame)
    IfEntity = AutoEmitter(IfEntity)
    Repeat = AutoEmitter(Repeat)
    
    # Wrap Events with HeaderEmitter
    PlayerEvent = HeaderEmitter(_PlayerEvent)
    EntityEvent = HeaderEmitter(_EntityEvent)

# Wrapper for Function
def Function(*args, **kwargs):
    block = DFFunction(*args, **kwargs)
    return ContextBlock(block)

# Wrapper for Process
def Process(*args, **kwargs):
    block = DFProcess(*args, **kwargs)
    return ContextBlock(block)

