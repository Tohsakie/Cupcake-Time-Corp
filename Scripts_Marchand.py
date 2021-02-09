import Utils_Intersect as Intersect
import Entities_Marchand as Marchand
import Entities_Player as Player
import Entities_Tile as Tile
import Utils_Position as Position
import Utils_Size as Size

class ScriptMarchand:
    def __init__(self):
        self.scenes = []
        self.joueur = None
        self.uiTexture = None

    def update(self):
        for scene in self.scenes:
            if scene.state == True:
                for marchand in scene.marchands:
                    if Intersect.intersectXY(self.joueur.position, self.joueur.colBox, marchand.pos, marchand.colBox):
                            if self.joueur.state == Player.PlayerState.PLANTATION:
                                self.joueur.state = Player.PlayerState.DISCUTION
                                marchand.state = Marchand.EtatMarchand.ACTIF
                                ui = Tile.Tile(self.uiTexture)
                                ui.position = Position.Position(32, 32)
                                ui.size = Size.Size(96, 64)
                                scene.ui.append(ui)