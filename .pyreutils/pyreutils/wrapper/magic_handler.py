from ..alias.SetVariable import SetVariable as _SetVariable
from .context import _get_current_context
from .math_ops import MathOp
from .smart_wrapper import OptimisticOp

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
                ctx.append(_SetVariable.Assign(var_obj, value.to_math()))
            
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