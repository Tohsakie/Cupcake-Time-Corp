import Utils_Model as Model
from enum import Enum
import Utils_Rotation as Rotation

class EnnemyState(Enum):
    IDLE = 0
    MOVEUP = 1
    MOVEDOWN = 2
    MOVELEFT = 3
    MOVERIGHT = 4
    ATTACK = 5

class TypeEnnemy(Enum):
    DONUTMAT = 0

class Ennemy(Model.Drawable):
    def __init__(self, texture):
        super().__init__(texture)
        self.speed = 384
        self.Rotation = Rotation.Rotation.SOUTH
        self.state = EnnemyState.IDLE
        self.life = 3
        self.type = TypeEnnemy.DONUTMAT
