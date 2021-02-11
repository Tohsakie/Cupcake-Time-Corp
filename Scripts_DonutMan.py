import random
import Entities_Ennemy as Ennemy
import Utils_Time as Time
import Utils_Rotation as Rotation
import Utils_Position as Position

class DonutMan:
    def __init__(self):
        self.scenes = []
        self.player = None
        self.__timer = 0
        self.random = random.randint(0, 15) / 100

    def update(self):
        self.__timer += Time.Time.deltaTime
        for scene in self.scenes:
            if scene.state == True:
                if scene.IsDungeon == True:
                    for monster in scene.monsters:
                        if monster.type == Ennemy.TypeEnnemy.DONUTMAT:
                            monster.state = Ennemy.EnnemyState.IDLE
                            if self.__timer >= self.random:
                                self.random = random.randint(0, 15) / 100
                                self.__timer = 0
                                if self.player.position.x > monster.position.x:
                                    monster.position.x += monster.speed * Time.Time.deltaTime
                                    monster.rotation = Rotation.Rotation.EAST
                                    monster.texPos = Position.Position(0, 16)
                                    monster.state = Ennemy.EnnemyState.MOVERIGHT
                                elif self.player.position.x < monster.position.x:
                                    monster.position.x -= monster.speed * Time.Time.deltaTime
                                    monster.rotation = Rotation.Rotation.WEST
                                    monster.texPos = Position.Position(0, 32)
                                    monster.state = Ennemy.EnnemyState.MOVELEFT
                                if self.player.position.y > monster.position.y:
                                    monster.position.y += monster.speed * Time.Time.deltaTime
                                    monster.rotation = Rotation.Rotation.SOUTH
                                    monster.texPos = Position.Position(0, 0)
                                    monster.state = Ennemy.EnnemyState.MOVEDOWN
                                elif self.player.position.y < monster.position.y:
                                    monster.position.y -= monster.speed * Time.Time.deltaTime
                                    monster.rotation = Rotation.Rotation.NORTH
                                    monster.texPos = Position.Position(0, 48)
                                    monster.state = Ennemy.EnnemyState.MOVEUP