from pyreutils.wrapper import *

item_FireModel = local('item-FireModel')
item_IdleModel = local('item-IdleModel')

with Process('FireModel') as f:
    # Set firing model
    SetVariable.SetModelDataNums(item_FireModel, '%default item-MainHand', 2)
    PlayerAction.SetSlotItem(item_FireModel, '%default num-HotbarSlot')

    # Wait for firing duration
    Control.Wait('num-Wait')

    # Set idle model
    SetVariable.SetModelDataNums(item_IdleModel, '%default item-MainHand', 1)
    PlayerAction.SetSlotItem(item_IdleModel, '%default num-HotbarSlot')

f.build_and_send()
