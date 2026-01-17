from dfpyre import Target, DEFAULT_TARGET
from dfpyre import GameValue as _GameValue

class GameValue(_GameValue):
    @staticmethod
    def Velocity(target: Target=DEFAULT_TARGET):
        """
        Gets the speed at which the target is moving (not walking) in each direction.

        :param Target target: The target to retrieve the velocity from.
        :return Vector: Movement velocity
        """
        return GameValue('Velocity', target.get_string_value())
    
    @staticmethod
    def Direction(target: Target=DEFAULT_TARGET):
        """
        Gets the looking direction of a target's location as a vector.

        :param Target target: The target to retrieve the direction from.
        :return Vector: Direction vector (length of 1)
        """
        return GameValue('Velocity', target.get_string_value())
    
    @staticmethod
    def Location(target: Target=DEFAULT_TARGET):
        """
        Retrieves the location of the specified target.

        :param Target target: The target to retrieve the location from.
        :return Location: Location and rotation, at feet height.
        """
        return GameValue('Location', target.get_string_value())
    
    @staticmethod
    def EyeLocation(target: Target=DEFAULT_TARGET):
        """
        Gets a target's location, but adjusted to its eye height.

        :param Target target: The target to retrieve the eye location from.
        :return Location: The eye location and rotation.
        """
        return GameValue('Eye Location', target.get_string_value())
    
    @staticmethod
    def CurrentHealth(target: Target=DEFAULT_TARGET):
        """
        Gets the target's remaining health points.

        :param Target target: The target to retrieve their current health.
        :return Number: 0.0 (dead) up to the target's maximum health (20.0 by default)
        """
        return GameValue('Current Health', target.get_string_value())
    
    

