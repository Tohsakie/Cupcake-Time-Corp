import Entities_Player as Player
import Entities_Window as Window
import Entities_Tile as Tile

import Scripts_Input as Input
import Scripts_PlayerAction as PlayerAction
import Scripts_Collision as Collision
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
assetTexture = pygame.image.load("res/Assets.png").convert_alpha()
debugTexture = pygame.image.load("res/Debug.png").convert_alpha()

# entities
tilemap = [
    1, 1,  1, 0, 0, 0, 0, 0, 0, 0,
    1, 1,  1, 0, 0, 0, 0, 0, 0, 0,
    0, 1,  1, 0, 0, 0, 0, 0, 0, 0,
    0, 1,  1, 0, 0, 0, 0, 0, 0, 0,
    0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
    0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
    0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
    0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
    0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
]
tileCollider = [
    0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
    0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
    0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
    0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
    0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
    0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
    0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
    0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
    0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
]
tiles = []
for i in range(0, len(tilemap)):
    if tilemap[i] != 0:
        tile = Tile.Tile(tileTexture)
        tile.position = Position.Position(i % 10 * 16, int(i / 10) * 16)
        tile.texPos = Position.Position(tilemap[i] % 16 * 16, int(tilemap[i] / 16) * 16)
        if tileCollider[i] == 1:
            tile.collider = True
        tiles.append(tile)

assetmap = [
    0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
    0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 21, 0, 0, 0, 0, 0, 0, 0,
    0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
    0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
    0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
    0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
    0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
    0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
]
assetCollider = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
assets = []
for i in range(0, len(assetmap)):
    if assetmap[i] != 0:
        asset = Tile.Tile(assetTexture)
        asset.position = Position.Position(i % 10 * 16, int(i / 10) * 16)
        asset.texPos = Position.Position(assetmap[i] % 16 * 16, int(assetmap[i] / 16) * 16)
        if assetCollider[i] == 1:
            tile.collider = True
        assets.append(asset)

player = Player.Player(playerTexture)

# scripts
input = Input.Input()
input.window = window
input.player = player

playerAction = PlayerAction.PlayerAction()
playerAction.player = player

collision = Collision.Collision()
collision.tiles = tiles
collision.assets = assets
collision.player = player

draw = Draw.Draw()
draw.window = window
draw.player = player
draw.tiles = tiles
draw.assets = assets

frameCounter = FrameCounter.FrameCounter()

clock = pygame.time.Clock()

while window.open:
    # clock.tick(60)
    t2 = pygame.time.get_ticks()
    Time.Time.deltaTime = (t2 - t1) / 1000
    t1 = t2

    input.update()
    playerAction.update()
    collision.update()
    draw.update()
    frameCounter.update()

pygame.quit()