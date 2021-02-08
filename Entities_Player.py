import Utils_Model as Model
from enum import Enum
import Utils_Rotation as Rotation

class PlayerState(Enum):
    IDLE = 0
    MOVEUP = 1
    MOVEDOWN = 2
    MOVELEFT = 3
    MOVERIGHT = 4
    WINDATTRACT = 5

class Player(Model.Drawable):
    def __init__(self, texture):
        super().__init__(texture)
        self.speed = 128
        self.Rotation = Rotation.Rotation.NORTH
        self.state = PlayerState.IDLE