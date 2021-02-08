import Entities_Player as Player
import Entities_Window as Window
import Entities_Tile as Tile
import pygame
import Utils_Scene as Scene

class Draw:
    def __init__(self):
        self.window = None
        self.player = None
        self.scenes = []

    def update(self):
        self.window.screen.fill((0, 0, 0))
        for scene in self.scenes:
            if scene.state == True:
                for tile in scene.tiles:
                    tile.draw(self.window.screen)
                for asset in scene.assets:
                    asset.draw(self.window.screen)
                for plante in scene.plantes:
                    plante.draw(self.window.screen)
        self.player.draw(self.window.screen)

    # Rescale
        self.window.window.blit(pygame.transform.scale(self.window.screen, (160*4, 144*4)), (0, 0))

    # Ambiant Light
        #mask = pygame.surface.Surface((160*4, 144*4)).convert_alpha()
        #mask.fill((0, 0, 0, 64))
        #self.window.window.blit(mask,(0,0))

    # Point Light
        #maskLight = pygame.surface.Surface((160*4, 144*4)).convert_alpha()
        #maskLight.fill((0,0,0,0))
        #radius = 64
        #intensite = 0
        #while radius > 0:
        #    pygame.draw.circle(maskLight, (255, 128, 32, intensite), (128, 128), radius)
        #    intensite += 16
        #    radius -= 8
        #self.window.window.blit(maskLight,(0,0))
        
        pygame.display.update()

        # pygame.display.flip()