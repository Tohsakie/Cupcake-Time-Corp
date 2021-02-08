import sys
import pygame
import Entities_Player as Player
import Entities_Window as Window

class Input:
    def __init__(self):
        self.window = None
        self.player = None

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
            # window input
                if event.key == pygame.K_ESCAPE:
                    self.window.open = False
            # player input
                if event.key == pygame.K_z:
                    self.player.state = Player.PlayerState.MOVEUP
                if event.key == pygame.K_s:
                    self.player.state = Player.PlayerState.MOVEDOWN
                if event.key == pygame.K_q:
                    self.player.state = Player.PlayerState.MOVELEFT
                if event.key == pygame.K_d:
                    self.player.state = Player.PlayerState.MOVERIGHT
                if event.key == pygame.K_a:
                    self.player.state = Player.PlayerState.WINDATTRACT
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_z and self.player.state == Player.PlayerState.MOVEUP:
                    self.player.state = Player.PlayerState.IDLE
                if event.key == pygame.K_s and self.player.state == Player.PlayerState.MOVEDOWN:
                    self.player.state = Player.PlayerState.IDLE
                if event.key == pygame.K_q and self.player.state == Player.PlayerState.MOVELEFT:
                    self.player.state = Player.PlayerState.IDLE
                if event.key == pygame.K_d and self.player.state == Player.PlayerState.MOVERIGHT:
                    self.player.state = Player.PlayerState.IDLE
                if event.key == pygame.K_a and self.player.state == Player.PlayerState.WINDATTRACT:
                    self.player.state = Player.PlayerState.IDLE