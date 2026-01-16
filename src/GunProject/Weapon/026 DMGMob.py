from dfpyre import *

Function('026 DMGMob', Parameter('num-Damage', ParameterType.NUMBER), codeblocks=[
    SetVariable.ShiftAllAxes(Variable('loc-Position1', 'local'), GameValue('Location', 'Selection'), -0.5, 0, 0.5),
    SetVariable.ShiftAllAxes(Variable('loc-Position2', 'local'), GameValue('Location', 'Selection'), 0.5, 2, -0.5),
    SetVariable.GetCoord(Variable('num-YMob', 'local'), Variable('loc-Hit', 'local'), Variable('loc-ShootBullet', 'local'), coordinate='Y'),
    SetVariable.GetCoord(Variable('num-YMobPos1', 'local'), Variable('loc-Position1', 'local'), coordinate='Y'),
    SetVariable.GetCoord(Variable('num-YMobPos2', 'local'), Variable('loc-Position2', 'local'), coordinate='Y'),
    IfVariable.InRange(Variable('num-YMob', 'local'), Variable('num-YMobPos1', 'local'), Variable('num-YMobPos2', 'local'), codeblocks=[
        SetVariable.Increment(Variable('num-YMobPos1', 'local'), 1.5),
        SetVariable.Assign(Variable('num-DMGDealt', 'local'), Variable('num-Damage', 'line')),
        IfVariable.InRange(Variable('num-YMob', 'local'), Variable('num-YMobPos1', 'local'), Variable('num-YMobPos2', 'local'), codeblocks=[
            SetVariable.Multiply(Variable('num-DMGDealt', 'local'), Variable('num-Damage', 'local'), 2.5)
        ]),
        PlayerAction.PlaySound(Sound('Item Frame Add Item', 2.0, 2.0), target=Target.DEFAULT),
        PlayerAction.SendMessage(Text('hit'), target=Target.DEFAULT),
        EntityAction.Damage(Variable('num-DMGDealt', 'local')),
        EntityAction.SetInvulTicks(0),
        SetVariable.Assign(Variable('num-Health', 'local'), GameValue('Current Health', 'Selection')),
        EntityAction.SetName(Text('%var(num-Health)')),
        IfVariable.LessEqual(GameValue('Current Health', 'Selection'), 100, codeblocks=[
            Control.Wait(),
            EntityAction.Remove()
        ]),
        SelectObject.Reset()
    ])
])