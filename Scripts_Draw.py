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
        self.items = []

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
        for item in self.items:
            item.draw(self.window.screen)
            img = self.window.font.render(str(item.quantity), False, (224, 224, 224))
            self.window.screen.blit(img, (item.position.x - 14, 131))
        self.player.draw(self.window.screen)
        for scene in self.scenes:
            if scene.state == True:
                for ui in scene.ui:
                    ui.draw(self.window.screen)

    # Rescale
        self.window.window.blit(pygame.transform.scale(self.window.screen, (160*4, 144*4)), (0, 0))

    # Ambiant Light
        mask = pygame.surface.Surface((160*4, 144*4)).convert_alpha()
        for scene in self.scenes:
            if scene.state == True:
                mask.fill(scene.ambiant)

    # Point Light
        for scene in self.scenes:
            if scene.state == True:
                for light in scene.lights:
                    radius = light.Radius
                    intensite = 1.0
                    (r, g, b) = light.Color
                    while radius > 0:
                        pygame.draw.circle(mask, (r, g, b), (162, 354), radius)
                        (r, g, b) = (min(int(r * intensite), 255), min(int(g * intensite), 255), min(int(b * intensite), 255))
                        intensite += 0.1
                        radius -= 4
        
        self.window.window.blit(mask, (0,0), special_flags = pygame.BLEND_MULT)
        
        pygame.display.update()

        # pygame.display.flip()