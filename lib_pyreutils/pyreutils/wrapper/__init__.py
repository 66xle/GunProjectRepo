from typing import TYPE_CHECKING

# 1. IMPORTS: Raw classes aliased with '_' to hide them
from dfpyre import Function as _Function
from dfpyre import Process as _Process
from dfpyre import CallFunction as _CallFunction
from dfpyre import StartProcess as _StartProcess
from dfpyre import Else as _Else
from dfpyre import PlayerEvent as _PlayerEvent
from dfpyre import EntityEvent as _EntityEvent
from dfpyre import Repeat as _Repeat
from dfpyre import *

# Import Aliases
from ..alias.SetVariable  import SetVariable as _SetVariable
from ..alias.PlayerAction import PlayerAction as _PlayerAction
from ..alias.GameAction   import GameAction as _GameAction
from ..alias.EntityAction import EntityAction as _EntityAction
from ..alias.IfPlayer     import IfPlayer as _IfPlayer
from ..alias.IfGame       import IfGame as _IfGame
from ..alias.IfVariable   import IfVariable as _IfVariable
from ..alias.IfEntity     import IfEntity as _IfEntity
from ..alias.SelectObject import SelectObject as _SelectObject
from ..alias.Control      import Control as _Control
from ..alias              import *

from .context import ContextBlock, _get_current_context
from .emitter import AutoEmitter, HeaderEmitter
from .smart_wrapper import SmartSetVariableWrapper
from .magic_handler import MagicVarHandler
from .math_ops import MathOp 

# ==========================================
# 2. WRAPPER FUNCTIONS (Internal)
# ==========================================

def _Function_Wrapper(*args, **kwargs):
    """Wraps Function() in a ContextBlock."""
    return ContextBlock(_Function(*args, **kwargs), name="Function")

def _Process_Wrapper(*args, **kwargs):
    """Wraps Process() in a ContextBlock."""
    return ContextBlock(_Process(*args, **kwargs), name="Process")
def _CallFunction_Wrapper(*args, **kwargs):
    """Wraps CallFunction with MathOp support."""
    # 2. Create Block
    block = _CallFunction(*args, **kwargs)
    
    # 3. Add to Context
    ctx = _get_current_context()
    if ctx is not None:
        if isinstance(block, list): 
            ctx.extend(block)
        else: 
            ctx.append(block)
        
    return block

def _StartProcess_Wrapper(*args, **kwargs):
    """Wraps StartProcess with MathOp support."""
    block = _StartProcess(*args, **kwargs)
    
    ctx = _get_current_context()
    if ctx is not None:
        if isinstance(block, list): 
            ctx.extend(block)
        else: 
            ctx.append(block)
        
    return block

def _Else_Wrapper(*args, **kwargs):
    """Wraps Else to handle bracket context."""
    result = _Else(*args, **kwargs)
    
    if isinstance(result, list) and len(result) >= 2:
        close_block = result[-1]      
        immediate_blocks = result[:-1] 
        
        # FIX: Do not ctx.extend here. Let ContextBlock do it on __enter__
        return ContextBlock(immediate_blocks, close_block=close_block, name="Else")
    
    # Fallback (Shouldn't happen for Else)
    ctx = _get_current_context()
    if ctx is not None:
        if isinstance(result, list): 
            ctx.extend(result)
        else: 
            ctx.append(result)
    return ContextBlock(result, name="Else")

if TYPE_CHECKING:
    # --- IDE / STATIC ANALYSIS VIEW ---
    # The IDE sees the ORIGINAL classes.
    # This enables Auto-Complete and Ctrl+Click navigation to the library.
    SetVariable = _SetVariable
    
    PlayerAction = _PlayerAction
    GameAction = _GameAction
    EntityAction = _EntityAction
    
    IfPlayer = _IfPlayer
    IfGame = _IfGame
    IfVariable = _IfVariable
    IfEntity = _IfEntity
    
    SelectObject = _SelectObject
    Repeat = _Repeat
    Control = _Control
    
    # Events
    PlayerEvent = _PlayerEvent
    EntityEvent = _EntityEvent
    
    # Functions
    CallFunction = _CallFunction
    StartProcess = _StartProcess
    Else = _Else
    Process = _Process
    Function = _Function

else:
    # --- RUNTIME VIEW ---
    # Python executes this. It sees the WRAPPERS.
    
    # 1. Action Containers (AutoEmitter)
    PlayerAction = AutoEmitter(_PlayerAction)
    GameAction = AutoEmitter(_GameAction)
    EntityAction = AutoEmitter(_EntityAction)
    
    IfPlayer = AutoEmitter(_IfPlayer)
    IfVariable = AutoEmitter(_IfVariable)
    IfGame = AutoEmitter(_IfGame)
    IfEntity = AutoEmitter(_IfEntity)
    
    SelectObject = AutoEmitter(_SelectObject)
    Repeat = AutoEmitter(_Repeat)
    Control = AutoEmitter(_Control)
    
    # 2. Smart Variables
    SetVariable = SmartSetVariableWrapper()

    # 3. Events (HeaderEmitter)
    PlayerEvent = HeaderEmitter(_PlayerEvent)
    EntityEvent = HeaderEmitter(_EntityEvent)
    
    # 4. Standalone Wrappers (Explicit Assignment)
    # This is where we force Python to use our logic.
    CallFunction = _CallFunction_Wrapper
    StartProcess = _StartProcess_Wrapper
    Else = _Else_Wrapper
    Function = _Function_Wrapper
    Process = _Process_Wrapper
    
# Other
SetV    = SetVariable
SV      = SetVariable

Select  = SelectObject
SO      = SelectObject

Ctrl    = Control
C       = Control

# Actions
Player  = PlayerAction
PA      = PlayerAction

Entity  = EntityAction
EA      = EntityAction

Game    = GameAction
GA      = GameAction

# If Statements
If      = IfVariable
IV      = IfVariable

IfP     = IfPlayer
IF      = IfPlayer

IfE     = IfEntity
IE      = IfEntity

IfG     = IfGame
IG      = IfGame
    
local = MagicVarHandler('local')
"""
Create a local variable with the given name. 


:param name: The name of the variable.
:return MagicVarHandler: Creates Variable(name, 'local')
"""

line = MagicVarHandler('line')
"""
Create a line variable with the given name.

:param name: The name of the variable.
:return MagicVarHandler: Creates Variable(name, 'line')
"""

save = MagicVarHandler('saved')
"""
Create a save variable with the given name.

:param name: The name of the variable.
:return MagicVarHandler: Creates Variable(name, 'save')
"""

game = MagicVarHandler('unsaved')
"""
Create a game (unsaved) variable with the given name.

:param name: The name of the variable.
:return MagicVarHandler: Creates Variable(name, 'game')
"""

