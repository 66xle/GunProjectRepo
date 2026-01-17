from dfpyre import Target, DEFAULT_TARGET
from dfpyre import GameValue as _GameValue

class GameValue(_GameValue):
    @staticmethod
    def Velocity(target: Target=DEFAULT_TARGET):
        """
        Gets the speed at which the target is moving (not walking) in each direction.

        :param Target target: The target to retrieve the velocity from. Defaults to the default target.
        :return Vector: The velocity of the target.
        """
        return GameValue('Velocity', target.get_string_value())
    
    @staticmethod
    def Location(target: Target=DEFAULT_TARGET):
        """
        Retrieves the location of the specified target.

        :param Target target: The target to retrieve the location from. Defaults to the default target.
        :return Location: The location of the target.
        """
        return GameValue('Location', target.get_string_value())

