from ..alias.SetVariable import SetVariable as _SetVariable
from .math_ops import MathOp
from .context import _get_current_context

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