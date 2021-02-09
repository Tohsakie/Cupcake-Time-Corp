import Entities_Player as Player
import Entities_Warp as Warp
import Utils_Scene as Scene
import Utils_Intersect as Intersect
import Utils_Rotation as Rotation

class WarpScript:
    def __init__(self):
        self.player = None
        self.scenes = []

    def update(self):
        for scene in self.scenes:
            if scene.state == True:
                for warp in scene.warps:
                    if Intersect.intersectXY(self.player.position, self.player.colBox, warp.warppos, warp.colBox):
                        scene.state = False
                        self.scenes[warp.sceneId].state = True
                        if self.player.Rotation == Rotation.Rotation.NORTH:
                            self.player.position.y = warp.tppos.y
                        if self.player.Rotation == Rotation.Rotation.SOUTH:
                            self.player.position.y = warp.tppos.y
                        if self.player.Rotation == Rotation.Rotation.EAST:
                            self.player.position.x = warp.tppos.x
                        if self.player.Rotation == Rotation.Rotation.WEST:
                            self.player.position.x = warp.tppos.x