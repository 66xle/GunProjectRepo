from dfpyre import Particle

# 1. Save a reference to the ORIGINAL __init__ method
# We need this so we can still run the library's standard setup code.
_original_init = Particle.__init__

def fixed_init(self, *args, **kwargs):
    """
    Patched Particle __init__ to fix key naming issues in dfpyre.
    - 'duration' is renamed to 'time'
    - 'fade_rgb' is renamed to 'rgb_fade'
    """
    # 2. Call the original method manually
    # We pass 'self' explicitly because we are calling the unbound function.
    _original_init(self, *args, **kwargs)

    # 3. Apply the fix
    data = self.particle_data.get('data', {})
    
    if 'duration' in data:
        data['time'] = data.pop('duration')
        
    if 'fade_rgb' in data:
        data['rgb_fade'] = data.pop('fade_rgb')

def apply_patch():
    """
    Overwrites the Particle class __init__ with our fixed version.
    """
    Particle.__init__ = fixed_init