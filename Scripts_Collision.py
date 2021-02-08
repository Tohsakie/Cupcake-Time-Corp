import Entities_Tile as Tile
import Entities_Player as Player
import Utils_Time as Time
import Utils_Intersect as Intersect
import Utils_Scene as Scene

class Collision:
    def __init__(self):
        self.scenes = []
        self.player = None

    def update(self):
        if self.player.state == Player.PlayerState.MOVEUP:
            for scene in self.scenes:
                if scene.state == True:
                    for tile in scene.tiles:
                        if tile.collider == True:
                            if Intersect.intersectXY(self.player.position, self.player.size, tile.position, tile.size):
                                self.player.position.y += self.player.speed * Time.Time.deltaTime
                    for tile in scene.assets:
                        if tile.collider == True:
                            if Intersect.intersectXY(self.player.position, self.player.size, tile.position, tile.size):
                                self.player.position.y += self.player.speed * Time.Time.deltaTime

        if self.player.state == Player.PlayerState.MOVEDOWN:
            for scene in self.scenes:
                if scene.state == True:
                    for tile in scene.tiles:
                        if tile.collider == True:
                            if Intersect.intersectXY(self.player.position, self.player.size, tile.position, tile.size):
                                self.player.position.y -= self.player.speed * Time.Time.deltaTime
                    for tile in scene.assets:
                        if tile.collider == True:
                            if Intersect.intersectXY(self.player.position, self.player.size, tile.position, tile.size):
                                self.player.position.y -= self.player.speed * Time.Time.deltaTime

        if self.player.state == Player.PlayerState.MOVELEFT:
            for scene in self.scenes:
                if scene.state == True:
                    for tile in scene.tiles:
                        if tile.collider == True:
                            if Intersect.intersectXY(self.player.position, self.player.size, tile.position, tile.size):
                                self.player.position.x += self.player.speed * Time.Time.deltaTime
                    for tile in scene.assets:
                        if tile.collider == True:
                            if Intersect.intersectXY(self.player.position, self.player.size, tile.position, tile.size):
                                self.player.position.x += self.player.speed * Time.Time.deltaTime

        if self.player.state == Player.PlayerState.MOVERIGHT:
            for scene in self.scenes:
                if scene.state == True:
                    for tile in scene.tiles:
                        if tile.collider == True:
                            if Intersect.intersectXY(self.player.position, self.player.size, tile.position, tile.size):
                                self.player.position.x -= self.player.speed * Time.Time.deltaTime
                    for tile in scene.assets:
                        if tile.collider == True:
                            if Intersect.intersectXY(self.player.position, self.player.size, tile.position, tile.size):
                                self.player.position.x -= self.player.speed * Time.Time.deltaTime