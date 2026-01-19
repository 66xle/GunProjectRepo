from pyreutils.wrapper import *

with Function("test") as f:
    -Select.PlayerName("%default")
    
f.build_and_send()