# ruff: noqa: F403, F405, E402
import sys
import os

# Add the parent directory to Python's search path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from Utils.alias import *

# Variables
loc = Var('loc-Check', 'local')
hit_loc = Var('loc-Hit', 'local')
y_velocity = Var('num-YVelocity', 'local')
y_hit = Var('num-HitY', 'local')
raycast_loc = Var('loc-Raycast', 'local')

player_pos = GameValue.Location()
player_velocity = GameValue.Velocity()

# Constants
JUMP_ENABLE = 0.42
JUMP_DISABLE = 0
BUFFER_DISTANCE = 1.5  # How far above ground we "Prepare" the jump..
FIRST_RAYCAST_LENGTH = 2
SECOND_RAYCAST_LENGTH = 4


template = Function('PreVault', codeblocks=[
    
    # 1. LOGIC: If Player Airborne & Floor Nearby
    IfPlayer.IsGrounded(inverted=True, codeblocks=[
        # 2. Setup Raycast Origin
        SetVariable.SetPitch(loc, player_pos, 90), # Look Down
        
        # 3. Check for floor nearby
        SetVariable.Raycast(hit_loc, loc, BUFFER_DISTANCE, block_collision='Solid blocks'),
        
        SetVariable.GetVectorY(y_velocity, player_velocity),
        If.GreaterEqual(y_velocity, 0,         codeblocks=[Control.PrintDebug("Y Velocity >= 0: %var(num-YVelocity)"), PlayerAction.JumpStrength(JUMP_DISABLE), Control.Return()]),
        IfGame.InBlock(hit_loc, inverted=True, codeblocks=[Control.PrintDebug("2nd Raycast hit air"), PlayerAction.JumpStrength(JUMP_DISABLE), Control.Return()]), 
        
        Control.PrintDebug("Airborne & Floor nearby"),
        SetVariable.GetY(y_hit, hit_loc),
        SetVariable.SetY(raycast_loc, player_pos, Num("%math(%var(num-HitY) + 0.5)")),
        
        CallFunction('VaultCheck', raycast_loc, SECOND_RAYCAST_LENGTH),
    ]),
    Else(codeblocks=[
        CallFunction('VaultCheck', player_pos, FIRST_RAYCAST_LENGTH),
    ]),
])

template.build_and_send()