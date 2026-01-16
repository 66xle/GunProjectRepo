from typing import TYPE_CHECKING
from dfpyre import *
from dfpyre import Function as DFFunction
from ..alias.SetVariable import SetVariable as _SetVariable
from ..alias import *

# ==========================================
# 0. MATH OPERATOR LOGIC & PATCHES
# ==========================================
class MathOp:
    """Represents a chain of math operations (e.g. Var * 2 + 5)"""
    def __init__(self, source, ops=None):
        self.source = source 
        self.ops = ops if ops else [] # List of ('Add', val, '+')
    
    def _add_op(self, method_name, val, symbol):
        return MathOp(self.source, self.ops + [(method_name, val, symbol)])

    # Standard Python Operators
    def __add__(self, o): return self._add_op('Add', o, '+')
    def __sub__(self, o): return self._add_op('Subtract', o, '-')
    def __mul__(self, o): return self._add_op('Multiply', o, '*')
    def __truediv__(self, o): return self._add_op('Divide', o, '/')
    def __mod__(self, o): return self._add_op('Remainder', o, '%')

    def is_complex(self):
        """Returns True if the operations are mixed (e.g. * and +)"""
        if not self.ops: 
            return False
        first_op = self.ops[0][0]
        # If any operation is different from the first one, it's complex.
        return any(op[0] != first_op for op in self.ops)

    def to_math(self):
        """Converts mixed math into a DF Num Item with %math()"""
        parts = []
        
        # Handle Source
        if isinstance(self.source, Var): 
            parts.append(f'%var({self.source.name})')
        else: 
            parts.append(str(self.source))
        
        # Handle Ops
        for _, val, symbol in self.ops:
            if isinstance(val, Var): 
                val_str = f'%var({val.name})'
            else: 
                val_str = str(val)
            parts.append(f' {symbol} {val_str}')
            
        math_str = "".join(parts)
        return Number(f'%math({math_str})')

# --- HELPER: Emit In-Place Block ---
def _emit_inplace(block):
    ctx = _get_current_context()
    if ctx is None: 
        return
    if isinstance(block, list): 
        ctx.extend(block)
    else: 
        ctx.append(block)

# --- MONKEY PATCHES ---
def _patch_var_methods(cls):
    # 1. Math Ops (Var + 5) -> Returns MathOp object
    cls.__add__ = lambda self, o: MathOp(self)._add_op('Add', o, '+')
    cls.__sub__ = lambda self, o: MathOp(self)._add_op('Subtract', o, '-')
    cls.__mul__ = lambda self, o: MathOp(self)._add_op('Multiply', o, '*')
    cls.__truediv__ = lambda self, o: MathOp(self)._add_op('Divide', o, '/')
    cls.__mod__ = lambda self, o: MathOp(self)._add_op('Remainder', o, '%')
    
    # 2. Reverse Math (5 + Var)
    cls.__radd__ = lambda self, o: MathOp(o)._add_op('Add', self, '+')
    cls.__rmul__ = lambda self, o: MathOp(o)._add_op('Multiply', self, '*')
    
    # 3. In-Place Assignments (v.x += 1)
    # These execute immediately and return 'self' to satisfy Python's assignment logic
    cls.__iadd__ = lambda self, o: (_emit_inplace(_SetVariable.Increment(self, o)) or self)
    cls.__isub__ = lambda self, o: (_emit_inplace(_SetVariable.Decrement(self, o)) or self)
    # Note: Multiply/Divide in DF takes [Target, Target, Source]
    cls.__imul__ = lambda self, o: (_emit_inplace(_SetVariable.Multiply(self, [self, o])) or self)
    cls.__idiv__ = lambda self, o: (_emit_inplace(_SetVariable.Divide(self, [self, o])) or self)

def _patch_gamevalue_methods(cls):
    # GameValues are read-only source
    cls.__add__ = lambda self, o: MathOp(self)._add_op('Add', o, '+')
    cls.__sub__ = lambda self, o: MathOp(self)._add_op('Subtract', o, '-')
    cls.__mul__ = lambda self, o: MathOp(self)._add_op('Multiply', o, '*')
    cls.__truediv__ = lambda self, o: MathOp(self)._add_op('Divide', o, '/')
    cls.__mod__ = lambda self, o: MathOp(self)._add_op('Remainder', o, '%')
    # Reverse: (Number + GameValue)
    cls.__radd__ = lambda self, o: MathOp(o)._add_op('Add', self, '+')
    cls.__rmul__ = lambda self, o: MathOp(o)._add_op('Multiply', self, '*')

_patch_var_methods(Var)
_patch_gamevalue_methods(GameValue)

# ==========================================
# 1. CONTEXT STACK & MANAGER
# ==========================================
_context_stack = []

def _get_current_context():
    if _context_stack: 
        return _context_stack[-1]
    return None

class ContextBlock:
    def __init__(self, block_obj, close_block=None):
        self.block = block_obj
        self.close_block = close_block
        
    def __enter__(self):
        if self.close_block is not None: 
            return self.block

        if not hasattr(self.block, 'codeblocks'): 
            self.block.codeblocks = []
        _context_stack.append(self.block.codeblocks)
        return self.block

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.close_block is not None:
            ctx = _get_current_context()
            if ctx is not None: 
                ctx.append(self.close_block)
            return
        _context_stack.pop()

    def __getattr__(self, name):
        return getattr(self.block, name)

# ==========================================
# 2. AUTO-EMITTER
# ==========================================
class AutoEmitter:
    def __init__(self, original_class):
        self._cls = original_class
        class_name = self._cls.__name__
        self._is_container_class = class_name.startswith("If") or class_name == "Repeat"

    def __getattr__(self, name):
        original_attr = getattr(self._cls, name)
        if not callable(original_attr): 
            return original_attr

        def wrapper(*args, **kwargs):
            result = original_attr(*args, **kwargs)
            is_container = self._is_container_class or name == "Else"
            
            # Linear Bracket List [If, Open, Close]
            if is_container and isinstance(result, list) and len(result) >= 2:
                close_block = result[-1]      
                immediate_blocks = result[:-1] 
                ctx = _get_current_context()
                if ctx is not None: 
                    ctx.extend(immediate_blocks)
                return ContextBlock(immediate_blocks[0], close_block=close_block)

            # Standard Block
            else:
                if isinstance(result, list):
                    blocks = result
                    main_block = result[-1] if result else None
                else:
                    blocks = [result]
                    main_block = result

                ctx = _get_current_context()
                if ctx is not None: 
                    ctx.extend(blocks)
                
                if name == "Function" or is_container:
                     return ContextBlock(main_block)
                return main_block
        return wrapper

# ==========================================
# 3. SMART SetVariable WRAPPER
# ==========================================
class OptimisticOp:
    def __init__(self, name, args, created_block=None):
        self.name = name
        self.args = args
        self.created_block = created_block

class SmartSetVariableWrapper:
    def __getattr__(self, name):
        original_method = getattr(_SetVariable, name)
        
        def wrapper(*args, **kwargs):
            # --- FIX: MATH IN PARAMETERS ---
            # If any argument is a MathOp (e.g. SetVar.Exp(x, 2, v.y + 2)),
            # we must convert it to a Num item immediately.
            clean_args = []
            for arg in args:
                if isinstance(arg, MathOp): 
                    clean_args.append(arg.to_math())
                else: 
                    clean_args.append(arg)
            
            try:
                result = original_method(*clean_args, **kwargs)
                ctx = _get_current_context()
                if isinstance(result, list): 
                    ctx.extend(result)
                else: 
                    ctx.append(result)
                return OptimisticOp(name, clean_args, created_block=result)
            except Exception:
                return OptimisticOp(name, clean_args, created_block=None)
            
        return wrapper

# ==========================================
# 4. MAGIC VARIABLE HANDLER (Optimized Math)
# ==========================================
class MagicVarHandler:
    def __init__(self, local_vars):
        self._vars = local_vars

    def __setattr__(self, name, value):
        if name.startswith("_"): 
            super().__setattr__(name, value)
            return
        if name not in self._vars: 
            raise ValueError(f"Undefined variable: '{name}'")
        
        var_obj = self._vars[name]

        # FIX: Ignore self-assignment from += (v.x = v.x + 1)
        if value is var_obj:
            return

        ctx = _get_current_context()
        
        # --- CASE 1: MATH OPERATION ---
        if isinstance(value, MathOp):
            
            # Sub-Case A: Mixed/Complex Math -> Use %math
            if value.is_complex():
                ctx.append(_SetVariable.Assign(var_obj, value.to_item()))
            
            # Sub-Case B: Sequential Math -> Optimized Chain
            else:
                ops = value.ops
                source = value.source

                if ops:
                    # OPTIMIZATION: Use 3-Argument Method for the first step.
                    # Instead of: Assign(T, A) -> Subtract(T, B)
                    # We do:      Subtract(T, A, B)
                    first_method_name, first_val, _ = ops[0]
                    method = getattr(_SetVariable, first_method_name)
                    
                    # Generate: SetVariable.Subtract(Target, Source, Amount)
                    if isinstance(first_val, list):
                        ctx.append(method(var_obj, [source, *first_val]))
                    else:
                        ctx.append(method(var_obj, [source, first_val]))
                    
                    # Process remaining operations (chained to the Target)
                    # e.g. T = A - B - C  becomes:
                    # 1. Subtract(T, A, B)  (Result is now in T)
                    # 2. Subtract(T, C)     (Subtract C from T)
                    for method_name, val, _ in ops[1:]:
                        method = getattr(_SetVariable, method_name)
                        if isinstance(val, list): 
                            ctx.append(method(var_obj, *val))
                        else: 
                            ctx.append(method(var_obj, val))
                
                else:
                    # No ops (just v.x = v.y) -> Standard Assign
                    ctx.append(_SetVariable.Assign(var_obj, source))

            return 

        # --- CASE 2: OPTIMISTIC OP (Rollback) ---
        if isinstance(value, OptimisticOp):
            if value.created_block is not None:
                if isinstance(value.created_block, list):
                    for b in reversed(value.created_block):
                        if ctx and ctx[-1] is b: 
                            ctx.pop()
                elif ctx and ctx[-1] is value.created_block:
                    ctx.pop()

            method = getattr(_SetVariable, value.name)
            result = method(var_obj, *value.args)
            if isinstance(result, list):
                ctx.extend(result)
            else: 
                ctx.append(result)
            return

        # --- CASE 3: STANDARD ASSIGN ---
        result = _SetVariable.Assign(var_obj, value)
        if isinstance(result, list): 
            ctx.extend(result)
        else: 
            ctx.append(result)

    def __getattr__(self, name):
        if name in self._vars: 
            # FIX: Return the RAW Var object (No Proxy)
            return self._vars[name]
        raise AttributeError(f"Var '{name}' not found.")

# ==========================================
# 5. EXPORTS
# ==========================================
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
    Else = Else
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

def Function(*args, **kwargs):
    block = DFFunction(*args, **kwargs)
    return ContextBlock(block)