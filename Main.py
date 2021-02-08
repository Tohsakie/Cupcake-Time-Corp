import Entities_Player as Player
import Entities_Window as Window
import Entities_Tile as Tile

import Scripts_Input as Input
import Scripts_PlayerAction as PlayerAction
import Scripts_Collision as Collision
import Scripts_Draw as Draw
import Scripts_FrameCounter as FrameCounter
import Scripts_Plantations as Plantations

import Scene_1 as Scene1
import Scene_2 as Scene2
import Scene_house as SceneHouse

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
scene1 = Scene1.createScene1(tileTexture, assetTexture)
scene1.state = False
scenes.append(scene1)
scene2 = Scene2.createScene2(tileTexture, assetTexture)
scene2.state = False
scenes.append(scene2)

scenehouse = SceneHouse.createSceneHouse(tileTexture, assetTexture)
scenehouse.state = True
scenes.append(scenehouse)

player = Player.Player(playerTexture)
player.position.x = 64
player.position.y = 64

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
    frameCounter.update()

pygame.quit()