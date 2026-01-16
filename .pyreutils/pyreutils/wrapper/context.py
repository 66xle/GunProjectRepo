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