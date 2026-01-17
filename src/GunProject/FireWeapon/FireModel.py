from pyreutils.wrapper import *

item_FireModel = local('item-FireModel')
item_IdleModel = local('item-IdleModel')

with Process('FireModel') as f:
    # Set firing model
    item_FireModel.v = SetV.SetModelDataNums('%default item-MainHand', 2)
    Player.SetSlotItem(item_FireModel, Num('%var(%default num-HotbarSlot)'))

    # Wait for firing duration
    Control.Wait(Num('%var(num-Wait)'))

    # Set idle model
    item_IdleModel.v = SetV.SetModelDataNums('%default item-MainHand', 1)
    Player.SetSlotItem(item_IdleModel, Num('%var(%default num-HotbarSlot)'))

f.build_and_send()
