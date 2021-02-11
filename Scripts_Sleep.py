import Utils_Intersect as Intersect
import Entities_Bed as Bed
import Entities_Player as Player
import Utils_DungeonGen as DungeonGen
import Utils_DungeonGenScene as DungeonGenScene

class Sleep:
    def __init__(self):
        self.player = None
        self.scenes = []
        self.tileTexture = None
        self.assetTexture = None
        self.ennemyTexture = None
        self.keurTexture = None
        self.inventory = None

    def update(self):
        for scene in self.scenes:
            if scene.state == True:
                for bed in scene.beds:
                    if Intersect.intersectXY(self.player.position, self.player.colBox, bed.pos, bed.colBox):

                    # S'endormir
                        if self.player.state == Player.PlayerState.PLANTATION:
                            # if bed.state == Bed.BedState.INACTIF:
                            self.player.state = Player.PlayerState.DISCUTION
                            # bed.state = Bed.BedState.ACTIF
                            dungeon = DungeonGen.DungeonGen()
                            dungeon.Gen()
                            DungeonGenScene.createDungeonScenes(self.player, self.scenes, self.tileTexture, self.assetTexture, self.ennemyTexture, self.keurTexture, dungeon.genMatrix)
                            self.player.state = Player.PlayerState.IDLE
                            self.inventory.IsGraines = False
                            
