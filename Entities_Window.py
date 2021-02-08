import pygame

class Window:
    def __init__(self):
        self.width = 160
        self.height = 144
        self.scalingFactor = 4
        self.open = True
        self.window = pygame.display.set_mode((self.width * self.scalingFactor, self.height * self.scalingFactor))
        self.screen = pygame.Surface((self.width, self.height))