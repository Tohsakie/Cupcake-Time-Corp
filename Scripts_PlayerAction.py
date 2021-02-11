import Entities_Player as Player
import pygame
import Utils_Time as Time
import Utils_Rotation as Rotation
import Utils_ColliderBox as ColliderBox

class PlayerAction:
    def __init__(self):
        self.player = None
        self.__lock = False
        self.__lock2 = False
        self.__time = 0.0
        self.Attack = False
        self.sound = None

    def update(self):

        if self.Attack == False:
        # Etat initiale
            if self.player.state == Player.PlayerState.IDLE:
                self.player.texPos.x = 0
                self.player.size.w = 16
                self.player.size.h = 16

        # Mouvements
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
        # Attaque
            elif self.player.state == Player.PlayerState.ATTACK:
                self.Attack = True
                self.sound.play()

        else:
            self.player.state = Player.PlayerState.ATTACK
            self.__time += Time.Time.deltaTime
            if self.__time >= 0 and self.__time < 0.05:
                if self.player.Rotation == Rotation.Rotation.SOUTH:
                    if self.__lock == False:
                        self.__lock = True
                        self.player.texPos.y = 0
                        self.player.texPos.x = 32
                        self.player.position.x -= 16
                        self.player.size.w = 32
                        self.player.size.h = 16
                        self.player.colBox = ColliderBox.ColliderBox(0, 0, 32, 32)
                if self.player.Rotation == Rotation.Rotation.EAST:
                    self.player.texPos.y = 0
                    self.player.texPos.x = 112
                    self.player.size.w = 16
                    self.player.size.h = 32
                    self.player.colBox = ColliderBox.ColliderBox(0, 0, 32, 32)
                if self.player.Rotation == Rotation.Rotation.NORTH:
                    self.player.texPos.y = 48
                    self.player.texPos.x = 32
                    self.player.size.w = 32
                    self.player.size.h = 16
                    self.player.colBox = ColliderBox.ColliderBox(0, 0, 32, 32)
                if self.player.Rotation == Rotation.Rotation.WEST:
                    if self.__lock == False:
                        self.__lock = True
                        self.player.texPos.y = 0
                        self.player.texPos.x = 128
                        self.player.position.y -= 16
                        self.player.size.w = 16
                        self.player.size.h = 32
                        self.player.colBox = ColliderBox.ColliderBox(0, 0, 32, 32)
            elif self.__time >= 0.05 and self.__time < 0.1:
                if self.player.Rotation == Rotation.Rotation.SOUTH:
                    self.__lock = False
                    self.player.texPos.y = 16
                    self.player.texPos.x = 32
                    self.player.size.w = 32
                    self.player.size.h = 32
                if self.player.Rotation == Rotation.Rotation.EAST:
                    self.player.texPos.y = 16
                    self.player.texPos.x = 80
                    self.player.size.w = 32
                    self.player.size.h = 32
                if self.player.Rotation == Rotation.Rotation.NORTH:
                    if self.__lock == False:
                        self.__lock = True
                        self.player.texPos.y = 32
                        self.player.texPos.x = 112
                        self.player.position.y -= 16
                        self.player.size.w = 32
                        self.player.size.h = 32
                if self.player.Rotation == Rotation.Rotation.WEST:
                    if self.__lock2 == False:
                        self.__lock2 = True
                        self.__lock = False
                        self.player.texPos.y = 0
                        self.player.texPos.x = 144
                        self.player.position.x -= 16
                        self.player.size.w = 32
                        self.player.size.h = 32
            elif self.__time >= 0.1 and self.__time < 0.15:
                if self.player.Rotation == Rotation.Rotation.SOUTH:
                    if self.__lock == False:
                        self.__lock = True
                        self.player.texPos.y = 0
                        self.player.texPos.x = 64
                        self.player.position.x += 16
                        self.player.size.w = 16
                        self.player.size.h = 32
                if self.player.Rotation == Rotation.Rotation.EAST:
                    self.player.texPos.y = 0
                    self.player.texPos.x = 80
                    self.player.size.w = 32
                    self.player.size.h = 16
                if self.player.Rotation == Rotation.Rotation.NORTH:
                    self.player.texPos.y = 32
                    self.player.texPos.x = 64
                    self.player.size.w = 16
                    self.player.size.h = 32
                if self.player.Rotation == Rotation.Rotation.WEST:
                    if self.__lock == False:
                        self.__lock = True
                        self.__lock2 = False
                        self.player.texPos.y = 48
                        self.player.texPos.x = 80
                        self.player.position.y += 16
                        self.player.size.w = 32
                        self.player.size.h = 16
            elif self.__time >= 0.15:
                self.__lock = False
                self.player.state = Player.PlayerState.IDLE
                self.player.size.w = 16
                self.player.size.h = 16
                if self.player.Rotation == Rotation.Rotation.SOUTH:
                    self.player.texPos.y = 0
                    self.player.texPos.x = 0
                    self.player.colBox = ColliderBox.ColliderBox(2, 4, 12, 12)
                if self.player.Rotation == Rotation.Rotation.EAST:
                    self.player.texPos.y = 16
                    self.player.texPos.x = 0
                    self.player.colBox = ColliderBox.ColliderBox(2, 4, 12, 12)
                if self.player.Rotation == Rotation.Rotation.NORTH:
                    self.__lock = False
                    self.player.position.y += 16
                    self.player.texPos.y = 48
                    self.player.texPos.x = 0
                    self.player.colBox = ColliderBox.ColliderBox(2, 4, 12, 12)
                if self.player.Rotation == Rotation.Rotation.WEST:
                    self.__lock = False
                    self.player.position.x += 16
                    self.player.texPos.y = 32
                    self.player.texPos.x = 0
                    self.player.colBox = ColliderBox.ColliderBox(2, 4, 12, 12)
                self.__time = 0
                self.Attack = False