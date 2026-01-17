from dfpyre import Control as _Control
from dfpyre import Number

class Control(_Control): 
    @staticmethod
    def WaitSeconds(number: Number | None=None):
        """
        Pauses the current code sequence for a specified duration in seconds.
    
        :param Number | None number: Wait duration (optional) (Default = 1)
        :param str time_unit: Time Unit
        
        """
        return Control.Wait(number, time_unit='Seconds')
    
    WaitSecs = WaitSeconds