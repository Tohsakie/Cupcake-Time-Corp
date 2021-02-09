import sys
import pygame
import Entities_Player as Player
import Entities_Window as Window
import Entities_Plante as Plante
import Utils_Scene as Scene

class Input:
    def __init__(self):
        self.window = None
        self.player = None
        self.scenes = []

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
                if event.key == pygame.K_UP:
                        self.player.state = Player.PlayerState.MOVEUP
                if event.key == pygame.K_s:
                    self.player.state = Player.PlayerState.MOVEDOWN
                if event.key == pygame.K_DOWN:
                        self.player.state = Player.PlayerState.MOVEDOWN
                if event.key == pygame.K_q:
                    self.player.state = Player.PlayerState.MOVELEFT
                if event.key == pygame.K_LEFT:
                    self.player.state = Player.PlayerState.MOVELEFT
                if event.key == pygame.K_d:
                    self.player.state = Player.PlayerState.MOVERIGHT
                if event.key == pygame.K_RIGHT:
                    self.player.state = Player.PlayerState.MOVERIGHT
                if event.key == pygame.K_e:
                    self.player.state = Player.PlayerState.PLANTATION
                if event.key == pygame.K_a:
                    self.player.state = Player.PlayerState.SWITCH_ITEM
                #### A SUPPRIMER ####
                if event.key == pygame.K_m:
                    for scene in self.scenes:
                        if scene.state == True:
                            for plante in scene.plantes:
                                plante.state = Plante.PlanteState.FRUIT
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_z and self.player.state == Player.PlayerState.MOVEUP:
                    self.player.state = Player.PlayerState.IDLE
                if event.key == pygame.K_UP and self.player.state == Player.PlayerState.MOVEUP:
                    self.player.state = Player.PlayerState.IDLE
                if event.key == pygame.K_s and self.player.state == Player.PlayerState.MOVEDOWN:
                    self.player.state = Player.PlayerState.IDLE
                if event.key == pygame.K_DOWN and self.player.state == Player.PlayerState.MOVEDOWN:
                    self.player.state = Player.PlayerState.IDLE
                if event.key == pygame.K_q and self.player.state == Player.PlayerState.MOVELEFT:
                    self.player.state = Player.PlayerState.IDLE
                if event.key == pygame.K_LEFT and self.player.state == Player.PlayerState.MOVELEFT:
                    self.player.state = Player.PlayerState.IDLE
                if event.key == pygame.K_d and self.player.state == Player.PlayerState.MOVERIGHT:
                    self.player.state = Player.PlayerState.IDLE
                if event.key == pygame.K_RIGHT and self.player.state == Player.PlayerState.MOVERIGHT:
                    self.player.state = Player.PlayerState.IDLE
                if event.key == pygame.K_e and self.player.state == Player.PlayerState.PLANTATION:
                    self.player.state = Player.PlayerState.IDLE