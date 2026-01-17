from typing import Literal
from dfpyre import Number, Target, DEFAULT_TARGET
from dfpyre import PlayerAction as _PlayerAction

class PlayerAction(_PlayerAction):
    
    # region MovementAttribute
    @staticmethod
    def JumpStrength(number: Number | None=None, value_type: Literal["Direct", "Percentage (Base)", "Percentage (Relative)"]="Direct", target: Target=DEFAULT_TARGET):
        """
        Sets the player's jump strength.
        Base: 0.42 | Range: 0.0-32.0

        :param Number | None number: Value (optional)
        :param str value_type: Value Type
    
            - Percentage (Base): A percentage of the base value shown above. 100% is equal to the base value.
            - Percentage (Relative): A percentage of what the attribute is currently set to. For example, 200% doubles the current value.
        :param Target target: The target for the action.
        """
        return PlayerAction.MovementAttribute(number, 'Jump strength', value_type, target)
    
    @staticmethod
    def WalkingSpeed(number: Number | None=None, value_type: Literal["Direct", "Percentage (Base)", "Percentage (Relative)"]="Direct", target: Target=DEFAULT_TARGET):
        """
        Sets the player's jump strength.
        Base: 0.2 | Range: -1.0-1.0


        :param Number | None number: Value (optional)
        :param str value_type: Value Type
    
            - Percentage (Base): A percentage of the base value shown above. 100% is equal to the base value.
            - Percentage (Relative): A percentage of what the attribute is currently set to. For example, 200% doubles the current value.
        :param Target target: The target for the action.
        """
        return PlayerAction.MovementAttribute(number, 'Walking speed', value_type, target)
    
    # endregion MovementAttribute

