import Utils_Model as Model
from enum import Enum

class PlanteState(Enum):
    POUSSE = 0
    FRUIT = 1

class PlanteType(Enum):
    PASTEQUE = 0
    PIMENT = 1

class Plante(Model.Drawable):
    def __init__(self, texture):
        super().__init__(texture)
        self.state = PlanteState.POUSSE
        self.type = PlanteType.PASTEQUE
