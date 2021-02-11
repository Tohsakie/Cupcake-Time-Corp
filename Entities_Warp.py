import Utils_Position as Position
import Utils_ColliderBox as ColliderBox

class Warp:
    def __init__(self):
        self.warppos = Position.Position()
        self.colBox = ColliderBox.ColliderBox()
        self.tppos = Position.Position()
        self.purgeDungeon = False
        self.sceneId = 0
        self.IsDoor = True