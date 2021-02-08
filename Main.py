import Entities_Player as Player
import Entities_Window as Window
import Entities_Tile as Tile
import Entities_Warp as Warp

import Scripts_Input as Input
import Scripts_PlayerAction as PlayerAction
import Scripts_Collision as Collision
import Scripts_Draw as Draw
import Scripts_FrameCounter as FrameCounter
import Scripts_Plantations as Plantations
import Scripts_Warp as WarpScript

import Scene_0 as Scene0
import Scene_1 as Scene1

import Utils_Position as Position
import Utils_Time as Time
import Utils_Scene as Scene

import sys
import pygame

# init
pygame.init()
window = Window.Window()
t1 = pygame.time.get_ticks()
t2 = 0.0

# textures
playerTexture = pygame.image.load("res/Leguman.png").convert_alpha()
tileTexture = pygame.image.load("res/Tiles.png").convert_alpha()
assetTexture = pygame.image.load("res/Assets.png").convert_alpha()
debugTexture = pygame.image.load("res/Debug.png").convert_alpha()

# entities
scenes = []

scene0 = Scene0.createScene0(tileTexture, assetTexture)
scene0.state = True
scenes.append(scene0)

scene1 = Scene1.createScene1(tileTexture, assetTexture)
scenes.append(scene1)

player = Player.Player(playerTexture)
player.position.x = 16
player.position.y = 16

# scripts
input = Input.Input()
input.window = window
input.player = player
input.scenes = scenes

playerAction = PlayerAction.PlayerAction()
playerAction.player = player

collision = Collision.Collision()
collision.scenes = scenes
collision.player = player

plantations = Plantations.Plantations()
plantations.player = player
plantations.scenes = scenes
plantations.texture = assetTexture

draw = Draw.Draw()
draw.window = window
draw.player = player
draw.scenes = scenes

warpScript = WarpScript.WarpScript()
warpScript.player = player
warpScript.scenes = scenes

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
    plantations.update()
    draw.update()
    warpScript.update()
    frameCounter.update()

pygame.quit()