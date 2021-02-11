import Entities_Tile as Tile
import Utils_Position as Position
import Utils_ColliderBox as ColliderBox
import Utils_Scene as Scene
import Entities_Warp as Warp
import Entities_Cloud as Cloud
import Utils_Size as Size

def createScene0(tileTexture, assetTexture):
    scene0 = Scene.Scene()

    tilemap = [
         83,   8,   8,   8,  36,  8,  8,  8,  9,   9,
          8,   8,   9,   8,  36,  8,  9,  9,  8,   9,
          8, 102, 110, 110, 108,  8,  8,  9,  9,   8,
          8,  36,  64,  65,  65, 65, 65, 65, 65,  66,
          8,  36,  80,  81,  81, 81, 81, 81, 81,  82,
          8,  36,  80,  81,  81, 81, 81, 81, 81,  82,
        110, 108,  96,  97,  97, 97, 97, 97, 97,  98,
          8,   9,   9,   8,   8,  8,  9,  9,  9,   9,
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
        46,  0,  0,  0,  0,  0,  0,  0,  0,  196,
        0,  0,  0, 21,  0,  0,  136,  0,  0,  196,
        0,  0,  0,  0,  0,  0,  0,  0,  136,  196,
        0,  0,  0,  0,  0,  0,138,140,  0,  196,
        0,  0,  0,  0,  0,  0,154,156,  0,  196,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  196,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  196,
        184, 184, 182, 182,184, 184, 182, 182, 184,190,
    ]
    assetCollider = [
        1, 0, 0, 0, 0, 0, 0, 0, 0, 1,
        0, 0, 0, 1, 0, 0, 0, 0, 0, 1,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
        0, 0, 0, 0, 0, 0, 1, 1, 0, 1,
        0, 0, 0, 0, 0, 0, 1, 1, 0, 1,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    ]
    assets = []
    for i in range(0, len(assetmap)):
        if assetmap[i] != 0:
            asset = Tile.Tile(assetTexture)
            asset.position = Position.Position(i % 10 * 16, int(i / 10) * 16)
            asset.texPos = Position.Position(assetmap[i] % 16 * 16, int(assetmap[i] / 16) * 16)
            if assetCollider[i] == 1:
                asset.collider = True
            if assetmap[i] >= 128:
                asset.anime = True
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
# Warp vers Maison joueur
    warp = Warp.Warp()
    warp.warppos = Position.Position(0, -16)
    warp.colBox = ColliderBox.ColliderBox(0, 0, 160, 16)
    warp.tppos = Position.Position(0, 112)
    warp.sceneId = 1
    warp.IsDoor = False
    warps.append(warp)

# Warp vers Marchand
    warp = Warp.Warp()
    warp.warppos = Position.Position(-16, 0)
    warp.colBox = ColliderBox.ColliderBox(0, 0, 16, 144)
    warp.tppos = Position.Position(144, 0)
    warp.sceneId = 4
    warp.IsDoor = False
    warps.append(warp)

    scene0.ambiant = (225, 255, 255)
    scene0.type = Scene.TypeScene.EXTERIEUR
    scene0.tiles = tiles
    scene0.assets = assets
    scene0.plantes = plantes
    scene0.warps = warps
    scene0.clouds = clouds

    return scene0