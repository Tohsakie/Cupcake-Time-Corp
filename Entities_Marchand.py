import Utils_Position as Position
import Utils_ColliderBox as ColliderBox
from enum import Enum

class EtatMarchand(Enum):
    INACTIF = 0
    ACTIF = 1

class Marchand:
    def __init__(self):
        self.pos = Position.Position()
        self.colBox = ColliderBox.ColliderBox()
        self.etat = EtatMarchand.INACTIF