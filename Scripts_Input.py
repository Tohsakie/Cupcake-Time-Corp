import sys
import pygame
import Entities_Player as Player
import Entities_Window as Window
import Entities_Plante as Plante
import Entities_Marchand as Marchand
import Utils_Scene as Scene

class Input:
    def __init__(self):
        self.window = None
        self.player = None
        self.scenes = []

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.window.open = False
            elif event.type == pygame.KEYDOWN:
            # window input
                if event.key == pygame.K_ESCAPE:
                    self.window.open = False
            # player input
                if event.key == pygame.K_z:
                    if self.player.state != Player.PlayerState.DISCUTION:
                        self.player.state = Player.PlayerState.MOVEUP
                    else:
                        for scene in self.scenes:
                            if scene.state == True:
                                for marchand in scene.marchands:
                                    if marchand.etat == Marchand.EtatMarchand.ACTIF:
                                        marchand.inventaireMarchand = Marchand.InventaireMarchand.INVENTAIRE_HAUT
                if event.key == pygame.K_UP:
                    if self.player.state != Player.PlayerState.DISCUTION:
                        self.player.state = Player.PlayerState.MOVEUP
                if event.key == pygame.K_s:
                    if self.player.state != Player.PlayerState.DISCUTION:
                        self.player.state = Player.PlayerState.MOVEDOWN
                    else:
                        for scene in self.scenes:
                            if scene.state == True:
                                for marchand in scene.marchands:
                                    if marchand.etat == Marchand.EtatMarchand.ACTIF:
                                        marchand.inventaireMarchand = Marchand.InventaireMarchand.INVENTAIRE_BAS
                if event.key == pygame.K_DOWN:
                    if self.player.state != Player.PlayerState.DISCUTION:
                        self.player.state = Player.PlayerState.MOVEDOWN
                if event.key == pygame.K_q:
                    if self.player.state != Player.PlayerState.DISCUTION:
                        self.player.state = Player.PlayerState.MOVELEFT
                if event.key == pygame.K_LEFT:
                    if self.player.state != Player.PlayerState.DISCUTION:
                        self.player.state = Player.PlayerState.MOVELEFT
                if event.key == pygame.K_d:
                    if self.player.state != Player.PlayerState.DISCUTION:
                        self.player.state = Player.PlayerState.MOVERIGHT
                if event.key == pygame.K_RIGHT:
                    if self.player.state != Player.PlayerState.DISCUTION:
                        self.player.state = Player.PlayerState.MOVERIGHT
                if event.key == pygame.K_e:
                    if self.player.state != Player.PlayerState.DISCUTION:
                        self.player.state = Player.PlayerState.PLANTATION
                    else:
                        for scene in self.scenes:
                            if scene.state == True:
                                for marchand in scene.marchands:
                                    if marchand.etat == Marchand.EtatMarchand.ACTIF:
                                        marchand.inventaireMarchand = Marchand.InventaireMarchand.INVENTAIRE_ACHAT
                if event.key == pygame.K_a:
                    self.player.state = Player.PlayerState.SWITCH_ITEM
                if event.key == pygame.K_r:
                    if self.player.state != Player.PlayerState.DISCUTION:
                        self.player.state = Player.PlayerState.ATTACK
                if event.key == pygame.K_2:
                    if self.player.state != Player.PlayerState.DISCUTION:
                        self.player.state = Player.PlayerState.ATTACKPIMENT









            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_z and self.player.state == Player.PlayerState.MOVEUP:
                    self.player.state = Player.PlayerState.IDLE
                if event.key == pygame.K_z and self.player.state == Player.PlayerState.DISCUTION:
                    for scene in self.scenes:
                        if scene.state == True:
                            for marchand in scene.marchands:
                                if marchand.etat == Marchand.EtatMarchand.ACTIF:
                                    marchand.inventaireMarchand = Marchand.InventaireMarchand.INVENTAIRE_RIEN
                if event.key == pygame.K_UP and self.player.state == Player.PlayerState.MOVEUP:
                    self.player.state = Player.PlayerState.IDLE
                if event.key == pygame.K_s and self.player.state == Player.PlayerState.MOVEDOWN:
                    self.player.state = Player.PlayerState.IDLE
                if event.key == pygame.K_s and self.player.state == Player.PlayerState.DISCUTION:
                    for scene in self.scenes:
                        if scene.state == True:
                            for marchand in scene.marchands:
                                if marchand.etat == Marchand.EtatMarchand.ACTIF:
                                    marchand.inventaireMarchand = Marchand.InventaireMarchand.INVENTAIRE_RIEN
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
                if event.key == pygame.K_e and self.player.state == Player.PlayerState.DISCUTION:
                    for scene in self.scenes:
                        if scene.state == True:
                            for marchand in scene.marchands:
                                if marchand.etat == Marchand.EtatMarchand.ACTIF:
                                    marchand.inventaireMarchand = Marchand.InventaireMarchand.INVENTAIRE_RIEN
                if event.key == pygame.K_r and self.player.state == Player.PlayerState.ATTACK:
                    self.player.state = Player.PlayerState.IDLE
                if event.key == pygame.K_2 and self.player.state == Player.PlayerState.ATTACKPIMENT:
                        self.player.state = Player.PlayerState.ATTACKPIMENT