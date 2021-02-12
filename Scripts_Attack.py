import Entities_Player as Player
import Utils_Intersect as Intersect
import Utils_Time as Time
import Utils_Rotation as Rotation
import random
import Entities_Tile as Tile
import Utils_Position as Position
import Utils_ColliderBox as ColliderBox
import Utils_Size as Size
import Entities_Inventory as Inventory
import Entities_Item as Item
import time

class Attack:
    def __init__(self):
        self.scenes = []
        self.player = None
        self.pognon = None
        self.keur = None
        self.inventory = None
        self.__timer = 0
        self.__timerPiment = 0
        self.__IsPiment = False
        self.sound = None
        self.soundMob = None
        self.assetTexture = None

    def update(self):
        self.__timer += Time.Time.deltaTime
        self.__timerPiment += Time.Time.deltaTime
        if self.player.state == Player.PlayerState.ATTACK:
            for scene in self.scenes:
                if scene.state == True:
                    if scene.IsDungeon == True:
                        for monster in scene.monsters:
                            if Intersect.intersectXY(self.player.position, self.player.colBox, monster.position, monster.colBox):
                                if self.__timer >= 0.1:
                                    self.soundMob.play()
                                    monster.life -= 1
                                    self.__timer = 0
                                    if self.player.Rotation == Rotation.Rotation.EAST:
                                        monster.position.x += 16
                                    if self.player.Rotation == Rotation.Rotation.WEST:
                                        monster.position.x -= 16
                                    if self.player.Rotation == Rotation.Rotation.NORTH:
                                        monster.position.y -= 16
                                    if self.player.Rotation == Rotation.Rotation.SOUTH:
                                        monster.position.y += 16
                                    if monster.life <= 0:
                                        scene.monsters.remove(monster)
                                        self.pognon.pognon += random.randint(3, 6)
        else:
            for scene in self.scenes:
                if scene.state == True:
                    if scene.IsDungeon == True:
                        for monster in scene.monsters:
                            if Intersect.intersectXY(self.player.position, self.player.colBox, monster.position, monster.colBox):
                                if self.__timer >= 0.5:
                                    self.sound.play()
                                    self.__timer = 0
                                    self.player.life -= 1
                                    self.keur.size.w -= 8
                                    if self.player.Rotation == Rotation.Rotation.EAST:
                                        self.player.position.x -= 16
                                    if self.player.Rotation == Rotation.Rotation.WEST:
                                        self.player.position.x += 16
                                    if self.player.Rotation == Rotation.Rotation.NORTH:
                                        self.player.position.y += 16
                                    if self.player.Rotation == Rotation.Rotation.SOUTH:
                                        self.player.position.y -= 16
                                    if self.player.life <= 0:
                                        self.player.nbJour = 1
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
                                        self.pognon.pognon = 0
                                        for graine in self.inventory.itemGraines:
                                            graine.quantity = 0
                                        for legume in self.inventory.itemLegumes:
                                            legume.quantity = 0
                                        self.player.life = 3
                                        self.keur.size.w = 24

                                        # for scene in self.scenes:
                                        #     if scene.state == True: # la scene en cours
                                        #         scene.ambiant(255,255,255)

                                        self.scenes[2].state = True
                                        self.player.position = Position.Position(16, 64)


        if self.player.state == Player.PlayerState.ATTACKPIMENT and self.__IsPiment == False:
            for itemLegume in self.inventory.itemLegumes:
                if itemLegume.Item == Item.Items.PIMENT:
                    if itemLegume.quantity > 0:
                        itemLegume.quantity -= 1
                        if self.player.Rotation == Rotation.Rotation.EAST:
                            castpiment = Tile.Tile(self.assetTexture)
                            castpiment.position = Position.Position(self.player.position.x + 16, self.player.position.y)
                            castpiment.texPos = Position.Position(16, 0)
                            castpiment.size = Size.Size(32, 16)
                            castpiment.colBox = ColliderBox.ColliderBox(4, 4, 24, 8)
                        if self.player.Rotation == Rotation.Rotation.WEST:
                            castpiment = Tile.Tile(self.assetTexture)
                            castpiment.position = Position.Position(self.player.position.x - 32, self.player.position.y)
                            castpiment.texPos = Position.Position(48, 0)
                            castpiment.size = Size.Size(32, 16)
                            castpiment.colBox = ColliderBox.ColliderBox(4, 4, 24, 8)
                        if self.player.Rotation == Rotation.Rotation.NORTH:
                            castpiment = Tile.Tile(self.assetTexture)
                            castpiment.position = Position.Position(self.player.position.x, self.player.position.y - 32)
                            castpiment.texPos = Position.Position(208, 0)
                            castpiment.size = Size.Size(16, 32)
                            castpiment.colBox = ColliderBox.ColliderBox(4, 4, 8, 24)
                        if self.player.Rotation == Rotation.Rotation.SOUTH:
                            castpiment = Tile.Tile(self.assetTexture)
                            castpiment.position = Position.Position(self.player.position.x, self.player.position.y + 16)
                            castpiment.texPos = Position.Position(64, 16)
                            castpiment.size = Size.Size(16, 32)
                            castpiment.colBox = ColliderBox.ColliderBox(4, 4, 8, 24)
                        self.__IsPiment = True
                        self.__timerPiment = 0
                        for scene in self.scenes:
                            if scene.state == True:
                                if scene.IsDungeon == True:
                                    scene.attackPiment.append(castpiment)
                                    for monster in scene.monsters:
                                        if Intersect.intersectXY(castpiment.position, castpiment.colBox, monster.position, monster.colBox):
                                            if self.__timer >= 0.1:
                                                self.soundMob.play()
                                                monster.life -= 1
                                                self.__timer = 0
                                                if self.player.Rotation == Rotation.Rotation.EAST:
                                                    monster.position.x += 16
                                                if self.player.Rotation == Rotation.Rotation.WEST:
                                                    monster.position.x -= 16
                                                if self.player.Rotation == Rotation.Rotation.NORTH:
                                                    monster.position.y -= 16
                                                if self.player.Rotation == Rotation.Rotation.SOUTH:
                                                    monster.position.y += 16
                                                if monster.life <= 0:
                                                    scene.monsters.remove(monster)
                                                    self.pognon.pognon += random.randint(3, 6)

        if self.__IsPiment == True and self.__timerPiment >= 0.1:
            self.__IsPiment = False
            for scene in self.scenes:
                if scene.state == True:
                    if scene.IsDungeon == True:
                        scene.attackPiment.clear()