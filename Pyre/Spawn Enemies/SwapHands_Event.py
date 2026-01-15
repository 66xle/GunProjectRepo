# ruff: noqa: F403, F405, E402
from dfpyre import *

PlayerEvent.SwapHands([
    CallFunction('poisson_disc_sampling', 100, 100, 5),
    Control.PrintDebug('points', Variable('points', 'local')),
    SetVariable.Assign(Variable('origin', 'local'), Location(7.5, 50.0, 18.5)),
    SelectObject.AllEntities(),
    EntityAction.Remove(),
    SelectObject.Reset(),
    Repeat.ForEach(Variable('point', 'local'), Variable('points', 'local'), codeblocks=[
        Control.Wait(0),
        SetVariable.ShiftOnVector(Variable('spawn_pos', 'local'), Variable('origin', 'local'), Variable('point', 'local')),
        GameAction.SpawnArmorStand(Variable('spawn_pos', 'local')),
        EntityAction.MiscAttribute(20, attribute='Follow range'),
        EntityAction.SetAI()
    ])
])