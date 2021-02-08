import Entities_Player as Player
import Entities_Window as Window
import Entities_Tile as Tile

import Scripts_Input as Input
import Scripts_PlayerAction as PlayerAction
import Scripts_Draw as Draw
import Scripts_FrameCounter as FrameCounter

import Utils_Position as Position
import Utils_Time as Time

import sys
import pygame

# init
pygame.init()
window = Window.Window()
t1 = pygame.time.get_ticks()
t2 = 0.0

# textures
playerTexture = pygame.image.load("res/Player.png").convert_alpha()
tileTexture = pygame.image.load("res/Tiles.png").convert_alpha()

# entities
tile = Tile.Tile(tileTexture)
tile.position = Position.Position(16, 32)
tile.texPos = Position.Position(16, 0)
player = Player.Player(playerTexture)

# scripts
input = Input.Input()
input.window = window
input.player = player

playerAction = PlayerAction.PlayerAction()
playerAction.player = player

draw = Draw.Draw()
draw.window = window
draw.player = player
draw.tile = tile

frameCounter = FrameCounter.FrameCounter()

clock = pygame.time.Clock()

while window.open:
    # clock.tick(60)
    t2 = pygame.time.get_ticks()
    Time.Time.deltaTime = (t2 - t1) / 1000
    t1 = t2

    input.update()
    playerAction.update()
    draw.update()
    frameCounter.update()

pygame.quit()