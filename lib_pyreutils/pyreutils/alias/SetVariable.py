from dfpyre import Variable, Location, Number
from dfpyre import SetVariable as _SetVariable

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

SetV = SetVariable
SV = SetVariable