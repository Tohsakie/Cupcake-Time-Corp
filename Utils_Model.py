import Utils_Position as Position
import Utils_Size as Size
import Utils_ColliderBox as ColliderBox
import pygame

class Drawable:
    def __init__(self, texture):
        self.texture = texture
        self.position = Position.Position()
        self.texPos = Position.Position()
        self.size = Size.Size()
        self.colBox= ColliderBox.ColliderBox()

    def draw(self, surface):
        if (surface != None):
            srect: pygame.Rect = pygame.Rect(self.texPos.x, self.texPos.y, self.size.w, self.size.h)
            drect: pygame.Rect = pygame.Rect(self.position.x, self.position.y, self.size.w, self.size.h)
            surface.blit(self.texture, drect, srect)