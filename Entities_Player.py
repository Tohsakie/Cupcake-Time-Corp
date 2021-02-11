import Utils_Model as Model
from enum import Enum
import Utils_Rotation as Rotation

class PlayerState(Enum):
    IDLE = 0
    MOVEUP = 1
    MOVEDOWN = 2
    MOVELEFT = 3
    MOVERIGHT = 4
    PLANTATION = 5
    SWITCH_ITEM = 6
    DISCUTION = 7
    ATTACK = 8
    ATTACKPIMENT = 9
    ATTACKPASTEQUE = 10

class Player(Model.Drawable):
    def __init__(self, texture):
        super().__init__(texture)
        self.speed = 96
        self.Rotation = Rotation.Rotation.NORTH
        self.state = PlayerState.IDLE
        self.life = 3
        self.maxlife = 3
        self.nbJour = 1