import Entities_Player as Player
import Entities_Window as Window
import Entities_Tile as Tile
import Entities_Warp as Warp
import Entities_Item as Item
import Entities_Pognon as Pognon
import Entities_Heart as Heart
import Entities_Inventory as Inventory

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
import Scripts_Ambiant as Ambiant
import Scripts_CloudsTranslation as CloudsTranslation
import Scripts_Sleep as Sleep
import Scripts_DonutMan as DonutMan
import Scripts_Attack as Attack
import Scripts_Music as Music
import Scripts_GetHeart as GetHeart

import Scene_0 as Scene0
import Scene_1 as Scene1
import Scene_2 as Scene2
import Scene_3 as Scene3
import Scene_4 as Scene4
import Scene_5 as Scene5

import Utils_Position as Position
import Utils_Time as Time
import Utils_Scene as Scene
import Utils_ColliderBox as ColliderBox
import Utils_DungeonGen as DungeonGen
import Utils_Size as Size

import sys
import pygame

# init
pygame.init()
pygame.display.set_caption('Sweet Nightmare')
window = Window.Window()
t1 = pygame.time.get_ticks()
t2 = 0.0
clock = pygame.time.Clock()

# textures
playerTexture = pygame.image.load("res/Leguman.png").convert_alpha()
tileTexture = pygame.image.load("res/Tiles.png").convert_alpha()
assetTexture = pygame.image.load("res/Assets.png").convert_alpha()
debugTexture = pygame.image.load("res/Debug.png").convert_alpha()
uiTexture = pygame.image.load("res/ui.png").convert_alpha()
ennemyTexture = pygame.image.load("res/Ennemy.png").convert_alpha()
keur = pygame.image.load("res/3keur.png").convert_alpha()
reglesTexture = pygame.image.load("res/regles.png").convert_alpha()

# sounds
planterSon = pygame.mixer.Sound('sample/Planter.mp3')
planterSon.set_volume(0.08)
attaqueSoundFx = pygame.mixer.Sound('sample/attaque.mp3')
attaqueSoundFx.set_volume(0.08)
doorSoundFx = pygame.mixer.Sound('sample/porte.mp3')
doorSoundFx.set_volume(0.08)
oofSoundFx = pygame.mixer.Sound('sample/oof.mp3')
oofSoundFx.set_volume(0.08)
mobSoundFx = pygame.mixer.Sound('sample/zombie.mp3')
mobSoundFx.set_volume(0.04)
dungeonSound = pygame.mixer.Sound('sample/Battle_Dungeon.ogg')
dungeonSound.set_volume(0.04)
ExterieurSound = pygame.mixer.Sound('sample/Pas_dungeon.ogg')
ExterieurSound.set_volume(0.04)
InterieurSound = pygame.mixer.Sound('sample/shop2.mp3')
InterieurSound.set_volume(0.04)


# entities
scenes = []

scene0 = Scene0.createScene0(tileTexture, assetTexture)
scene0.state = False
scenes.append(scene0)

scene1 = Scene1.createScene1(tileTexture, assetTexture)
scene1.state = False
scenes.append(scene1)

scene2 = Scene2.createScene2(tileTexture, assetTexture)
scene2.state = True
scenes.append(scene2)

scene3 = Scene3.createScene3(tileTexture, assetTexture)
scene3.state = False
scenes.append(scene3)

scene4 = Scene4.createScene4(tileTexture, assetTexture)
scene4.state = False
scenes.append(scene4)

scene5 = Scene5.createScene5(reglesTexture)
scene5.state = False
scenes.append(scene5)

itemGraines = []

itemGraine0 = Item.Item(assetTexture)
itemGraine0.texPos = Position.Position(224, 16)
itemGraine0.position = Position.Position(16, 128)
itemGraine0.current = True
itemGraine0.quantity = 0
itemGraines.append(itemGraine0)

itemGraine1 = Item.Item(assetTexture)
itemGraine1.texPos = Position.Position(240, 0)
itemGraine1.position = Position.Position(48, 128)
itemGraine1.quantity = 5
itemGraine1.Item = Item.Items.GRN_PIMENT
itemGraines.append(itemGraine1)

itemLegumes = []

itemLegume0 = Item.Item(assetTexture)
itemLegume0.texPos = Position.Position(96, 48)
itemLegume0.position = Position.Position(16, 128)
itemLegume0.current = True
itemLegume0.quantity = 0
itemLegume0.Item = Item.Items.PASTEQUE
itemLegumes.append(itemLegume0)

itemLegume1 = Item.Item(assetTexture)
itemLegume1.texPos = Position.Position(112, 32)
itemLegume1.position = Position.Position(48, 128)
itemLegume1.quantity = 5
itemLegume1.Item = Item.Items.PIMENT
itemLegumes.append(itemLegume1)

inventory = Inventory.Inventory()
inventory.itemGraines = itemGraines
inventory.itemLegumes = itemLegumes

heart = Heart.Heart(keur)
heart.position = Position.Position(96, 128)
heart.texPos = Position.Position(0, 0)
heart.size = Size.Size(24, 8)

pognon = Pognon.Pognon(assetTexture)
pognon.texPos = Position.Position(240, 32)
pognon.position = Position.Position(144, 128)

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
playerAction.sound = attaqueSoundFx

donutMan = DonutMan.DonutMan()
donutMan.scenes = scenes
donutMan.player = player

collision = Collision.Collision()
collision.scenes = scenes
collision.player = player

getHeart = GetHeart.GetHeart()
getHeart.scenes = scenes
getHeart.player = player
getHeart.keur = heart

attack = Attack.Attack()
attack.scenes = scenes
attack.player = player
attack.pognon = pognon
attack.keur = heart
attack.sound = oofSoundFx
attack.soundMob = mobSoundFx
attack.assetTexture = assetTexture
attack.inventory = inventory

plantations = Plantations.Plantations()
plantations.player = player
plantations.scenes = scenes
plantations.texture = assetTexture
plantations.items = inventory
plantations.son = planterSon

scriptMarchand = ScriptMarchand.ScriptMarchand()
scriptMarchand.scenes = scenes
scriptMarchand.items = inventory
scriptMarchand.pognon = pognon
scriptMarchand.joueur = player
scriptMarchand.uiTexture = uiTexture
scriptMarchand.assetTexture = assetTexture

animation = Animation.Animation()
animation.scenes = scenes

cloudTranslation = CloudsTranslation.CloudsTranslation()
cloudTranslation.scenes = scenes

dynLight = DynLight.DynLight()
dynLight.scenes = scenes

ambiant = Ambiant.Ambiant()
ambiant.scenes = scenes

draw = Draw.Draw()
draw.window = window
draw.player = player
draw.scenes = scenes
draw.items = inventory
draw.pognon = pognon
draw.keur = heart

music = Music.Music()
music.interieur = InterieurSound
music.exterieur = ExterieurSound
music.donjon = dungeonSound
music.scenes = scenes

warpScript = WarpScript.WarpScript()
warpScript.player = player
warpScript.scenes = scenes
warpScript.sound = doorSoundFx
warpScript.inventory = inventory

sleep = Sleep.Sleep()
sleep.player = player
sleep.scenes = scenes
sleep.tileTexture = tileTexture
sleep.assetTexture = assetTexture
sleep.ennemyTexture = ennemyTexture
sleep.keurTexture = keur
sleep.inventory = inventory

frameCounter = FrameCounter.FrameCounter()

while window.open:
    # clock.tick(60)
    t2 = pygame.time.get_ticks()
    Time.Time.deltaTime = (t2 - t1) / 1000
    t1 = t2

    input.update()
    playerAction.update()
    donutMan.update()
    collision.update()
    getHeart.update()
    attack.update()
    scriptMarchand.update()
    plantations.update()
    animation.update()
    cloudTranslation.update()
    dynLight.update()
    # ambiant.update()
    draw.update()
    music.update()
    warpScript.update()
    sleep.update()
    frameCounter.update()

pygame.quit()