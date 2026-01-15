# ruff: noqa: F403, F405
from dfpyre import *

def Local(name: str, scope: str = 'local'):
    return Variable(name, scope)

# Define variables
loc = Local('loc')
hit_loc = Local('hit_loc')
check_loc = Local('check_loc')
raycast_length = Local('raycast_length')

# Define the process
template = Function('Vault2', codeblocks=[
    # 1. Default jump attribute to 0
    SetVariable.SetCoord(loc, GameValue('Location'), 0, coordinate='Pitch'),
    SetVariable.ShiftOnAxis(loc, 1, coordinate='Y'),
    
    # 3. Raycast to find the block in front
    SetVariable.Raycast(hit_loc, loc, 2, block_collision='Solid blocks'),
    
    # 4. Check if the raycast actually hit a block (Result is not Air)
    IfGame.InBlock(hit_loc, codeblocks=[
        SetVariable.Distance(raycast_length, loc, hit_loc),
        
        # Check 1st block above
        SetVariable.ShiftOnAxis(loc, 1, coordinate='Y'),
        SetVariable.Raycast(hit_loc, loc, raycast_length, block_collision='Solid blocks'),
        # CHANGE HERE
        IfGame.InBlock(hit_loc, inverted=True, codeblocks=[
            
            # Check 2nd block above
            SetVariable.ShiftOnAxis(loc, 1, coordinate='Y'),
            SetVariable.Raycast(hit_loc, loc, raycast_length, block_collision='Solid blocks'),
            IfGame.InBlock(hit_loc, inverted=True, codeblocks=[
                
                # If both are air, enable vaulting
                PlayerAction.MovementAttribute(0.42, attribute='Jump strength'),
                Control.Return()
            ])
        ])
    ]),
    PlayerAction.MovementAttribute(0, attribute='Jump strength')
])

template.build_and_send()