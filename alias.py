# ruff: noqa: F403, F405
from typing import Literal
from dfpyre import *
from dfpyre import PlayerAction as _PlayerAction
from dfpyre import SetVariable as _SetVariable
from dfpyre import GameValue as _GameValue
from dfpyre import IfVariable as _IfVariable

DEFAULT_TARGET = Target.NONE

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

class SetVariable(_SetVariable):

    # region GetCoord

    @staticmethod
    def GetCoordX(variable: Variable, location: Location | None=None):
        """
        Gets the X coordinate of a location.

        :param Variable variable: Variable to set
        :param Location | None location: Location to get (optional)

        """
        return SetVariable.GetCoord(variable, location, coordinate="X")

    @staticmethod
    def GetCoordY(variable: Variable, location: Location | None=None):
        """
        Gets the Y coordinate of a location.

        :param Variable variable: Variable to set
        :param Location | None location: Location to get (optional)

        """
        
        return SetVariable.GetCoord(variable, location, coordinate="Y")

    @staticmethod
    def GetCoordZ(variable: Variable, location: Location | None=None):
        """
        Gets the Z coordinate of a location.

        :param Variable variable: Variable to set
        :param Location | None location: Location to get (optional)

        """
        
        return SetVariable.GetCoord(variable, location, coordinate="Z")

    @staticmethod
    def GetCoordPitch(variable: Variable, location: Location | None=None):
        """
        Gets the Pitch coordinate of a location.

        :param Variable variable: Variable to set
        :param Location | None location: Location to get (optional)

        """

        return SetVariable.GetCoord(variable, location, coordinate="Pitch")

    @staticmethod
    def GetCoordYaw(variable: Variable, location: Location | None=None):
        """
        Gets the Yaw coordinate of a location.

        :param Variable variable: Variable to set
        :param Location | None location: Location to get (optional)

        """
        return SetVariable.GetCoord(variable, location, coordinate="Yaw")
    
    GetX     = GetCoordX
    GetY     = GetCoordY
    GetZ     = GetCoordZ
    GetPitch = GetCoordPitch
    GetYaw   = GetCoordYaw
    
    #endregion GetCoord

    # region SetCoord

    @staticmethod
    def SetCoordX(variable: Variable, location: Location | None=None, number: Number=None):
        """
        Sets the X coordinate of a location.

        :param Variable variable: Variable to set
        :param Location | None location: Location to change (optional)
        :param Number number: New X value (optional)

        """
        return SetVariable.SetCoord(variable, location, number, coordinate="X")

    @staticmethod
    def SetCoordY(variable: Variable, location: Location | None=None, number: Number=None):
        """
        Sets the Y coordinate of a location.

        :param Variable variable: Variable to set
        :param Location | None location: Location to change (optional)
        :param Number number: New Y value (optional)

        """
        
        return SetVariable.SetCoord(variable, location, number, coordinate="Y")

    @staticmethod
    def SetCoordZ(variable: Variable, location: Location | None=None, number: Number=None):
        """
        Sets the Z coordinate of a location.

        :param Variable variable: Variable to set
        :param Location | None location: Location to change (optional)
        :param Number number: New Z value (optional)

        """
        
        return SetVariable.SetCoord(variable, location, number, coordinate="Z")

    @staticmethod
    def SetCoordPitch(variable: Variable, location: Location | None=None, number: Number=None):
        """
        Sets the Pitch coordinate of a location.

        :param Variable variable: Variable to set
        :param Location | None location: Location to change (optional)
        :param Number number: New Pitch value (optional)

        """

        return SetVariable.SetCoord(variable, location, number, coordinate="Pitch")

    @staticmethod
    def SetCoordYaw(variable: Variable, location: Location | None=None, number: Number=None):
        """
        Sets the Yaw coordinate of a location.

        :param Variable variable: Variable to set
        :param Location | None location: Location to change (optional)
        :param Number number: New Yaw value (optional)

        """
        return SetVariable.SetCoord(variable, location, number, coordinate="Yaw")
    
    SetX     = SetCoordX
    SetY     = SetCoordY
    SetZ     = SetCoordZ
    SetPitch = SetCoordPitch
    SetYaw   = SetCoordYaw
    
    # endregion SetCoord
    
    # region ShiftOnAxis

    @staticmethod
    def ShiftX(variable: Variable, location: Location | None=None, number: Number=None):
        """
        Shifts the X coordinate of a location on its axis.
    
        :param Variable variable: Variable to set
        :param Location | None location: Location to shift (optional)
        :param Number number: Shift distance
        
        """
        return SetVariable.ShiftOnAxis(variable, location, number, coordinate="X")

    @staticmethod
    def ShiftY(variable: Variable, location: Location | None=None, number: Number=None):
        """
        Shifts the Y coordinate of a location on its axis.
    
        :param Variable variable: Variable to set
        :param Location | None location: Location to shift (optional)
        :param Number number: Shift distance
        
        """
        return SetVariable.ShiftOnAxis(variable, location, number, coordinate="Y")

    @staticmethod
    def ShiftZ(variable: Variable, location: Location | None=None, number: Number=None):
        """
        Shifts the Z coordinate of a location on its axis.
    
        :param Variable variable: Variable to set
        :param Location | None location: Location to shift (optional)
        :param Number number: Shift distance
        
        """
        return SetVariable.ShiftOnAxis(variable, location, number, coordinate="Z")

    # endregion ShiftOnAxis
    
    # region GetVectorComp
    
    @staticmethod
    def GetVectorX(variable: Variable, location: Location | None=None):
        """
        Gets the X component of a vector.

        :param Variable variable: Variable to set
        :param DFVector vector: Vector to get component of
        
        """
        return SetVariable.GetVectorComp(variable, location, "X")

    @staticmethod
    def GetVectorY(variable: Variable, location: Location | None=None):
        """
        Gets the Y component of a vector.

        :param Variable variable: Variable to set
        :param DFVector vector: Vector to get component of
        
        """
        return SetVariable.GetVectorComp(variable, location, "Y")

    @staticmethod
    def GetVectorZ(variable: Variable, location: Location | None=None):
        """
        Gets the Z component of a vector.

        :param Variable variable: Variable to set
        :param DFVector vector: Vector to get component of
        
        """
        return SetVariable.GetVectorComp(variable, location, "Z")

    # endregion GetVectorComp
class GameValue(_GameValue):
    @staticmethod
    def Velocity(target: Target=Target.DEFAULT):
        """
        Gets the speed at which the target is moving (not walking) in each direction.

        :param Target target: The target to retrieve the velocity from. Defaults to the default target.
        :return Vector: The velocity of the target.
        """
        return GameValue('Velocity', target.get_string_value())
    
    @staticmethod
    def Location(target: Target=Target.DEFAULT):
        """
        Retrieves the location of the specified target.

        :param Target target: The target to retrieve the location from. Defaults to the default target.
        :return Location: The location of the target.
        """
        return GameValue('Location', target.get_string_value())

class IfVariable(_IfVariable): 
    pass

If = IfVariable