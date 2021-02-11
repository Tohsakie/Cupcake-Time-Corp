import Entities_Tile as Tile
import Entities_Player as Player
import Utils_Time as Time
import Utils_Intersect as Intersect
import Utils_Scene as Scene
import Entities_Ennemy as Ennemy

class Collision:
    def __init__(self):
        self.scenes = []
        self.player = None

    def update(self):
    # Collisions joueur
        if self.player.state == Player.PlayerState.MOVEUP:
            for scene in self.scenes:
                if scene.state == True:
                    for tile in scene.tiles:
                        if tile.collider == True:
                            if Intersect.intersectXY(self.player.position, self.player.colBox, tile.position, tile.colBox):
                                self.player.position.y += self.player.speed * Time.Time.deltaTime
                    for tile in scene.assets:
                        if tile.collider == True:
                            if Intersect.intersectXY(self.player.position, self.player.colBox, tile.position, tile.colBox):
                                self.player.position.y += self.player.speed * Time.Time.deltaTime

        if self.player.state == Player.PlayerState.MOVEDOWN:
            for scene in self.scenes:
                if scene.state == True:
                    for tile in scene.tiles:
                        if tile.collider == True:
                            if Intersect.intersectXY(self.player.position, self.player.colBox, tile.position, tile.colBox):
                                self.player.position.y -= self.player.speed * Time.Time.deltaTime
                    for tile in scene.assets:
                        if tile.collider == True:
                            if Intersect.intersectXY(self.player.position, self.player.colBox, tile.position, tile.colBox):
                                self.player.position.y -= self.player.speed * Time.Time.deltaTime

        if self.player.state == Player.PlayerState.MOVELEFT:
            for scene in self.scenes:
                if scene.state == True:
                    for tile in scene.tiles:
                        if tile.collider == True:
                            if Intersect.intersectXY(self.player.position, self.player.colBox, tile.position, tile.colBox):
                                self.player.position.x += self.player.speed * Time.Time.deltaTime
                    for tile in scene.assets:
                        if tile.collider == True:
                            if Intersect.intersectXY(self.player.position, self.player.colBox, tile.position, tile.colBox):
                                self.player.position.x += self.player.speed * Time.Time.deltaTime

        if self.player.state == Player.PlayerState.MOVERIGHT:
            for scene in self.scenes:
                if scene.state == True:
                    for tile in scene.tiles:
                        if tile.collider == True:
                            if Intersect.intersectXY(self.player.position, self.player.colBox, tile.position, tile.colBox):
                                self.player.position.x -= self.player.speed * Time.Time.deltaTime
                    for tile in scene.assets:
                        if tile.collider == True:
                            if Intersect.intersectXY(self.player.position, self.player.colBox, tile.position, tile.colBox):
                                self.player.position.x -= self.player.speed * Time.Time.deltaTime
    
    # Collision mechant tres sucre
        for scene in self.scenes:
            if scene.state == True:
                if scene.IsDungeon == True:
                    for monster in scene.monsters:
                        if monster.state == Ennemy.EnnemyState.MOVERIGHT:
                            for tile in scene.tiles:
                                if tile.collider == True:
                                    if Intersect.intersectXY(monster.position, monster.colBox, tile.position, tile.colBox):
                                        monster.position.x -= monster.speed * Time.Time.deltaTime
                            for tile in scene.assets:
                                if tile.collider == True:
                                    if Intersect.intersectXY(monster.position, monster.colBox, tile.position, tile.colBox):
                                        monster.position.x -= monster.speed * Time.Time.deltaTime
                        if monster.state == Ennemy.EnnemyState.MOVELEFT:
                            for tile in scene.tiles:
                                if tile.collider == True:
                                    if Intersect.intersectXY(monster.position, monster.colBox, tile.position, tile.colBox):
                                        monster.position.x += monster.speed * Time.Time.deltaTime
                            for tile in scene.assets:
                                if tile.collider == True:
                                    if Intersect.intersectXY(monster.position, monster.colBox, tile.position, tile.colBox):
                                        monster.position.x += monster.speed * Time.Time.deltaTime
                        if monster.state == Ennemy.EnnemyState.MOVEUP:
                            for tile in scene.tiles:
                                if tile.collider == True:
                                    if Intersect.intersectXY(monster.position, monster.colBox, tile.position, tile.colBox):
                                        monster.position.x += monster.speed * Time.Time.deltaTime
                            for tile in scene.assets:
                                if tile.collider == True:
                                    if Intersect.intersectXY(monster.position, monster.colBox, tile.position, tile.colBox):
                                        monster.position.y += monster.speed * Time.Time.deltaTime
                        if monster.state == Ennemy.EnnemyState.MOVEDOWN:
                            for tile in scene.tiles:
                                if tile.collider == True:
                                    if Intersect.intersectXY(monster.position, monster.colBox, tile.position, tile.colBox):
                                        monster.position.x -= monster.speed * Time.Time.deltaTime
                            for tile in scene.assets:
                                if tile.collider == True:
                                    if Intersect.intersectXY(monster.position, monster.colBox, tile.position, tile.colBox):
                                        monster.position.y -= monster.speed * Time.Time.deltaTime