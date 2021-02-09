import Entities_Player as Player
import Entities_Window as Window
import Entities_Tile as Tile
import Entities_Warp as Warp
import Entities_Item as Item

import Scripts_Input as Input
import Scripts_PlayerAction as PlayerAction
import Scripts_Collision as Collision
import Scripts_DynLight as DynLight
import Scripts_Draw as Draw
import Scripts_FrameCounter as FrameCounter
import Scripts_Plantations as Plantations
import Scripts_Warp as WarpScript
import Scripts_Animation as Animation
import Scripts_Marchand as ScriptMarchand

import Scene_0 as Scene0
import Scene_1 as Scene1
import Scene_2 as Scene2
import Scene_3 as Scene3
import Scene_4 as Scene4

import Utils_Position as Position
import Utils_Time as Time
import Utils_Scene as Scene
import Utils_ColliderBox as ColliderBox

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
uiTexture = pygame.image.load("res/ui.png").convert_alpha()

# entities
scenes = []

scene0 = Scene0.createScene0(tileTexture, assetTexture)
scene0.state = False
scenes.append(scene0)

scene1 = Scene1.createScene1(tileTexture, assetTexture)
scene1.state = False
scenes.append(scene1)

scene2 = Scene2.createScene2(tileTexture, assetTexture)
scene2.state = False
scenes.append(scene2)

scene3 = Scene3.createScene3(tileTexture, assetTexture)
scene3.state = False
scenes.append(scene3)

scene4 = Scene4.createScene4(tileTexture, assetTexture)
scene4.state = True
scenes.append(scene4)

items = []

item0 = Item.Item(assetTexture)
item0.texPos = Position.Position(224, 16)
item0.position = Position.Position(16, 128)
item0.current = False
items.append(item0)

item1 = Item.Item(assetTexture)
item1.texPos = Position.Position(240, 0)
item1.position = Position.Position(48, 128)
item1.Item = Item.Items.GRN_PIMENT
items.append(item1)

player = Player.Player(playerTexture)
player.colBox = ColliderBox.ColliderBox(2, 4, 12, 12)
player.position = Position.Position(16, 64)

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
plantations.items = items

scriptMarchand = ScriptMarchand.ScriptMarchand()
scriptMarchand.scenes = scenes
scriptMarchand.joueur = player
scriptMarchand.uiTexture = uiTexture

animation = Animation.Animation()
animation.scenes = scenes

dynLight = DynLight.DynLight()
dynLight.scenes = scenes

draw = Draw.Draw()
draw.window = window
draw.player = player
draw.scenes = scenes
draw.items = items

warpScript = WarpScript.WarpScript()
warpScript.player = player
warpScript.scenes = scenes

frameCounter = FrameCounter.FrameCounter()

clock = pygame.time.Clock()

while window.open:
    clock.tick(144)
    t2 = pygame.time.get_ticks()
    Time.Time.deltaTime = (t2 - t1) / 1000
    t1 = t2

    input.update()
    playerAction.update()
    collision.update()
    scriptMarchand.update()
    plantations.update()
    animation.update()
    dynLight.update()
    draw.update()
    warpScript.update()
    frameCounter.update()

pygame.quit()