import Entities_Tile as Tile
import Entities_Player as Player
import Utils_Time as Time
import Utils_Intersect as Intersect

class Collision:
    def __init__(self):
        self.tiles = []
        self.assets = []
        self.player = None

    def update(self):
        if self.player.state == Player.PlayerState.MOVEUP:
            for tile in self.tiles:
                if tile.collider == True:
                    if Intersect.intersectXY(self.player.position, self.player.size, tile.position, tile.size):
                        self.player.position.y += self.player.speed * Time.Time.deltaTime
            for tile in self.assets:
                if tile.collider == True:
                    if Intersect.intersectXY(self.player.position, self.player.size, tile.position, tile.size):
                        self.player.position.y += self.player.speed * Time.Time.deltaTime

        if self.player.state == Player.PlayerState.MOVEDOWN:
            for tile in self.tiles:
                if tile.collider == True:
                    if Intersect.intersectXY(self.player.position, self.player.size, tile.position, tile.size):
                        self.player.position.y -= self.player.speed * Time.Time.deltaTime
            for tile in self.assets:
                if tile.collider == True:
                    if Intersect.intersectXY(self.player.position, self.player.size, tile.position, tile.size):
                        self.player.position.y -= self.player.speed * Time.Time.deltaTime

        if self.player.state == Player.PlayerState.MOVELEFT:
            for tile in self.tiles:
                if tile.collider == True:
                    if Intersect.intersectXY(self.player.position, self.player.size, tile.position, tile.size):
                        self.player.position.x += self.player.speed * Time.Time.deltaTime
            for tile in self.assets:
                if tile.collider == True:
                    if Intersect.intersectXY(self.player.position, self.player.size, tile.position, tile.size):
                        self.player.position.x += self.player.speed * Time.Time.deltaTime

        if self.player.state == Player.PlayerState.MOVERIGHT:
            for tile in self.tiles:
                if tile.collider == True:
                    if Intersect.intersectXY(self.player.position, self.player.size, tile.position, tile.size):
                        self.player.position.x -= self.player.speed * Time.Time.deltaTime
            for tile in self.assets:
                if tile.collider == True:
                    if Intersect.intersectXY(self.player.position, self.player.size, tile.position, tile.size):
                        self.player.position.x -= self.player.speed * Time.Time.deltaTime