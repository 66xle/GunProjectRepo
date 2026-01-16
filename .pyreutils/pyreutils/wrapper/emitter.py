# pyreutils/wrapper/emitter.py
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
    
class HeaderEmitter:
    """
    Wraps classes like PlayerEvent/EntityEvent.
    Usage: with PlayerEvent.Join() as e:
    """
    def __init__(self, original_class):
        self._cls = original_class

    def __getattr__(self, name):
        original_attr = getattr(self._cls, name)
        if not callable(original_attr): 
            return original_attr

        def wrapper(*args, **kwargs):
            # 1. Create the Block (e.g. PlayerEvent.Join)
            result = original_attr(*args, **kwargs)
            
            # 2. Wrap it in ContextBlock so it acts as a Root
            return ContextBlock(result)
            
        return wrapper