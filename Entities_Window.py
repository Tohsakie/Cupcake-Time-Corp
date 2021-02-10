import pygame

class Window:
    def __init__(self):
        self.width = 160
        self.height = 144
        self.scalingFactor = 5
        self.open = True
        self.window = pygame.display.set_mode((self.width * self.scalingFactor, self.height * self.scalingFactor))
        self.screen = pygame.Surface((self.width, self.height))
        self.font = pygame.font.SysFont("res/Links_awakening_font.ttf", 16)