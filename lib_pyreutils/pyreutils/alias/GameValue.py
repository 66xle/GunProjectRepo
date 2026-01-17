from dfpyre import Target
from dfpyre import GameValue as _GameValue

class GameValue(_GameValue):
    
    #region Location
    
    @staticmethod
    def Velocity(target: Target=Target.DEFAULT):
        """
        Gets the speed at which the target is moving (not walking) in each direction.

        :param Target target: The target to retrieve the velocity from.
        :return Vector: Movement velocity
        """
        return GameValue('Velocity', target.get_string_value())
    
    @staticmethod
    def Direction(target: Target=Target.DEFAULT):
        """
        Gets the looking direction of a target's location as a vector.

        :param Target target: The target to retrieve the direction from.
        :return Vector: Direction vector (length of 1)
        """
        return GameValue('Velocity', target.get_string_value())
    
    @staticmethod
    def Location(target: Target=Target.DEFAULT):
        """
        Retrieves the location of the specified target.

        :param Target target: The target to retrieve the location from.
        :return Location: Location and rotation, at feet height.
        """
        return GameValue('Location', target.get_string_value())

    @staticmethod
    def MidpointLocation(target: Target=Target.DEFAULT):
        """
        Gets the midpoint location of the target.

        :param Target target: The target to retrieve the midpoint location from.
        :return Location: The midpoint location and rotation.
        """
        return GameValue('Midpoint Location', target.get_string_value())
    
    @staticmethod
    def EyeLocation(target: Target=Target.DEFAULT):
        """
        Gets a target's location, but adjusted to its eye height.

        :param Target target: The target to retrieve the eye location from.
        :return Location: The eye location and rotation.
        """
        return GameValue('Eye Location', target.get_string_value())
    
    #endregion Location
    
    # region Statistics
    
    @staticmethod
    def CurrentHealth(target: Target=Target.DEFAULT):
        """
        Gets the target's remaining health points.

        :param Target target: The target to retrieve their current health.
        :return Number: 0.0 (dead) up to the target's maximum health (20.0 by default)
        """
        return GameValue('Current Health', target.get_string_value())
    
    # endregion Statistics
    
    # region Information
    
    @staticmethod
    def UUID(target: Target=Target.DEFAULT):
        """
        Gets the UUID of the target.

        :param Target target: The target to retrieve the UUID from.
        :return String: The UUID of the target.
        """
        return GameValue('UUID', target.get_string_value())
    
    # endregion Information
    
    # region Events
    
    @staticmethod
    def EventCommandArguments(target: Target=Target.DEFAULT):
        """
        Gets the arguments of the current event command.

        :param Target target: The target to retrieve the event command arguments from.
        :return List: The arguments of the current event command.
        """
        return GameValue('Event Command Arguments', target.get_string_value())

    @staticmethod
    def EventHotbarSlot(target: Target=Target.DEFAULT):
        """
        Gets the hotbar slot of the current event command.

        :param Target target: The target to retrieve the event hotbar slot from.
        :return Number: The hotbar slot of the current event command.
        """
        return GameValue('Event Hotbar Slot', target.get_string_value())

    # endregion Events
    
    # region Item

    @staticmethod
    def MainHandItem(target: Target=Target.DEFAULT):
        """
        Gets the item in the target's main hand.

        :param Target target: The target to retrieve the main hand item from.
        :return Item: The item in the main hand.
        """
        return GameValue('Main Hand Item', target.get_string_value())

    @staticmethod
    def HotbarItems(target: Target=Target.DEFAULT):
        """
        Gets the items in the target's hotbar.

        :param Target target: The target to retrieve the hotbar items from.
        :return List: The items in the hotbar.
        """
        return GameValue('Hotbar Items', target.get_string_value())

    # endregion Item
    
    # region Plot

    @staticmethod
    def SelectionSize(target: Target=Target.DEFAULT):
        """
        Gets the size of the selection.

        :param Target target: The target to retrieve the selection size from.
        :return Number: The number of entities in the selection.
        """
        return GameValue('Selection Size', target.get_string_value())

    @staticmethod
    def SelectionTargetUUIDs(target: Target=Target.DEFAULT):
        """
        Gets the UUIDs of the selected targets.

        :param Target target: The target to retrieve the selection target UUIDs from.
        :return List: The UUIDs of the selected targets.
        """
        return GameValue('Selection Target UUIDs', target.get_string_value())

    # endregion Plot
