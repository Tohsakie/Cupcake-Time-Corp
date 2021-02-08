import Entities_Player as Player
import pygame
import Utils_Time as Time
import Utils_Rotation as Rotation

class PlayerAction:
    def __init__(self):
        self.player = None

    def update(self):
        if self.player.state == Player.PlayerState.IDLE:
            self.player.texPos.x = 0
        elif self.player.state == Player.PlayerState.MOVEUP:
            self.player.texPos.y = 48
            self.player.position.y -= self.player.speed * Time.Time.deltaTime
            self.player.Rotation = Rotation.Rotation.NORTH
        elif self.player.state == Player.PlayerState.MOVEDOWN:
            self.player.texPos.y = 0
            self.player.position.y += self.player.speed * Time.Time.deltaTime
            self.player.Rotation = Rotation.Rotation.SOUTH
        elif self.player.state == Player.PlayerState.MOVELEFT:
            self.player.texPos.y = 32
            self.player.position.x -= self.player.speed * Time.Time.deltaTime
            self.player.Rotation = Rotation.Rotation.WEST
        elif self.player.state == Player.PlayerState.MOVERIGHT:
            self.player.texPos.y = 16
            self.player.position.x += self.player.speed * Time.Time.deltaTime
            self.player.Rotation = Rotation.Rotation.EAST