import Utils_Position as Position
import Utils_ColliderBox as ColliderBox
from enum import Enum

class EtatMarchand(Enum):
    INACTIF = 0
    ACTIF = 1

class InventaireMarchand(Enum):
    INVENTAIRE_RIEN = 0
    INVENTAIRE_HAUT = 1
    INVENTAIRE_BAS = 2
    INVENTAIRE_ACHAT = 3

class Marchand:
    def __init__(self):
        self.pos = Position.Position()
        self.colBox = ColliderBox.ColliderBox()
        self.etat = EtatMarchand.INACTIF
        self.inventaireMarchand = InventaireMarchand.INVENTAIRE_RIEN