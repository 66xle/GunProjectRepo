import sys
import inspect
import atexit

_context_stack = []
_pending_containers = [] 

def _get_current_context():
    if _context_stack: 
        return _context_stack[-1]
    return None

def _check_unclosed_blocks():
    """
    Called at script exit. Checks if any containers were abandoned.
    """
    for block in _pending_containers:
        if not block._is_entered:
            RED = "\033[91m"
            CYAN = "\033[96m"
            BOLD = "\033[1m"
            RESET = "\033[0m"
            
            sys.stderr.write(
                f"\n{RED}{BOLD}✖ FATAL ERROR: Missing 'with' keyword!{RESET}\n"
                f"{RED}You defined a '{block.name}' block but didn't enter it.{RESET}\n"
                f'{CYAN}  File "{block.origin_file}", line {block.origin_line}{RESET}\n'
                f"Correct usage: {BOLD}with {block.name}(...):{RESET}\n\n"
            )

atexit.register(_check_unclosed_blocks)

class ContextBlock:
    def __init__(self, start_blocks, close_block=None, name="Block"):
        # ==========================================================
        # 1. CRITICAL: ASSIGN ATTRIBUTES FIRST (Prevents Recursion)
        # ==========================================================
        self.start_blocks = start_blocks if isinstance(start_blocks, list) else [start_blocks]
        self.close_block = close_block
        self.name = name
        self._is_entered = False
        
        self.origin_file = "Unknown"
        self.origin_line = 0
        
        # ==========================================================
        # 2. STACK TRACE LOGIC
        # ==========================================================
        try:
            # Smart Stack Trace: Filter out pyreutils library files
            for frame_info in inspect.stack():
                frame_file = frame_info.filename
                if "pyreutils" not in frame_file and "importlib" not in frame_file:
                    self.origin_file = frame_file
                    self.origin_line = frame_info.lineno
                    break     
        except Exception:
            try:
                # Fallback
                frame = inspect.stack()[2]
                self.origin_file = frame.filename
                self.origin_line = frame.lineno
            except Exception:
                pass
            
        # ==========================================================
        # 3. REGISTRY LOGIC
        # ==========================================================
        # Now it is safe to check self.start_blocks because it is assigned
        has_blocks = hasattr(self.start_blocks[0], 'codeblocks')
        is_container = (self.close_block is not None) or has_blocks
        
        if is_container:
            _pending_containers.append(self)
        
    def __enter__(self):
        self._is_entered = True
        
        if hasattr(self.start_blocks[0], 'codeblocks'):
             if not self.start_blocks[0].codeblocks:
                 self.start_blocks[0].codeblocks = []
             _context_stack.append(self.start_blocks[0].codeblocks)
        else:
            ctx = _get_current_context()
            if ctx is not None:
                ctx.extend(self.start_blocks)
        
        return self.start_blocks[0]

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.close_block is not None:
            ctx = _get_current_context()
            if ctx is not None: 
                ctx.append(self.close_block)
            return
        _context_stack.pop()

    def __getattr__(self, name):
        """
        Proxies attributes to the underlying DF object.
        """
        # SAFETY CHECK: If __init__ fails or attributes are missing, 
        # do not loop infinitely looking for them.
        if name in ('start_blocks', 'close_block', '_is_entered'):
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
            
        return getattr(self.start_blocks[0], name)