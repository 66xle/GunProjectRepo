# ruff: noqa: F403, F405, E402
import sys
import os

# Add the parent directory to Python's search path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from Utils.alias import *

# Constants
JUMP_STRENGTH = 0.42
JUMP_DISABLED = 0

# Variables
loc = Var('loc-Raycast', 'line')
raycast_length = Var('num-RaycastLength', 'line')
hit_pos = Var('loc-Hit', 'local')
wall_dist = Var('num-WallDistance', 'local')
vec_debug = Var('vec-Debug', 'local')

# Game Values
player_loc = GameValue.Location()

loc_check = Var('loc-GroundCheck', 'local')
hit_pos = Var('loc-GroundHit', 'local')
is_grounded = Var('bool-IsGrounded', 'local')


def verify_clearance(error_message):
    """
    Checks for space above. Shifts UP, then Raycasts.
    """
    return [
        SetVariable.ShiftY(loc, 1),
        # We can safely use wall_dist here because this runs AFTER Step 4
        SetVariable.Raycast(hit_pos, loc, wall_dist, block_collision='Solid blocks'),
        IfGame.InBlock(hit_pos, codeblocks=[
            Control.PrintDebug(error_message),
            Control.Return()
        ])
    ]

template = Function('VaultCheck', [
                        Parameter('loc-Raycast', ParameterType.LOCATION, description="Raycast Origin"), 
                        Parameter('num-RaycastLength', ParameterType.NUMBER, description="Raycast Length")
                    ], codeblocks=[
    # 1. INITIALIZE
    PlayerAction.JumpStrength(JUMP_DISABLED),
    
    SetVariable.SetCoordPitch(loc, 0),
    SetVariable.AlignLoc(loc, coordinates='Only Y'),
    
    # 2. Find block in front
    SetVariable.Raycast(hit_pos, loc, raycast_length, block_collision='Solid blocks'),
    
    # (Optional: Visual Debugging)
    SetVariable.GetDirection(vec_debug, loc),
    SetVariable.SetVectorLength(vec_debug, raycast_length),
    PlayerAction.ParticleRay(Particle.Dust(), loc, vec_debug),
    
    # 3. GUARD: MUST HIT WALL
    IfGame.InBlock(hit_pos, inverted=True, codeblocks=[
        Control.PrintDebug("Fail: No wall in front"),
        Control.Return()
    ]),

    # 4. CALCULATE SPACING
    # We lock the distance now so upper checks don't reach further than the wall
    SetVariable.Distance(wall_dist, loc, hit_pos),
    
    # 5. GUARD: HEAD CHECK (1 Block Up)
    *verify_clearance("Fail: Head obstructed"), # The '*' unpacks the list returned by our helper function

    # 6. GUARD: CLIMB CHECK (2 Blocks Up)
    *verify_clearance("Fail: Ledge too high"),

    # 7. SUCCESS
    PlayerAction.JumpStrength(JUMP_STRENGTH),
    Control.PrintDebug("Success: Can Jump"),
])

template.build_and_send()