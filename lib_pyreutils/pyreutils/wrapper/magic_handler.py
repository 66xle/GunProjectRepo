from dfpyre import Var
from ..alias.SetVariable import SetVariable as _SetVariable
from ..alias.SelectObject import SelectObject as _SelectObject # Import SelectObject
from .context import _get_current_context
from .math_ops import MathOp
from .smart_wrapper import OptimisticOp

# ==========================================
# 1. SHARED ASSIGNMENT LOGIC
# ==========================================
def _perform_assignment(var_obj, value):
    """
    Handles assignment logic.
    """
    # Ignore self-assignment
    if value is var_obj:
        return

    ctx = _get_current_context()

    # --- CASE 1: MATH OPERATIONS ---
    if isinstance(value, MathOp):
        if value.is_complex():
            ctx.append(_SetVariable.Assign(var_obj, value.to_math()))
        else:
            ops = value.ops
            source = value.source
            if ops:
                first_method_name, first_val, _ = ops[0]
                method = getattr(_SetVariable, first_method_name)
                if isinstance(first_val, list):
                    ctx.append(method(var_obj, [source, *first_val]))
                else:
                    ctx.append(method(var_obj, [source, first_val]))
                for method_name, val, _ in ops[1:]:
                    method = getattr(_SetVariable, method_name)
                    if isinstance(val, list):
                        ctx.append(method(var_obj, *val))
                    else:
                        ctx.append(method(var_obj, val))
            else:
                ctx.append(_SetVariable.Assign(var_obj, source))
        return

    # --- CASE 2: OPTIMISTIC OPS (Smart Wrapper Results) ---
    if isinstance(value, OptimisticOp):
        # 1. Rollback the block if it was auto-added by the SmartWrapper
        if value.created_block is not None:
            if isinstance(value.created_block, list):
                for b in reversed(value.created_block):
                    if ctx and ctx[-1] is b:
                        ctx.pop()
            elif ctx and ctx[-1] is value.created_block:
                ctx.pop()

        # 2. PRIORITY 1: Try SetVariable
        if hasattr(_SetVariable, value.name):
            method = getattr(_SetVariable, value.name)
            result = method(var_obj, *value.args)
            if isinstance(result, list): 
                ctx.extend(result)
            else: 
                ctx.append(result)
            return
        
        # 3. PRIORITY 2: Try SelectObject (Fallback)
        # This treats 'Select.Method' as if it were 'SetVar.Method', 
        # passing the variable as the first argument.
        if hasattr(_SelectObject, value.name):
            method = getattr(_SelectObject, value.name)
            try:
                result = method(var_obj, *value.args)
                if isinstance(result, list): 
                    ctx.extend(result)
                else: 
                    ctx.append(result)
                return
            except TypeError as e:
                # Provide a helpful error if the arguments don't match
                raise TypeError(
                    f"Failed to assign using 'Select.{value.name}'.\n"
                    f"The method exists, but it likely does not accept a Variable as the first argument.\n"
                    f"Python Error: {e}"
                )

        raise AttributeError(f"Neither SetVariable nor SelectObject has a method named '{value.name}'")

    # --- CASE 3: STANDARD ASSIGNMENT ---
    result = _SetVariable.Assign(var_obj, value)
    if isinstance(result, list):
        ctx.extend(result)
    else:
        ctx.append(result)


# ==========================================
# 2. THE .v PROXY VARIABLE
# ==========================================
class ValueProxyVar(Var):
    """
    A subclass of Var that adds a .v property for assignment.
    """

    @property
    def v(self):
        """Getter: Returns self, so 'x = var.v' is just 'x = var'."""
        return self

    @v.setter
    def v(self, value):
        """Setter: Triggers the assignment logic (SetVariable/Math)."""
        _perform_assignment(self, value)


# ==========================================
# 3. SCOPE HANDLER (The Factory)
# ==========================================
class MagicVarHandler:
    def __init__(self, scope_name):
        self._scope = scope_name
        self._cache = {}

    def __call__(self, name):
        """
        Factory Method: local("Variable Name")
        Returns a ValueProxyVar bound to this name.
        """
        # Check cache (Case-sensitive matching for DF names)
        if name in self._cache:
            return self._cache[name]

        # Create new Proxy Var
        # We DO NOT replace underscores here, because the user provided a string explicitly.
        # local("My_Var") -> %local(My_Var)
        new_var = ValueProxyVar(name, self._scope)
        self._cache[name] = new_var
        return new_var

    # Optional: Keep the dot syntax for quick access if you want both
    def __getattr__(self, name):
        formatted_name = name.replace("_", "-")
        return self.__call__(formatted_name)

    # Optional: Keep direct assignment via local.name = 5
    def __setattr__(self, name, value):
        if name.startswith("_"):
            super().__setattr__(name, value)
            return
        formatted_name = name.replace("_", "-")
        var_obj = self.__call__(formatted_name)
        _perform_assignment(var_obj, value)
