from .context import _get_current_context, ContextBlock

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
            
            # CASE A: Container (If/Repeat) -> Return ContextBlock with blocks
            if is_container and isinstance(result, list) and len(result) >= 2:
                close_block = result[-1]      
                immediate_blocks = result[:-1] 
                
                # FIX: Do NOT ctx.extend() here. Pass logic to ContextBlock.
                return ContextBlock(immediate_blocks, close_block=close_block, name=f"{self._cls.__name__}.{name}")

            # CASE B: Standard Block
            else:
                # Standard blocks (Action) are added immediately
                if isinstance(result, list):
                    blocks = result
                    main_block = result[-1] if result else None
                else:
                    blocks = [result]
                    main_block = result

                ctx = _get_current_context()
                if ctx is not None: 
                    ctx.extend(blocks)
                
                if name == "Function":
                     return ContextBlock(main_block, name="Function")
                return main_block
        return wrapper

class HeaderEmitter:
    def __init__(self, original_class):
        self._cls = original_class

    def __getattr__(self, name):
        original_attr = getattr(self._cls, name)
        if not callable(original_attr): 
            return original_attr

        def wrapper(*args, **kwargs):
            result = original_attr(*args, **kwargs)
            # FIX: Do not process here, just wrap.
            return ContextBlock(result, name=f"{self._cls.__name__}.{name}")
            
        return wrapper