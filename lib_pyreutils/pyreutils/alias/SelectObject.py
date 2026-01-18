from dfpyre import SelectObject as _SelectObject, String as DFString

class SelectObject(_SelectObject): 
    @staticmethod
    def PlayerName(texts: list[DFString] | DFString, inverted: bool=False):
        """
        Creates a selection using all players in the game whose name or UUID matches.
    
        :param list[DFString] | DFString texts: Name or UUID
        :param bool inverted: Whether the condition should be inverted.
        """
        return _SelectObject.PlayerName(texts, inverted)
