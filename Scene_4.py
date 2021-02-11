import Entities_Tile as Tile
import Utils_Position as Position
import Utils_ColliderBox as ColliderBox
import Utils_Scene as Scene
import Entities_Warp as Warp
import Entities_Light as Light
import Entities_Cloud as Cloud
import Utils_Size as Size

def createScene4(tileTexture, assetTexture):
    scene4 = Scene.Scene()

    tilemap = [
         8,  8,  8,  8,  8,  8,  8,  8,  9,  9,
         8,  8,  4,  4,  4,  4,  4,  9,  8,  9,
         8, 24, 58, 59, 60,  3,  7,  8,  9,  8,
         8,  2, 74, 75, 76,  2, 23,  8,  9,  8,
         8,  2,  2,  2,  2, 19, 25,  8,  8,  8,
         8,  8,  8,  8,  8,109,107,  9,  8,  8,
         8,  8,  9,  8,  9,  9,109,110,110,110,
         9,  8,  8,  8,  8,  8,  9,  8,  9,  9,
    ]
    
    tileCollider = [
        0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
        0, 0,  1, 1, 1, 1, 1, 0, 0, 0,
        0, 0,  1, 1, 1, 1, 1, 0, 0, 0,
        0, 0,  1, 1, 1, 0, 1, 0, 0, 0,
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
            if tilemap[i] >= 128:
                tile.anime = True
            tiles.append(tile)

    assetmap = [
        178,  0,   0,   0,  0,   0,   0,   28,  28, 28,
        178,   0,   0,   0,  0,   0,   0,  28, 136,  0,
        178,  64,   0,   0,  0,   0,  11,   0,   0,  0,
        178,   0,   0,   0,  0,  26,   0,   0,   0,  0,
        178, 136,   41, 42,  43,  0,   0,   0,   0,  0,
        178,   0,   0,   0,  0,   0,   0, 136,   0,  0,
        178,   0,   0,   0,  0,   0,   0,   0,   0,  0,
        180, 182, 184, 184,182, 182, 184, 184, 182,182,
    ]

    assetCollider = [
        1, 0, 0, 0, 0, 0, 0, 1, 1, 1,
        1, 0, 0, 0, 0, 0, 0, 1, 0, 0,
        1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    ]
    assets = []
    for i in range(0, len(assetmap)):
        if assetmap[i] != 0:
            asset = Tile.Tile(assetTexture)
            asset.position = Position.Position(i % 10 * 16, int(i / 10) * 16)
            asset.texPos = Position.Position(assetmap[i] % 16 * 16, int(assetmap[i] / 16) * 16)
            if assetmap[i] >= 128:
                asset.anime = True
            if assetCollider[i] == 1:
                asset.collider = True
            assets.append(asset)

    clouds = []

    cloud1 = Cloud.Cloud(assetTexture)
    cloud1.position = Position.Position(160, 144)
    cloud1.origin = Position.Position(160, 144)
    cloud1.size = Size.Size(48, 32)
    cloud1.texPos = Position.Position(176, 64)
    clouds.append(cloud1)

    cloud2 = Cloud.Cloud(assetTexture)
    cloud2.position = Position.Position(80, 200)
    cloud2.origin = Position.Position(160, 400)
    cloud2.size = Size.Size(48, 32)
    cloud2.texPos = Position.Position(176, 64)
    cloud2.speed = 24
    clouds.append(cloud2)

    cloud3 = Cloud.Cloud(assetTexture)
    cloud3.position = Position.Position(80, 90)
    cloud3.origin = Position.Position(160, 160)
    cloud3.size = Size.Size(48, 32)
    cloud3.texPos = Position.Position(176, 64)
    clouds.append(cloud3)

    cloud4 = Cloud.Cloud(assetTexture)
    cloud4.position = Position.Position(144, 20)
    cloud4.origin = Position.Position(160, 200)
    cloud4.size = Size.Size(48, 32)
    cloud4.speed = 24
    cloud4.texPos = Position.Position(176, 64)
    clouds.append(cloud4)

    plantes = []

    warps = []
# Warp vers Fermier
    warp = Warp.Warp()
    warp.warppos = Position.Position(86, 45)
    warp.colBox = ColliderBox.ColliderBox(4, 4, 8, 8)
    warp.tppos = Position.Position(64, 96)
    warp.sceneId = 3
    warps.append(warp)

    warp = Warp.Warp()
    warp.warppos = Position.Position(160, 0)
    warp.colBox = ColliderBox.ColliderBox(0, 0, 16, 144)
    warp.tppos = Position.Position(0, 128)
    warp.sceneId = 0
    warp.IsDoor = False
    warps.append(warp)

    #lights = []
    #light = Light.Light()
    #light.Color = (255, 128, 32)
    #light.Radius = 60
    #light.MaxRadius = 68
    #light.MinRadius = 60
    #light.Speed = 16
    #lights.append(light)

    scene4.ambiant = (225, 255, 255)
    scene4.type = Scene.TypeScene.EXTERIEUR
    scene4.tiles = tiles
    scene4.assets = assets
    scene4.plantes = plantes
    scene4.warps = warps
    scene4.clouds = clouds
    #scene4.lights = lights

    return scene4