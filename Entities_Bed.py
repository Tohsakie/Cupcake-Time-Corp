import Utils_Position as Position
import Utils_ColliderBox as ColliderBox
from enum import Enum

class BedState(Enum):
    INACTIF = 0
    ACTIF = 0

class Bed:
    def __init__(self):
        self.pos = Position.Position()
        self.colBox = ColliderBox.ColliderBox()
        self.state = BedState.INACTIF