from dfpyre import Var, GameValue, Number
from ..alias.SetVariable import SetVariable as _SetVariable
from .context import _get_current_context

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
        
        # --- COLOR CODES ---
        RED = "\033[91m"
        CYAN = "\033[96m"
        BOLD = "\033[1m"
        RESET = "\033[0m"

        def _convert_segment(obj):
            if isinstance(obj, Var): 
                return f'%var({obj.name})'
            
            # --- ERROR: Colored Output ---
            if isinstance(obj, GameValue):
                raise TypeError(
                    f"\n{RED}{BOLD}✖ CRITICAL ERROR: Invalid GameValue Usage{RESET}\n"
                    f"{RED}Cannot use GameValue '{obj}' inside complex math or function parameters.{RESET}\n"
                    f"{CYAN}✔ FIX: Assign the GameValue to a Variable first (e.g. v.temp = GameValue), then use v.temp.{RESET}\n"
                )
            
            return str(obj)

        parts.append(_convert_segment(self.source))
        
        for _, val, symbol in self.ops:
            parts.append(f' {symbol} {_convert_segment(val)}')
            
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
def _patch_methods(cls):
    # 1. Math Ops (Var + 5) -> Returns MathOp object
    cls.__add__ = lambda self, o: MathOp(self)._add_op('Add', o, '+')
    cls.__sub__ = lambda self, o: MathOp(self)._add_op('Subtract', o, '-')
    cls.__mul__ = lambda self, o: MathOp(self)._add_op('Multiply', o, '*')
    cls.__truediv__ = lambda self, o: MathOp(self)._add_op('Divide', o, '/')
    cls.__mod__ = lambda self, o: MathOp(self)._add_op('Remainder', o, '%')
    
    # 2. Reverse Math (5 + Var)
    cls.__radd__ = lambda self, o: MathOp(o)._add_op('Add', self, '+')
    cls.__rsub__ = lambda self, o: MathOp(o)._add_op('Subtract', self, '-')
    cls.__rmul__ = lambda self, o: MathOp(o)._add_op('Multiply', self, '*')
    cls.__rtruediv__ = lambda self, o: MathOp(o)._add_op('Divide', self, '/')
    cls.__rmod__ = lambda self, o: MathOp(o)._add_op('Remainder', self, '%')
    
    # 3. In-Place Assignments (v.x += 1)
    # These execute immediately and return 'self' to satisfy Python's assignment logic
    cls.__iadd__ = lambda self, o: (_emit_inplace(_SetVariable.Increment(self, o)) or self)
    cls.__isub__ = lambda self, o: (_emit_inplace(_SetVariable.Decrement(self, o)) or self)
    # Note: Multiply/Divide in DF takes [Target, Target, Source]
    cls.__imul__ = lambda self, o: (_emit_inplace(_SetVariable.Multiply(self, [self, o])) or self)
    cls.__idiv__ = lambda self, o: (_emit_inplace(_SetVariable.Divide(self, [self, o])) or self)

_patch_methods(Var)
_patch_methods(GameValue)