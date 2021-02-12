import Entities_Tile as Tile
import Utils_Position as Position
import Utils_ColliderBox as ColliderBox
import Utils_Scene as Scene
import Entities_Warp as Warp
import Entities_Light as Light
import Entities_Cloud as Cloud
import Utils_Size as Size

def createScene1(tileTexture, assetTexture):
    scene1 = Scene.Scene()

    tilemap = [
        8,  8,  8,  8,  8,  8,  8,  8,  9,  9,
        8,  8,  4,  4,  4,  4,  4,  9,  8,  9,
        8, 24,  5,  3,  3,  3,  7,  8,  9,  8,
        8,  2, 21, 22,  2, 22, 23,  8,  9,  8,
        8,  2,  2,  2,  2,  2, 25,  8,  8,  8,
        8,  8,  8,  8, 20,  8,  9,  9,  8,  8,
        8,  8,  9,  8, 36,  9,  9,  8,  8,  9,
        9,  8,  8,  8, 36,  8,  9,  8,  9,  9,
    ]
    tileCollider = [
        0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
        0, 0,  1, 1, 1, 1, 1, 0, 0, 0,
        0, 0,  1, 1, 1, 1, 1, 0, 0, 0,
        0, 0,  1, 1, 0, 1, 1, 0, 0, 0,
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
         0, 21,   0, 136,  0,   0,   0,  0,  0,  196,
         0,  0,   0,   0,  0,   0,   0,  0, 21,  196,
        64, 64, 144, 146,  0, 144, 146, 64, 64, 196,
        62, 62, 160, 162, 26, 160, 162,  0,  63,  196,
        62, 62,   0,   0,  0,   0,   0,0,  0,  196,
        62,  0, 128,   0,  0,  37,   0,  0,  0,  196,
        62,  0,   0,   0,  0,   0,   0,  0,136,  196,
        62,  0,   0,   0,  0,   0,   0,  0,  0,  196,
    ]
    assetCollider = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
        1, 1, 0, 0, 0, 0, 0, 1, 1, 1,
        1, 1, 0, 0, 0, 0, 0, 0, 0, 1,
        1, 1, 0, 0, 0, 0, 0, 0, 0, 1,
        1, 0, 1, 0, 0, 1, 0, 0, 0, 1,
        1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
        1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
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
# Warp vers Champ
    warp = Warp.Warp()
    warp.warppos = Position.Position(0, 128)
    warp.colBox = ColliderBox.ColliderBox(0, 0, 160, 16)
    warp.tppos = Position.Position(0, 0)
    warp.sceneId = 0
    warp.IsDoor = False
    warps.append(warp)

# Warp vers Maison Joueur
    warp = Warp.Warp()
    warp.warppos = Position.Position(64, 48)
    warp.colBox = ColliderBox.ColliderBox(4, 4, 8, 8)
    warp.tppos = Position.Position(0, 96)
    warp.sceneId = 2
    warps.append(warp)

# Warp vers Regles
    warp = Warp.Warp()
    warp.warppos = Position.Position(128, 48)
    warp.colBox = ColliderBox.ColliderBox(4, 4, 8, 8)
    warp.tppos = Position.Position(-20, 20)
    warp.sceneId = 5
    warps.append(warp)  

    lights = []
    light = Light.Light()
    light.Color = (255, 128, 32)
    light.position = Position.Position(203, 443)
    light.Radius = 80
    light.MaxRadius = 88
    light.MinRadius = 72
    light.Speed = 16
    lights.append(light)

    scene1.ambiant = (225, 255, 255)
    scene1.type = Scene.TypeScene.EXTERIEUR
    scene1.tiles = tiles
    scene1.assets = assets
    scene1.plantes = plantes
    scene1.warps = warps
    scene1.lights = lights
    scene1.clouds = clouds

    return scene1