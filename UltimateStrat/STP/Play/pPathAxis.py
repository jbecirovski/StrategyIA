#Under MIT License, see LICENSE.txt
from UltimateStrat.STP.Play.PlayBase import PlayBase

__author__ = 'agingrasc'

class pPathAxis(PlayBase):
    """
    Strategie de base qui permet au premier robot de se positionner sur la balle avec son dribbler.
    """
    def __init__(self):
        PlayBase.__init__(self, self.__class__.__name__)

    def getTactics(self, index=None):
        sequence = [['tNull' for x in range(6)]]
        sequence[0][4] = 'tPathAxis' 
        if index is None:
            return sequence[0]
        else:
            return sequence[index]
