import Utils_Position as Position
import Utils_Size as Size

class Warp:
    def __init__(self):
        self.warppos = Position.Position()
        self.warpsize = Size.Size()
        self.tppos = Position.Position()
        self.sceneId = 0