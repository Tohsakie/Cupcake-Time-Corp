import Entities_Player as Player
import Entities_Warp as Warp
import Utils_Scene as Scene
import Utils_Intersect as Intersect
import Utils_Rotation as Rotation
import Entities_Plante as Plante

class WarpScript:
    def __init__(self):
        self.player = None
        self.scenes = []
        self.__purge = False
        self.sound = None
        self.inventory = None

    def update(self):
        if self.player.state != Player.PlayerState.ATTACK:
            for scene in self.scenes:
                if scene.state == True:
                    for warp in scene.warps:
                        if Intersect.intersectXY(self.player.position, self.player.colBox, warp.warppos, warp.colBox):
                            scene.state = False
                            if warp.IsDoor == True:
                                self.sound.play()
                            self.scenes[warp.sceneId].state = True
                            if self.player.Rotation == Rotation.Rotation.NORTH:
                                self.player.position.y = warp.tppos.y
                            if self.player.Rotation == Rotation.Rotation.SOUTH:
                                self.player.position.y = warp.tppos.y
                            if self.player.Rotation == Rotation.Rotation.EAST:
                                self.player.position.x = warp.tppos.x
                            if self.player.Rotation == Rotation.Rotation.WEST:
                                self.player.position.x = warp.tppos.x
                            if warp.purgeDungeon == True:
                                self.__purge = True
            if self.__purge == True:
                self.player.nbJour += 1
                self.inventory.IsGraines = True
                self.__purge = False
                tmparray = []
                for i in self.scenes:
                    if i.IsDungeon == True:
                        tmparray.append(i)
                for i in tmparray:
                    self.scenes.remove(i)
                for scene in self.scenes:
                    for plante in scene.plantes:
                        plante.state = Plante.PlanteState.FRUIT
                