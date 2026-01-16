from pyreutils.wrapper import *

loc_Position1 = Var('loc-Position1', 'local')
loc_Position2 = Var('loc-Position2', 'local')
num_Damage = Var('num-Damage', 'line')
num_YShootBullet = Var('num-YShootBullet', 'local')
num_YPos1 = Var('num-YPos1', 'local')
num_YPos2 = Var('num-YPos2', 'local')
num_DealDMG = Var('num-DealDMG', 'local')
num_SetHealth = Var('num-SetHealth', 'local')
loc_Hit = Var('loc-Hit', 'local')

victim_location = GameValue('Location', 'Selection')
victim_health = GameValue('Current Health', 'Selection')

temp = Var('num-Temp', 'local')

v = MagicVarHandler(locals())

with PlayerEvent.Chat() as f:
    v.temp = GameValue('Current Health')
    v.loc_Position1 = 5 - v.temp + 5
    Else()
    
    PlayerAction.SendMessage()

# with Function('025 DMGPlayer', Parameter('num-Damage', ParameterType.NUMBER)) as f:
#     v.loc_Position1 = SetVariable.ShiftAllAxes(victim_location, -0.5, 0, 0.5)
#     v.loc_Position2 = SetVariable.ShiftAllAxes(victim_location, 0.5, 1.8, -0.5)
#     with IfPlayer.IsSneaking(target=Target.SELECTION):
#         v.loc_Position2 = SetVariable.ShiftY(-0.3)
#     v.num_YShootBullet = SetVariable.GetCoordY(loc_Hit)
#     v.num_YPos1 = SetVariable.GetCoordY(loc_Position1)
#     v.num_YPos2 = SetVariable.GetCoordY(loc_Position2)
#     with IfVariable.InRange(num_YShootBullet, num_YPos1, num_YPos2):
#         v.num_YShootBullet += 1.5
#         with IfPlayer.IsSneaking(target=Target.SELECTION):
#             v.loc_Position1 = SetVariable.ShiftY(-0.3)
#             v.loc_Position2 = SetVariable.ShiftY(-0.3)
#         v.num_DealDMG = num_Damage
#         with IfVariable.InRange(num_YShootBullet, num_YPos1, num_YPos2):
#             v.num_DealDMG *= 2.5
#         PlayerAction.PlaySound(Sound('Item Frame Add Item', 2.0, 2.0), target=Target.DEFAULT)
#         v.num_SetHealth = victim_health - num_DealDMG
#         PlayerAction.PlaySound(Sound('Player Hurt', 1.0, 2.0), target=Target.SELECTION)
#         PlayerAction.HurtAnimation(target=Target.SELECTION)
#         with IfVariable.LessEqual(num_SetHealth, 0):
#             v.num_SetHealth = 20
#             PlayerAction.SendMessage(Text('<dark_green>%default </dark_green><yellow>killed </yellow><red>%selected'), target=Target.ALL_PLAYERS)
#             PlayerAction.SendTitle(Text('<red>'), Text('<gray>[<dark_green> ⚔ </dark_green>]<gray>'), 10, 0, 0, target=Target.DEFAULT)
#             PlayerAction.PlaySound(Sound('Experience Orb Pickup', 1.0, 2.0), target=Target.DEFAULT)
#         PlayerAction.SetHealth(num_SetHealth, target=Target.SELECTION)
#         SelectObject.Reset()
    
f.build_and_send()