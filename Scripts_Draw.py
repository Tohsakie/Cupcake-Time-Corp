import Entities_Player as Player
import Entities_Window as Window
import Entities_Tile as Tile
import pygame
import Utils_Scene as Scene

class Draw:
    def __init__(self):
        self.window = None
        self.player = None
        self.pognon = None
        self.scenes = []
        self.items = None
        self.keur = None
        self.oldDay = 1
        self.font2 = pygame.font.SysFont("res/Links_awakening_font.ttf", 12)

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
                for monster in scene.monsters:
                    monster.draw(self.window.screen)
                for heartItem in scene.heartsItems:
                    heartItem.draw(self.window.screen)
                for attackpiment in scene.attackPiment:
                    attackpiment.draw(self.window.screen)
        self.player.draw(self.window.screen)
        for scene in self.scenes:
            if scene.state == True:
                for cloud in scene.clouds:
                    cloud.draw(self.window.screen)
                for ui in scene.ui:
                    ui.draw(self.window.screen)
                    if ui.quantity > 0:
                        img = self.window.font.render(str(ui.quantity), False, (224, 224, 224))
                        self.window.screen.blit(img, (ui.position.x + 19, ui.position.y + 3))
        if self.items.IsGraines == True:
            for item in self.items.itemGraines:
                item.draw(self.window.screen)
                img = self.window.font.render(str(item.quantity), False, (224, 224, 224))
                self.window.screen.blit(img, (item.position.x - 14, 131))
            img2 = self.font2.render("Jour:" + str(self.player.nbJour), False, (224, 224, 224))
            self.window.screen.blit(img2, (65, 132))
        else:
            for item in self.items.itemLegumes:
                item.draw(self.window.screen)
                img = self.window.font.render(str(item.quantity), False, (224, 224, 224))
                self.window.screen.blit(img, (item.position.x - 14, 131))
            img2 = self.font2.render("Nuit:" + str(self.player.nbJour), False, (224, 224, 224))
            self.window.screen.blit(img2, (65, 132))



        self.keur.draw(self.window.screen)
        self.pognon.draw(self.window.screen)
        img = self.window.font.render(str(self.pognon.pognon), False, (224, 224, 224))
        self.window.screen.blit(img, (self.pognon.position.x - 16, 131))

    # pixel light
        mask = pygame.surface.Surface((160, 128)).convert_alpha()
        for scene in self.scenes:
            if scene.state == True:
                mask.fill(scene.ambiant)

        for scene in self.scenes:
            if scene.state == True:
                for light in scene.lights:
                    radius = light.Radius
                    intensite = 1.0
                    (r, g, b) = light.Color
                    #while radius > 0:
                    #    pygame.draw.circle(mask, (r, g, b), (light.position.x, light.position.y), radius)
                    #    (r, g, b) = (min(int(r * intensite), 255), min(int(g * intensite), 255), min(int(b * intensite), 255))
                    #    intensite += 0.1
                    #    radius -= 4
                    pygame.draw.circle(mask, (r, g, b), (light.position.x, light.position.y), radius)

        self.window.screen.blit(mask, (0,0), special_flags = pygame.BLEND_MULT)

    # Rescale
        self.window.window.blit(pygame.transform.scale(self.window.screen, (160*5, 144*5)), (0, 0))

    # Ambiant Light
        #mask = pygame.surface.Surface((160*5, 128*5)).convert_alpha()
        #for scene in self.scenes:
        #    if scene.state == True:
        #        mask.fill(scene.ambiant)

    # Point Light
        #for scene in self.scenes:
        #    if scene.state == True:
        #        for light in scene.lights:
        #            radius = light.Radius
        #            intensite = 1.0
        #            (r, g, b) = light.Color
        #            while radius > 0:
        #                pygame.draw.circle(mask, (r, g, b), (light.position.x, light.position.y), radius)
        #                (r, g, b) = (min(int(r * intensite), 255), min(int(g * intensite), 255), min(int(b * intensite), 255))
        #                intensite += 0.1
        #                radius -= 4
        
        #self.window.window.blit(mask, (0,0), special_flags = pygame.BLEND_MULT)

        #  img = self.window.font.render(str("test"), True, (224, 224, 224))
        # self.window.screen.blit(img, (10, 10))
        # print(self.oldDay)
        # print("-")
        # print(self.player.nbJour)

        # if self.oldDay != self.player.nbJour :
        #     img = self.window.font.render(str("test"), True, (224, 224, 224))
        #     self.window.screen.blit(img, (10, 10))
        #     self.oldDay == self.player.nbJour
        #     self.oldDay += 1 

        pygame.display.update()

        # pygame.display.flip()