import Entities_Player as Player
import Entities_Plante as Plante
import Utils_Position as Position
import Utils_Intersect as Intersect
import Utils_Scene as Scene

class Plantations:
    def __init__(self):
        self.player = None
        self.scenes = []
        self.texture = None

    def update(self):
        if self.player.state == Player.PlayerState.PLANTATION:
            plante = Plante.Plante(self.texture)
            plante.position = Position.Position(self.player.position.x, self.player.position.y)
            plante.texPos = Position.Position(96, 16)
            for scene in self.scenes:
                if scene.state == True:
                    scene.plantes.append(plante)

        if self.player.state == Player.PlayerState.RECUPERATION:
            for scene in self.scenes:
                if scene.state == True:
                    for i in range(0, len(scene.plantes)):
                        if Intersect.intersectXY(self.player.position, self.player.size, scene.plantes[i].position, scene.plantes[i].size):
                            scene.plantes.pop(i)
                            break

        for scene in self.scenes:
            if scene.state == True:
                for plante in scene.plantes:
                    if plante.state == Plante.PlanteState.FRUIT:
                        plante.texPos.x = 112