from dfpyre import Target
from dfpyre import GameValue as _GameValue

class GameValue(_GameValue):

    # region Statistics

    @staticmethod
    def CurrentHealth(target: Target=Target.DEFAULT):
        """
        Gets a target's remaining health points. ❤ = 2 Health

        :param Target target: The target to retrieve the current health of.
        :return Number: 0.0 (dead) up to the target's maximum health (20.0 by default)
        """
        return GameValue('Current Health', target.get_string_value())

    @staticmethod
    def MaximumHealth(target: Target=Target.DEFAULT):
        """
        Gets a target's maximum health points. ❤ = 2 Health

        :param Target target: The target to retrieve the maximum health of.
        :return Number: Maximum health, 1.0 or above
        """
        return GameValue('Maximum Health', target.get_string_value())

    @staticmethod
    def AbsorptionHealth(target: Target=Target.DEFAULT):
        """
        Gets a target's absorption health (golden hearts). ❤ = 2 Health

        :param Target target: The target to retrieve the absorption health of.
        :return Number: Absorption health
        """
        return GameValue('Absorption Health', target.get_string_value())

    @staticmethod
    def FoodLevel(target: Target=Target.DEFAULT):
        """
        Gets a target's remaining food points. 

        :param Target target: The target to retrieve the food level of.
        :return Number: 0 (starving) to 20 (full bar)
        """
        return GameValue('Food Level', target.get_string_value())

    @staticmethod
    def FoodSaturation(target: Target=Target.DEFAULT):
        """
        Gets a target's saturation level, which depends on the types of food consumed. If saturation is > 0.0, the player's food level will not drop.

        :param Target target: The target to retrieve the food saturation of.
        :return Number: 0.0 (minimum), up to the player's food level
        """
        return GameValue('Food Saturation', target.get_string_value())

    @staticmethod
    def FoodExhaustion(target: Target=Target.DEFAULT):
        """
        Gets a target's exhaustion level, which is increased by the player's actions. When exhaustion resets from 4.0 to 0.0, a player's saturation decreases by 1.

        :param Target target: The target to retrieve the food exhaustion of.
        :return Number: 0.0 (minimum) to 4.0 (reset point)
        """
        return GameValue('Food Exhaustion', target.get_string_value())

    @staticmethod
    def AttackDamage(target: Target=Target.DEFAULT):
        """
        Gets a target's attack damage, which has a base value that can be altered by items. Default base value = 1.0

        :param Target target: The target to retrieve the attack damage of.
        :return Number: 0.0 or higher (more damage)
        """
        return GameValue('Attack Damage', target.get_string_value())

    @staticmethod
    def AttackSpeed(target: Target=Target.DEFAULT):
        """
        Gets a target's attack speed, which has a base value that can be altered by items. Default base value = 4.0

        :param Target target: The target to retrieve the attack speed of.
        :return Number: 0.0 or higher (faster)
        """
        return GameValue('Attack Speed', target.get_string_value())

    @staticmethod
    def AttackCooldown(target: Target=Target.DEFAULT):
        """
        Gets a target's current attack cooldown as a percentage of the way to fully charged. 

        :param Target target: The target to retrieve the attack cooldown of.
        :return Number: 0.0 (fully uncharged) to 100.0 (fully charged)
        """
        return GameValue('Attack Cooldown', target.get_string_value())

    @staticmethod
    def AttackCooldownTicks(target: Target=Target.DEFAULT):
        """
        Gets the number of ticks it will take to fully charge a target's attack cooldown after attacking with their held item. This value is set to -1 if it will never recharge.

        :param Target target: The target to retrieve the attack cooldown ticks of.
        :return Number: 0.0 (instant) or above
        """
        return GameValue('Attack Cooldown Ticks', target.get_string_value())

    @staticmethod
    def ArmorPoints(target: Target=Target.DEFAULT):
        """
        Gets a target's armor points, which has a base value that can be altered by items. Default base value = 0.0

        :param Target target: The target to retrieve the armor points of.
        :return Number: 0.0 (no armor) to 20.0 (full bar)
        """
        return GameValue('Armor Points', target.get_string_value())

    @staticmethod
    def ArmorToughness(target: Target=Target.DEFAULT):
        """
        Gets a target's armor toughness, which has a base value that can be altered by items. Armor Toughness increases the amount of damage required to penetrate one armor point. Default base value = 0.0

        :param Target target: The target to retrieve the armor toughness of.
        :return Number: 0.0 or above (full set of diamond armor = 8.0)
        """
        return GameValue('Armor Toughness', target.get_string_value())

    @staticmethod
    def InvulnerabilityTicks(target: Target=Target.DEFAULT):
        """
        Gets a target's remaining ticks of invulnerability. This value is set to 10 upon taking damage.

        :param Target target: The target to retrieve the invulnerability ticks of.
        :return Number: 0 (can be hurt) or above (invulnerable)
        """
        return GameValue('Invulnerability Ticks', target.get_string_value())

    @staticmethod
    def ExperienceLevel(target: Target=Target.DEFAULT):
        """
        Gets a target's experience level. 

        :param Target target: The target to retrieve the experience level of.
        :return Number: 0 (no levels) or above
        """
        return GameValue('Experience Level', target.get_string_value())

    @staticmethod
    def ExperienceProgress(target: Target=Target.DEFAULT):
        """
        Gets a target's experience progress percentage to the next level. 

        :param Target target: The target to retrieve the experience progress of.
        :return Number: 0.0% (no progress) to 100.0% (next level)
        """
        return GameValue('Experience Progress', target.get_string_value())

    @staticmethod
    def FireTicks(target: Target=Target.DEFAULT):
        """
        Gets the remaining ticks a target is on fire for. 

        :param Target target: The target to retrieve the fire ticks of.
        :return Number: 0 (not on fire) or above (burning)
        """
        return GameValue('Fire Ticks', target.get_string_value())

    @staticmethod
    def FreezeTicks(target: Target=Target.DEFAULT):
        """
        Gets the remaining ticks a target is freezing for. 

        :param Target target: The target to retrieve the freeze ticks of.
        :return Number: 0 (not frozen) or above (freezing)
        """
        return GameValue('Freeze Ticks', target.get_string_value())

    @staticmethod
    def RemainingAir(target: Target=Target.DEFAULT):
        """
        Gets a target's remaining air ticks. One breath bubble is equal to 30 air ticks.

        :param Target target: The target to retrieve the remaining air of.
        :return Number: 0 (drowning) to 300 (maximum air)
        """
        return GameValue('Remaining Air', target.get_string_value())

    @staticmethod
    def FallDistance(target: Target=Target.DEFAULT):
        """
        Gets a target's distance fallen in blocks. Resets to 0 upon landing. Works on the Damage Event.

        :param Target target: The target to retrieve the fall distance of.
        :return Number: 0.0 (not falling) or higher (falling down)
        """
        return GameValue('Fall Distance', target.get_string_value())

    @staticmethod
    def HeldSlot(target: Target=Target.DEFAULT):
        """
        Gets a target's selected hotbar slot index. 

        :param Target target: The target to retrieve the held slot of.
        :return Number: 1 (leftmost slot) to 9 (rightmost slot)
        """
        return GameValue('Held Slot', target.get_string_value())

    @staticmethod
    def Ping(target: Target=Target.DEFAULT):
        """
        Gets the latency between a player and the server in milliseconds. 

        :param Target target: The target to retrieve the ping of.
        :return Number: Player ping 0-1000+
        """
        return GameValue('Ping', target.get_string_value())

    @staticmethod
    def SteerSidewaysMovement(target: Target=Target.DEFAULT):
        """
        While a player is steering an entity, gets the sideways movement of the steering. 

        :param Target target: The target to retrieve the steer sideways movement of.
        :return Number: -1 (right), 1 (left), or 0 (none)
        """
        return GameValue('Steer Sideways Movement', target.get_string_value())

    @staticmethod
    def SteerForwardMovement(target: Target=Target.DEFAULT):
        """
        While a player is steering an entity, gets the forward movement of the steering. 

        :param Target target: The target to retrieve the steer forward movement of.
        :return Number: -1 (backward), 1 (forward), or 0 (none)
        """
        return GameValue('Steer Forward Movement', target.get_string_value())

    @staticmethod
    def ItemUsageProgress(target: Target=Target.DEFAULT):
        """
        Gets the progress percentage of a target using their held item, such as food. Bows, crossbows and tridents remain at 100.0% until they are released.

        :param Target target: The target to retrieve the item usage progress of.
        :return Number: 0 (not using an item), or 0.0% (start) to 100.0%
        """
        return GameValue('Item Usage Progress', target.get_string_value())

    @staticmethod
    def FlightSpeed(target: Target=Target.DEFAULT):
        """
        Gets a target's flight speed as a percentage. 

        :param Target target: The target to retrieve the flight speed of.
        :return Number: Flight speed percentage (0% to 1000%)
        """
        return GameValue('Flight Speed', target.get_string_value())

    @staticmethod
    def WalkSpeed(target: Target=Target.DEFAULT):
        """
        Gets a target's walk speed as a percentage. 

        :param Target target: The target to retrieve the walk speed of.
        :return Number: Walk speed percentage (0% to 500%)
        """
        return GameValue('Walk Speed', target.get_string_value())

    @staticmethod
    def EntityWidth(target: Target=Target.DEFAULT):
        """
        Gets the width of an entity's bounding box. 

        :param Target target: The target to retrieve the entity width of.
        :return Number: Width in blocks
        """
        return GameValue('Entity Width', target.get_string_value())

    @staticmethod
    def EntityHeight(target: Target=Target.DEFAULT):
        """
        Gets the height of an entity's bounding box. 

        :param Target target: The target to retrieve the entity height of.
        :return Number: Height in blocks
        """
        return GameValue('Entity Height', target.get_string_value())

    # endregion Statistics

    # region Location

    @staticmethod
    def Location(target: Target=Target.DEFAULT):
        """
        Gets a target's location. 

        :param Target target: The target to retrieve the location of.
        :return Location: Location and rotation, at feet height
        """
        return GameValue('Location', target.get_string_value())

    @staticmethod
    def TargetBlockLocation(target: Target=Target.DEFAULT):
        """
        Gets the location of the block a target is looking at. 

        :param Target target: The target to retrieve the target block location of.
        :return Location: Block center
        """
        return GameValue('Target Block Location', target.get_string_value())

    @staticmethod
    def TargetBlockSide(target: Target=Target.DEFAULT):
        """
        Gets the side of the block a target is looking at as a direction. 

        :param Target target: The target to retrieve the target block side of.
        :return Vector: Block side
        """
        return GameValue('Target Block Side', target.get_string_value())

    @staticmethod
    def EyeLocation(target: Target=Target.DEFAULT):
        """
        Gets a target's location, but adjusted to its eye height. 

        :param Target target: The target to retrieve the eye location of.
        :return Location: Eye location and rotation
        """
        return GameValue('Eye Location', target.get_string_value())

    @staticmethod
    def XCoordinate(target: Target=Target.DEFAULT):
        """
        Gets the X coordinate of a target's position. 

        :param Target target: The target to retrieve the x-coordinate of.
        :return Number: Coordinate
        """
        return GameValue('X-Coordinate', target.get_string_value())

    @staticmethod
    def YCoordinate(target: Target=Target.DEFAULT):
        """
        Gets the Y coordinate of a target's position. 

        :param Target target: The target to retrieve the y-coordinate of.
        :return Number: Coordinate
        """
        return GameValue('Y-Coordinate', target.get_string_value())

    @staticmethod
    def ZCoordinate(target: Target=Target.DEFAULT):
        """
        Gets the Z coordinate of a target's position. 

        :param Target target: The target to retrieve the z-coordinate of.
        :return Number: Coordinate
        """
        return GameValue('Z-Coordinate', target.get_string_value())

    @staticmethod
    def MidpointLocation(target: Target=Target.DEFAULT):
        """
        Gets the location of the center of the target's bounding box. 

        :param Target target: The target to retrieve the midpoint location of.
        :return Location: Location and rotation, at midpoint
        """
        return GameValue('Midpoint Location', target.get_string_value())

    @staticmethod
    def Pitch(target: Target=Target.DEFAULT):
        """
        Gets the pitch (up/down rotation) of a target's position. -90.0° = up 90.0° = down

        :param Target target: The target to retrieve the pitch of.
        :return Number: -90.0 to 90.0
        """
        return GameValue('Pitch', target.get_string_value())

    @staticmethod
    def Yaw(target: Target=Target.DEFAULT):
        """
        Gets the yaw (left/right rotation) of a target's position. -180.0° & 180.0° = north -90.0° = east 0.0° = south 90.0° = west

        :param Target target: The target to retrieve the yaw of.
        :return Number: -180.0 to 180.0
        """
        return GameValue('Yaw', target.get_string_value())

    @staticmethod
    def BodyYaw(target: Target=Target.DEFAULT):
        """
        Gets the yaw (left/right rotation) of a target's body. -180.0° & 180.0° = north -90.0° = east 0.0° = south 90.0° = west

        :param Target target: The target to retrieve the body yaw of.
        :return Number: -180.0 to 180.0
        """
        return GameValue('Body Yaw', target.get_string_value())

    @staticmethod
    def StandingBlockLocation(target: Target=Target.DEFAULT):
        """
        Gets the location of the block that is supporting the player. When not grounded, this will return the location of the block at the target's location.

        :param Target target: The target to retrieve the standing block location of.
        :return Location: Block center
        """
        return GameValue('Standing Block Location', target.get_string_value())

    @staticmethod
    def SpawnLocation(target: Target=Target.DEFAULT):
        """
        Gets a target's original spawn location. 

        :param Target target: The target to retrieve the spawn location of.
        :return Location: Location this entity was created at
        """
        return GameValue('Spawn Location', target.get_string_value())

    @staticmethod
    def Velocity(target: Target=Target.DEFAULT):
        """
        Gets the speed at which a target is moving (not walking) in each direction. When grounded, a target may still have a downward velocity due to how gravity is applied.

        :param Target target: The target to retrieve the velocity of.
        :return Vector: Movement velocity
        """
        return GameValue('Velocity', target.get_string_value())

    @staticmethod
    def Direction(target: Target=Target.DEFAULT):
        """
        Gets the looking direction of a target's location as a vector. 

        :param Target target: The target to retrieve the direction of.
        :return Vector: Direction vector (length of 1.0)
        """
        return GameValue('Direction', target.get_string_value())

    # endregion Location

    # region Item

    @staticmethod
    def MainHandItem(target: Target=Target.DEFAULT):
        """
        Gets a target's currently held item. 

        :param Target target: The target to retrieve the main hand item of.
        :return Item: Item in the selected hotbar slot
        """
        return GameValue('Main Hand Item', target.get_string_value())

    @staticmethod
    def OffHandItem(target: Target=Target.DEFAULT):
        """
        Gets a target's currently held off hand item. 

        :param Target target: The target to retrieve the off hand item of.
        :return Item: Item in the offhand slot
        """
        return GameValue('Off Hand Item', target.get_string_value())

    @staticmethod
    def ArmorItems(target: Target=Target.DEFAULT):
        """
        Gets the items in a target's armor slots. Armor slots are ordered from helmet to boots.

        :param Target target: The target to retrieve the armor items of.
        :return List: Contains one Item entry for each armor slot (air if empty, 4 in total)
        """
        return GameValue('Armor Items', target.get_string_value())

    @staticmethod
    def HotbarItems(target: Target=Target.DEFAULT):
        """
        Gets a target's current hotbar items. 

        :param Target target: The target to retrieve the hotbar items of.
        :return List: Contains one Item entry for each hotbar slot (air if empty, 9 in total)
        """
        return GameValue('Hotbar Items', target.get_string_value())

    @staticmethod
    def InventoryItems(target: Target=Target.DEFAULT):
        """
        Gets a target's inventory items (includes hotbar). 

        :param Target target: The target to retrieve the inventory items of.
        :return List: Contains one Item entry for each inventory slot (air if empty, 36 in total)
        """
        return GameValue('Inventory Items', target.get_string_value())

    @staticmethod
    def CursorItem(target: Target=Target.DEFAULT):
        """
        Gets the item on a target's cursor (used when moving items in the inventory). 

        :param Target target: The target to retrieve the cursor item of.
        :return Item: Cursor item
        """
        return GameValue('Cursor Item', target.get_string_value())

    @staticmethod
    def InventoryMenuItems(target: Target=Target.DEFAULT):
        """
        Gets a target's current inventory menu items. Works with container inventories.

        :param Target target: The target to retrieve the inventory menu items of.
        :return List: Contains one Item entry for each menu slot (air if empty)
        """
        return GameValue('Inventory Menu Items', target.get_string_value())

    @staticmethod
    def SaddleItem(target: Target=Target.DEFAULT):
        """
        Gets a target's currently worn saddle or carpet. 

        :param Target target: The target to retrieve the saddle item of.
        :return Item: Item in the saddle/decor slot
        """
        return GameValue('Saddle Item', target.get_string_value())

    @staticmethod
    def EntityItem(target: Target=Target.DEFAULT):
        """
        The item form of the target. 

        :param Target target: The target to retrieve the entity item of.
        :return Item: The entity item
        """
        return GameValue('Entity Item', target.get_string_value())

    # endregion Item

    # region Information

    @staticmethod
    def Name(target: Target=Target.DEFAULT):
        """
        Gets a target's name. 

        :param Target target: The target to retrieve the name of.
        :return Component: Target name
        """
        return GameValue('Name ', target.get_string_value())

    @staticmethod
    def UUID(target: Target=Target.DEFAULT):
        """
        Gets a target's universally unique identifier. 

        :param Target target: The target to retrieve the uuid of.
        :return Text: Target UUID
        """
        return GameValue('UUID', target.get_string_value())

    @staticmethod
    def EntityType(target: Target=Target.DEFAULT):
        """
        Gets a target's entity type. 

        :param Target target: The target to retrieve the entity type of.
        :return Text: Entity type, e.g. "tipped_arrow" or "cow"
        """
        return GameValue('Entity Type', target.get_string_value())

    @staticmethod
    def GameMode(target: Target=Target.DEFAULT):
        """
        Gets a player's game mode. 

        :param Target target: The target to retrieve the game mode of.
        :return Text: Game mode: "survival", "creative", "adventure", "spectator"
        """
        return GameValue('Game Mode', target.get_string_value())

    @staticmethod
    def OpenInventoryTitle(target: Target=Target.DEFAULT):
        """
        Gets the title of a target's opened inventory. 

        :param Target target: The target to retrieve the open inventory title of.
        :return Component: Inventory title, or "none" if either no menu or the player's regular inventory is open
        """
        return GameValue('Open Inventory Title ', target.get_string_value())

    @staticmethod
    def PotionEffects(target: Target=Target.DEFAULT):
        """
        Gets a target's active potion effects. 

        :param Target target: The target to retrieve the potion effects of.
        :return List: Contains one Potion Effect entry for each active effect on the target
        """
        return GameValue('Potion Effects', target.get_string_value())

    @staticmethod
    def Vehicle(target: Target=Target.DEFAULT):
        """
        Gets the UUID of the entity that the target is riding. The ridden entity does not need to be of vehicular type. In a stack of entities, the vehicle is the bottom entity.

        :param Target target: The target to retrieve the vehicle of.
        :return Text: UUID of the ridden entity, or "none" if the target is not riding one
        """
        return GameValue('Vehicle', target.get_string_value())

    @staticmethod
    def Passengers(target: Target=Target.DEFAULT):
        """
        Gets the UUIDs of any entities riding a target. 

        :param Target target: The target to retrieve the passengers of.
        :return List: Contains one String entry (UUID) for each passenger riding the target (Empty List if the target has no passengers)
        """
        return GameValue('Passengers ', target.get_string_value())

    @staticmethod
    def LeadHolder(target: Target=Target.DEFAULT):
        """
        Gets the entity that is holding a target on a lead. 

        :param Target target: The target to retrieve the lead holder of.
        :return Text: Lead holder UUID, or "none" if the target is not on a lead
        """
        return GameValue('Lead Holder', target.get_string_value())

    @staticmethod
    def AttachedLeads(target: Target=Target.DEFAULT):
        """
        Gets all entities attached to to a target by a lead. 

        :param Target target: The target to retrieve the attached leads of.
        :return List: Contains one String entry (UUID) for each leashed entity (Empty List if the target holds no leads)
        """
        return GameValue('Attached Leads', target.get_string_value())

    @staticmethod
    def TargetedEntityUUID(target: Target=Target.DEFAULT):
        """
        Gets the UUID of the entity that the target is targeting. The targeted entity is the entity the target is chasing.

        :param Target target: The target to retrieve the targeted entity uuid of.
        :return Text: UUID of the targeted entity, or "none" if the target is not chasing one
        """
        return GameValue('Targeted Entity UUID', target.get_string_value())

    @staticmethod
    def ProjectileShooterUUID(target: Target=Target.DEFAULT):
        """
        Gets the UUID of a projectile's shooter, or "none" if not set. 

        :param Target target: The target to retrieve the projectile shooter uuid of.
        :return Text: Shooter UUID
        """
        return GameValue('Projectile Shooter UUID', target.get_string_value())

    @staticmethod
    def DisplayEntityTranslation(target: Target=Target.DEFAULT):
        """
        Gets the translation of a display entity's transformation. 

        :param Target target: The target to retrieve the display entity translation of.
        :return Vector: Translation
        """
        return GameValue('Display Entity Translation', target.get_string_value())

    @staticmethod
    def DisplayEntityScale(target: Target=Target.DEFAULT):
        """
        Gets the scale of a display entity's transformation. 

        :param Target target: The target to retrieve the display entity scale of.
        :return Vector: Scale
        """
        return GameValue('Display Entity Scale', target.get_string_value())

    @staticmethod
    def Pose(target: Target=Target.DEFAULT):
        """
        Gets the target's pose. 

        :param Target target: The target to retrieve the pose of.
        :return Text: Pose: "dying" (dead), "fall_flying" (gliding), "sleeping", "sneaking", "spin_attack" (riptiding with a trident), "standing" (standing normally), "swimming" (swimming/crawling) Camel Only: "sitting" Frog Only: "croaking", "long_jumping", "using_tongue" Warden Only: "digging", "emerging", "roaring", "sniffing" Breeze Only: "inhaling", "shooting", "sliding"
        """
        return GameValue('Pose', target.get_string_value())

    @staticmethod
    def WeatherType(target: Target=Target.DEFAULT):
        """
        Gets a player's weather type. 

        :param Target target: The target to retrieve the weather type of.
        :return Text: Weather: "clear", "downfall"
        """
        return GameValue('Weather Type', target.get_string_value())

    @staticmethod
    def PickEntityResult(target: Target=Target.DEFAULT):
        """
        Gets the item that would be created when a player middle clicks the target in Creative mode. 

        :param Target target: The target to retrieve the pick entity result of.
        :return Spawn_egg: Item or air
        """
        return GameValue('Pick Entity Result', target.get_string_value())

    @staticmethod
    def ParticleVisibilityStatus(target: Target=Target.DEFAULT):
        """
        Gets the target's Particles setting. 

        :param Target target: The target to retrieve the particle visibility status of.
        :return Text: Particle Visibility Status: "all", "decreased", "minimal"
        """
        return GameValue('Particle Visibility Status', target.get_string_value())

    @staticmethod
    def PressedMovementKeys(target: Target=Target.DEFAULT):
        """
        Gets a list of all movement keys that are currently pressed by a player. 

        :param Target target: The target to retrieve the pressed movement keys of.
        :return List: Contains one String value for each movement type: "forward", "backward", "left", "right", "jump", "sneak", "sprint"
        """
        return GameValue('Pressed Movement Keys', target.get_string_value())

    # endregion Information

    # region Event

    @staticmethod
    def EventBlockLocation(target: Target=Target.DEFAULT):
        """
        Gets the location of the block in this event. 

        :param Target target: The target to retrieve the event block location of.
        :return Location: Block center
        """
        return GameValue('Event Block Location', target.get_string_value())

    @staticmethod
    def EventBlockSide(target: Target=Target.DEFAULT):
        """
        Gets the side of the block that was hit in this event as a direction. 

        :param Target target: The target to retrieve the event block side of.
        :return Vector: Block side
        """
        return GameValue('Event Block Side', target.get_string_value())

    @staticmethod
    def EventDamage(target: Target=Target.DEFAULT):
        """
        Gets the amount of damage dealt in this event. Includes damage reduction. ❤ = 2 Health

        :param Target target: The target to retrieve the event damage of.
        :return Number: 0.0 or above
        """
        return GameValue('Event Damage', target.get_string_value())

    @staticmethod
    def DamageEventCause(target: Target=Target.DEFAULT):
        """
        Gets the type of damage taken or dealt in this event. 

        :param Target target: The target to retrieve the damage event cause of.
        :return Text: Damage Cause: "block_explosion", "contact" (cactus), "cramming", "custom" (damage action), "dragon_breath", "drowning", "dryout", (fish on land), "entity_attack", "entity_explosion", "entity_sweep_attack", "fall", "falling_block", "fire" (in fire block), "fire_tick", "fly_into_wall", "freeze", "hot_floor" (magma block), "kill", "lava", "magic", "melting" (snowman), "poison", "projectile", "starvation", "suffocation", "thorns", "void", "wither", "world_border"
        """
        return GameValue('Damage Event Cause', target.get_string_value())

    @staticmethod
    def RawEventDamage(target: Target=Target.DEFAULT):
        """
        Gets the amount of damage dealt in this event before any damage reductions. ❤ = 2 Health

        :param Target target: The target to retrieve the raw event damage of.
        :return Number: 0.0 or above
        """
        return GameValue('Raw Event Damage', target.get_string_value())

    @staticmethod
    def EventDeathMessage(target: Target=Target.DEFAULT):
        """
        Gets the death message for this death event. 

        :param Target target: The target to retrieve the event death message of.
        :return Component: Death message
        """
        return GameValue('Event Death Message ', target.get_string_value())

    @staticmethod
    def EventHealAmount(target: Target=Target.DEFAULT):
        """
        Gets the amount of health regained in this event. ❤ = 2 Health

        :param Target target: The target to retrieve the event heal amount of.
        :return Number: Health regained
        """
        return GameValue('Event Heal Amount', target.get_string_value())

    @staticmethod
    def HealEventCause(target: Target=Target.DEFAULT):
        """
        Gets the reason the target regained health in this event. 

        :param Target target: The target to retrieve the heal event cause of.
        :return Text: Healing Cause: "natural" (natural regeneration), "magic" (instant health effect), "magic_regen" (regen effect), "custom" (code)
        """
        return GameValue('Heal Event Cause', target.get_string_value())

    @staticmethod
    def EventExplosionAffectedBlocks(target: Target=Target.DEFAULT):
        """
        Gets the locations of blocks affected by the explosion in this event. 

        :param Target target: The target to retrieve the event explosion affected blocks of.
        :return List: Contains one Location entry for each block
        """
        return GameValue('Event Explosion Affected Blocks', target.get_string_value())

    @staticmethod
    def EventPower(target: Target=Target.DEFAULT):
        """
        Gets the percentage of power this event was executed with. 

        :param Target target: The target to retrieve the event power of.
        :return Number: 0.0% to 100.0%
        """
        return GameValue('Event Power', target.get_string_value())

    @staticmethod
    def EventCommand(target: Target=Target.DEFAULT):
        """
        Gets the entire command line entered in this event. 

        :param Target target: The target to retrieve the event command of.
        :return Text: Command, with the first "@" excluded
        """
        return GameValue('Event Command', target.get_string_value())

    @staticmethod
    def EventCommandArguments(target: Target=Target.DEFAULT):
        """
        Gets the separated parts of the event command. 

        :param Target target: The target to retrieve the event command arguments of.
        :return List: Contains one String entry for each word in the command (split by " ")
        """
        return GameValue('Event Command Arguments', target.get_string_value())

    @staticmethod
    def EventItem(target: Target=Target.DEFAULT):
        """
        Gets the item in an item related event. 

        :param Target target: The target to retrieve the event item of.
        :return Item: Main item in event
        """
        return GameValue('Event Item', target.get_string_value())

    @staticmethod
    def EventHotbarSlot(target: Target=Target.DEFAULT):
        """
        Gets the hotbar slot being changed to in this event. 

        :param Target target: The target to retrieve the event hotbar slot of.
        :return Number: 1 (leftmost slot) to 9 (rightmost slot)
        """
        return GameValue('Event Hotbar Slot', target.get_string_value())

    @staticmethod
    def EventClickedSlotIndex(target: Target=Target.DEFAULT):
        """
        Gets the index of the clicked inventory slot in this event. 

        :param Target target: The target to retrieve the event clicked slot index of.
        :return Number: From 1 (first slot) up to the inventory's size
        """
        return GameValue('Event Clicked Slot Index', target.get_string_value())

    @staticmethod
    def EventClickedSlotItem(target: Target=Target.DEFAULT):
        """
        Gets the inventory item clicked on in this event. 

        :param Target target: The target to retrieve the event clicked slot item of.
        :return Item: Item in slot (before the click event)
        """
        return GameValue('Event Clicked Slot Item', target.get_string_value())

    @staticmethod
    def EventClickedSlotNewItem(target: Target=Target.DEFAULT):
        """
        Gets the inventory item clicked with in this event. 

        :param Target target: The target to retrieve the event clicked slot new item of.
        :return Item: Item in slot (after the click event)
        """
        return GameValue('Event Clicked Slot New Item', target.get_string_value())

    @staticmethod
    def CloseInventoryEventCause(target: Target=Target.DEFAULT):
        """
        Gets the reason the target's inventory was closed in this event. 

        :param Target target: The target to retrieve the close inventory event cause of.
        :return Text: Close Cause: "player", "code", "open_new", "teleport", "unloaded", "cant_use", "disconnect", "death", "unknown"
        """
        return GameValue('Close Inventory Event Cause', target.get_string_value())

    @staticmethod
    def InventoryEventClickType(target: Target=Target.DEFAULT):
        """
        Gets the click type in this inventory click event. 

        :param Target target: The target to retrieve the inventory event click type of.
        :return Text: Click Type: "left", "shift_left", "double_left", "right", "shift_right", "drop" (Q), "drop_stack" (Ctrl+Q), "copy" (middle click), "creative", "swap_offhand" (F), "swap_hotbar" (1 ... 9)
        """
        return GameValue('Inventory Event Click Type', target.get_string_value())

    @staticmethod
    def FishEventCause(target: Target=Target.DEFAULT):
        """
        Gets the cause of this fish event. 

        :param Target target: The target to retrieve the fish event cause of.
        :return Text: Event Type: "cast", "bite", "catch", "cancel", "cancel_block", "miss", "pull_entity"
        """
        return GameValue('Fish Event Cause', target.get_string_value())

    @staticmethod
    def TeleportEventCause(target: Target=Target.DEFAULT):
        """
        Gets the reason the player was teleported in this event. 

        :param Target target: The target to retrieve the teleport event cause of.
        :return Text: Teleport Cause: "code", "ender_pearl", "chorus_fruit", "unknown"
        """
        return GameValue('Teleport Event Cause', target.get_string_value())

    @staticmethod
    def TeleportLocation(target: Target=Target.DEFAULT):
        """
        Gets the location that will be teleported to in this event. 

        :param Target target: The target to retrieve the teleport location of.
        :return Location: Location
        """
        return GameValue('Teleport Location', target.get_string_value())

    @staticmethod
    def ExhaustionEventCause(target: Target=Target.DEFAULT):
        """
        Gets the reason the target became exhausted in this event. 

        :param Target target: The target to retrieve the exhaustion event cause of.
        :return Text: Exhaustion Cause: "attack", "block_mined", "custom", "crouch", "damaged", "hunger_effect", "jump", "jump_sprint", "none", "regen", "sprint", "swim", "walk", "walk_on_water", "walk_underwater"
        """
        return GameValue('Exhaustion Event Cause', target.get_string_value())

    @staticmethod
    def EventExhaustion(target: Target=Target.DEFAULT):
        """
        Gets the amount of exhaustion gained in this event. 

        :param Target target: The target to retrieve the event exhaustion of.
        :return Number: Number
        """
        return GameValue('Event Exhaustion', target.get_string_value())

    @staticmethod
    def TransformEventCause(target: Target=Target.DEFAULT):
        """
        Gets the reason the target transformed in this event. 

        :param Target target: The target to retrieve the transform event cause of.
        :return Text: Transform Cause: "cured" (Zombie Villager → Villager), "drowned" (Zombie → Drowned), "frozen" (Skeleton → Stray), "infection" (Villager → Zombie Villager), "metamorphosis" (Tadpole → Frog), "sheared" (Mooshroom → Cow), "split" (Slime → Small Slimes), "lightning", "piglin_zombified", "unknown"
        """
        return GameValue('Transform Event Cause', target.get_string_value())

    @staticmethod
    def EventTransformEntities(target: Target=Target.DEFAULT):
        """
        Gets the entities an entity transforms into. 

        :param Target target: The target to retrieve the event transform entities of.
        :return List: UUIDs of the new entity/entities
        """
        return GameValue('Event Transform Entities', target.get_string_value())

    @staticmethod
    def EventHitType(target: Target=Target.DEFAULT):
        """
        Gets the type of object that the projectile collided with 

        :param Target target: The target to retrieve the event hit type of.
        :return Text: Hit Type: "block", "entity"
        """
        return GameValue('Event Hit Type', target.get_string_value())

    @staticmethod
    def ProductID(target: Target=Target.DEFAULT):
        """
        Gets the ID of the product purchased. 

        :param Target target: The target to retrieve the product id of.
        :return Text: Product ID
        """
        return GameValue('Product ID', target.get_string_value())

    @staticmethod
    def EventMessage(target: Target=Target.DEFAULT):
        """
        The message sent in this event 

        :param Target target: The target to retrieve the event message of.
        :return Text: Chat message
        """
        return GameValue('Event Message', target.get_string_value())

    @staticmethod
    def EventSignText(target: Target=Target.DEFAULT):
        """
        Gets the sign text in this event. 

        :param Target target: The target to retrieve the event sign text of.
        :return List: Contains one String entry for each sign line.
        """
        return GameValue('Event Sign Text', target.get_string_value())

    @staticmethod
    def EventSignSide(target: Target=Target.DEFAULT):
        """
        Gets the sign side modified in this event. 

        :param Target target: The target to retrieve the event sign side of.
        :return Text: "front" or "back"
        """
        return GameValue('Event Sign Side', target.get_string_value())

    @staticmethod
    def CombustEventDuration(target: Target=Target.DEFAULT):
        """
        Gets the duration of fire inflicted in this event. 

        :param Target target: The target to retrieve the combust event duration of.
        :return Number: Fire duration in ticks
        """
        return GameValue('Combust Event Duration', target.get_string_value())

    @staticmethod
    def CombustEventCause(target: Target=Target.DEFAULT):
        """
        Gets the reason the target caught on fire in this event. 

        :param Target target: The target to retrieve the combust event cause of.
        :return Text: Combust Cause: "player", "entity", "block", "code", "unknown"
        """
        return GameValue('Combust Event Cause', target.get_string_value())

    # endregion Event

    # region Plot

    @staticmethod
    def PlayerCount(target: Target=Target.DEFAULT):
        """
        Gets the amount of players playing on the plot. 

        :param Target target: The target to retrieve the player count of.
        :return Number: Player count
        """
        return GameValue('Player Count', target.get_string_value())

    @staticmethod
    def CPUUsage(target: Target=Target.DEFAULT):
        """
        Gets the percentage of the plot's CPU being used this instant. 

        :param Target target: The target to retrieve the cpu usage of.
        :return Number: Usage as a percentage. Can go above 100%.
        """
        return GameValue('CPU Usage', target.get_string_value())

    @staticmethod
    def ServerTPS(target: Target=Target.DEFAULT):
        """
        Gets the amount of game Ticks Per Second the server is currently able to handle. 

        :param Target target: The target to retrieve the server tps of.
        :return Number: 20.0 (no server lag) or below (decreases with more lag)
        """
        return GameValue('Server TPS', target.get_string_value())

    @staticmethod
    def Timestamp(target: Target=Target.DEFAULT):
        """
        Gets the current time as one number in seconds. E.g.: 1418840496.5 means Dec 17, 2014, 18:21:36. The number represents the total seconds passed since 1970 (Unix Time).

        :param Target target: The target to retrieve the timestamp of.
        :return Number: Current time
        """
        return GameValue('Timestamp', target.get_string_value())

    @staticmethod
    def SelectionSize(target: Target=Target.DEFAULT):
        """
        Gets the amount of targets in the selection. 

        :param Target target: The target to retrieve the selection size of.
        :return Number: 0 (no targets) or above
        """
        return GameValue('Selection Size', target.get_string_value())

    @staticmethod
    def SelectionTargetNames(target: Target=Target.DEFAULT):
        """
        Gets the name of each target in the selection. 

        :param Target target: The target to retrieve the selection target names of.
        :return List: Contains one String entry (name) for each target
        """
        return GameValue('Selection Target Names', target.get_string_value())

    @staticmethod
    def SelectionTargetUUIDs(target: Target=Target.DEFAULT):
        """
        Gets the UUID of each target in the selection. 

        :param Target target: The target to retrieve the selection target uuids of.
        :return List: Contains one String entry (UUID) for each target
        """
        return GameValue('Selection Target UUIDs', target.get_string_value())

    @staticmethod
    def PlotID(target: Target=Target.DEFAULT):
        """
        Gets the id of the plot as a string. 

        :param Target target: The target to retrieve the plot id of.
        :return Text: Plot ID
        """
        return GameValue('Plot ID', target.get_string_value())

    @staticmethod
    def PlotName(target: Target=Target.DEFAULT):
        """
        Gets the name of the plot as a styled text. 

        :param Target target: The target to retrieve the plot name of.
        :return Component: Plot Name
        """
        return GameValue('Plot Name', target.get_string_value())

    @staticmethod
    def PlotSize(target: Target=Target.DEFAULT):
        """
        Gets the size of the plot. A basic plot will return 51. A large plot will return 101. A massive plot will return 301. A mega plot will return 1001.

        :param Target target: The target to retrieve the plot size of.
        :return Number: Plot size in blocks
        """
        return GameValue('Plot Size', target.get_string_value())

    @staticmethod
    def MicrosecondsSinceStartup(target: Target=Target.DEFAULT):
        """
        Gets the number of microseconds elapsed since the first player joined the plot. The decimal part represents nanoseconds. 

        :param Target target: The target to retrieve the microseconds since startup of.
        :return Number: Microseconds
        """
        return GameValue('Microseconds Since Startup', target.get_string_value())

    @staticmethod
    def TicksSinceStartup(target: Target=Target.DEFAULT):
        """
        Gets the number of ticks that elapsed since the first player joined the plot. 

        :param Target target: The target to retrieve the ticks since startup of.
        :return Number: Ticks
        """
        return GameValue('Ticks Since Startup', target.get_string_value())

    @staticmethod
    def ActiveBlockTransactions(target: Target=Target.DEFAULT):
        """
        Gets the number of block transactions a plot is executing. 

        :param Target target: The target to retrieve the active block transactions of.
        :return Number: Active Block Transactions
        """
        return GameValue('Active Block Transactions', target.get_string_value())

    @staticmethod
    def PlotPlayerNames(target: Target=Target.DEFAULT):
        """
        Gets the name of each player on the plot. 

        :param Target target: The target to retrieve the plot player names of.
        :return List: Contains one String entry (name) for each player
        """
        return GameValue('Plot Player Names', target.get_string_value())

    @staticmethod
    def PlotPlayerUUIDs(target: Target=Target.DEFAULT):
        """
        Gets the UUID of each player on the plot. 

        :param Target target: The target to retrieve the plot player uuids of.
        :return List: Contains one String entry (UUID) for each player
        """
        return GameValue('Plot Player UUIDs', target.get_string_value())

    # endregion Plot