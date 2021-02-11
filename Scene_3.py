import Entities_Tile as Tile
import Entities_Marchand as Marchand
import Utils_Position as Position
import Utils_Scene as Scene
import Entities_Warp as Warp
import Utils_ColliderBox as ColliderBox
import Entities_Light as Light

def createScene3(tileTexture, assetTexture):
    scene3 = Scene.Scene()

    tilemap = [
        12,  14,  30,  14,  14,  14,  14,  30,  14,  13,
        44,   3,   3,   3,   3,   3,   3,   3,   3,  45,
        44,   3,   3,   3,   3,   3,   3,   3,   3,  45,
        44,   3,   3,   3,   3,   3,   3,   3,   3,  45,
        44,   3,   3,   3,   3,   3,   3,   3,   3,  45,
        44,   3,   3,   3,   3,   3,   3,   3,   3,  45,
        44,   3,   3,   3,   3,   3,   3,   3,   3,  45,
        28,  15,  15,  15,   15,  3,  15,  15,  15,  29,
    ]
    tileCollider = [
        1, 1,  1, 1, 1, 1, 1, 1, 1, 1,
        1, 0,  0, 0, 0, 0, 0, 0, 0, 1,
        1, 0,  0, 0, 0, 0, 0, 0, 0, 1,
        1, 0,  0, 0, 0, 0, 0, 0, 0, 1,
        1, 0,  0, 0, 0, 0, 0, 0, 0, 1,
        1, 0,  0, 0, 0, 0, 0, 0, 0, 1,
        1, 0,  0, 0, 0, 0, 0, 0, 0, 1,
        1, 1,  1, 1, 1, 0, 1, 1, 1, 1,
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
         0,  0,   0,   0,   0,   0,  74,   0, 74,  0,
         0,  0,  40,   0,   0,   0,  90,   0, 90,  0,
         0,105, 106, 107,  88,  87,  89,   0,  0,  0,
         0,  0,   0,   0,   0,   0,   0,   0,  0,  0,
         0,  0,   0,   0,   0,   0,   0,   0, 23,  0,
         0,  0,   0,   0,   0,   0,   0,   0,  0,  0,
         0, 23,   0,   0,   0,   0,   0,   0,  0,  0,
         0,  0,   0,   0,  61,   24, 61,   0,  0,  0,
    ]
    assetCollider = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 1, 0, 1, 0,
        0, 1, 1, 1, 1, 1, 1, 0, 0, 0,
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
                asset.collider = True
            assets.append(asset)

    plantes = []

    warps = []
# Warp vers Fermier
    warp = Warp.Warp()
    warp.warppos = Position.Position(80, 112)
    warp.colBox = ColliderBox.ColliderBox(4, 4, 8, 8)
    warp.tppos = Position.Position(0, 64)
    warp.sceneId = 4
    warps.append(warp)

    marchands = []
    marchand = Marchand.Marchand()
    marchand.pos = Position.Position(32, 48)
    marchands.append(marchand)

    lights = []

    light1 = Light.Light()
    light1.Color = (224, 255, 255)
    light1.position = Position.Position(40, 8)
    light1.Radius = 32
    light1.MaxRadius = 33
    light1.MinRadius = 31
    light1.Speed = 2
    lights.append(light1)

    light2 = Light.Light()
    light2.Color = (224, 255, 255)
    light2.position = Position.Position(120, 8)
    light2.Radius = 32
    light2.MaxRadius = 33
    light2.MinRadius = 31
    light2.Speed = 2
    lights.append(light2)

    light3 = Light.Light()
    light3.Color = (255, 224, 192)
    light3.position = Position.Position(72, 120)
    light3.Radius = 24
    light3.MaxRadius = 26
    light3.MinRadius = 22
    light3.Speed = 4
    lights.append(light3)

    light4 = Light.Light()
    light4.Color = (255, 224, 192)
    light4.position = Position.Position(104, 120)
    light4.Radius = 24
    light4.MaxRadius = 26
    light4.MinRadius = 22
    light4.Speed = 4
    lights.append(light4)

    scene3.ambiant = (160, 192, 128)
    scene3.type = Scene.TypeScene.INTERIEUR
    scene3.tiles = tiles
    scene3.assets = assets
    scene3.plantes = plantes
    scene3.marchands = marchands
    scene3.warps = warps
    scene3.lights = lights

    return scene3