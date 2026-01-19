from .math_ops import MathOp
from .context import _get_current_context

class OptimisticOp:
    def __init__(self, name, args, created_block=None):
        self.name = name
        self.args = args
        self.created_block = created_block
        
    def __neg__(self):
        """
        Enables the syntax: -Select.PlayerName(...)
        This grabs the block that was just created and sets inverted=True.
        """
        if self.created_block:
            # Helper function to invert a single block
            def _invert(block):
                if hasattr(block, 'data') and isinstance(block.data, dict):
                    block.data['attribute'] = 'NOT'
            
            _invert(self.created_block)
        
        return self

class SmartWrapper:
    def __init__(self, target_class):
        """
        A generic wrapper that:
        1. Auto-adds the generated block to the Context.
        2. Converts MathOp arguments to valid DF numbers.
        3. Returns an OptimisticOp for variable assignment.
        """
        self.target_class = target_class

    def __getattr__(self, name):
        # Dynamically get the method from the target class (_SetVariable, _SelectObject, etc.)
        original_method = getattr(self.target_class, name)
        
        def wrapper(*args, **kwargs):
            # --- 1. CLEAN ARGUMENTS (MathOp -> Number) ---
            clean_args = []
            for arg in args:
                if isinstance(arg, MathOp): 
                    clean_args.append(arg.to_math())
                else: 
                    clean_args.append(arg)
            
            # --- 2. EXECUTE & CONTEXTUALIZE ---
            try:
                # Call the actual library method
                result = original_method(*clean_args, **kwargs)
                
                # Add to the current 'with' block automatically
                ctx = _get_current_context()
                if ctx is not None:
                    if isinstance(result, list): 
                        ctx.extend(result)
                    else: 
                        ctx.append(result)
                
                # --- 3. RETURN OPTIMISTIC OP ---
                # This allows logic like: v.var = SelectObject.Random()
                return OptimisticOp(name, clean_args, created_block=result)
                
            except Exception:
                # Fallback if something fails (keeps the script alive)
                return OptimisticOp(name, clean_args, created_block=None)
            
        return wrapper