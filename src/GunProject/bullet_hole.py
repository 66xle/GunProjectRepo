from dfpyre import *

BULLET_SCALE = 0.075
BULLET_3D_SCALE = 0.001

def Local(name: str, scope: str = 'local'):
    return Variable(name, scope)

# Define the process
template = Process('BulletHole2', codeblocks=[
    # --- PHASE 1: COORDINATE CALCULATION ---
    # Get Pitch and Yaw from the Hit Location
    SetVariable.GetCoord(Local('num-Pitch'), Local('loc-Hit'), coordinate='Pitch'),
    SetVariable.GetCoord(Local('num-Yaw'), Local('loc-Hit'), coordinate='Yaw'),

    # --- ALIGNMENT LOGIC ---
    # Check if Pitch is 0 (Wall)
    IfVariable.Equals(Local('num-Pitch'), 0, codeblocks=[
        SetVariable.AlignLoc(Local('loc-CenterXZ'), Local('loc-Hit'), coordinates="X and Z"),

        IfVariable.Equals(Local('num-Yaw'), [90, -90], codeblocks=[
            # East/West: Use Center X, Original Z
            SetVariable.GetCoord(Local('num-X'), Local('loc-CenterXZ'), coordinate='X'),
            SetVariable.SetCoord(Local('loc-Hit'), Local('num-X'), coordinate='X')
        ]),
        Else(codeblocks=[
            # North/South: Use Center Z, Original X
            SetVariable.GetCoord(Local('num-Z'), Local('loc-CenterXZ'), coordinate='Z'),
            SetVariable.SetCoord(Local('loc-Hit'), Local('num-Z'), coordinate='Z')
        ])
        # Else(codeblocks=[
        # ])
    ]),
    Else(codeblocks=[
        # Floor/Ceiling Logic (Pitch 90/-90) -> Align Y only
        SetVariable.AlignLoc(Local('loc-Hit'), coordinates='Only Y')
    ]),

    # --- OFFSET LOGIC ---
    # Conditional Z-fighting fix for specific angles
    # IfVariable.Equals(Local('num-Yaw'), [0, -90], codeblocks=[
    #     IfVariable.Equals(Local('num-Pitch'), [0, -90], codeblocks=[
    #         # Shift backward slightly
    #         SetVariable.ShiftInDirection(Local('loc-Hit'), -0.1)
    #     ])
    # ]),
    
    # Final surface offset (prevent clipping)
    SetVariable.ShiftInDirection(Local('loc-Hit'), 0.501),

    # --- RENDER ---
    # Spawn the block display at the calculated location
    GameAction.SpawnBlockDisp(Local('loc-Hit'), Item('black_concrete')),

    # --- SCALING ---
    # Apply scale based on orientation (using the previously calculated Pitch/Yaw)
    IfVariable.Equals(Local('num-Pitch'), 0, codeblocks=[
        IfVariable.Equals(Local('num-Yaw'), [90, -90], codeblocks=[
            # East/West Wall: Flatten X
            EntityAction.DisplayScale(BULLET_3D_SCALE, BULLET_SCALE, BULLET_SCALE),
            EntityAction.DispTranslation(0, -BULLET_SCALE/2, -BULLET_SCALE/2)
        ]),
        Else(codeblocks=[
            # North/South Wall: Flatten Z
            EntityAction.DisplayScale(BULLET_SCALE, BULLET_SCALE, BULLET_3D_SCALE),
            EntityAction.DispTranslation(-BULLET_SCALE/2, -BULLET_SCALE/2, 0)
        ])
    ]),
    Else(codeblocks=[
        # Floor/Ceiling: Flatten Y
        EntityAction.DisplayScale(BULLET_SCALE, BULLET_3D_SCALE, BULLET_SCALE),
        EntityAction.DispTranslation(-BULLET_SCALE/2, 0, -BULLET_SCALE/2)
    ]),

    # --- CLEANUP ---
    # Capture the Entity UUID
    SetVariable.Assign(Local('str-BulletUUID'), GameValue('UUID', 'LastEntity')),
    
    # Wait 3 seconds
    Control.Wait(3, 'Seconds'),
    
    # Reselect and Remove
    SelectObject.EntityName(Local('str-BulletUUID')),
    EntityAction.Remove()
])

template.build_and_send()