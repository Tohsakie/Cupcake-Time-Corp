import Entities_Tile as Tile
import Utils_Position as Position
import Utils_ColliderBox as ColliderBox
import Utils_Scene as Scene
import Entities_Warp as Warp
import Entities_Light as Light

def createScene4(tileTexture, assetTexture):
    scene4 = Scene.Scene()

    tilemap = [
        2,  2,  2,  2,  2,  2,  2,  2,  1,  1,
        2,  2,  4,  4,  4,  4,  4,  1,  2,  1,
        2,  2,  5,  3,  3,  3,  7,  2,  1,  2,
        2,  2, 21, 22,  2, 22, 23,  2,  1,  2,
        2,  2,  2,  2,  2,  2,  2,  2,  2,  2,
        2,  2,  2,  2, 19,  2,  1,  1,  2,  2,
        2,  2,  1,  2, 35,  1,  1,  2,  2,  1,
        1,  2,  2,  2, 35,  2,  1,  2,  1,  1,
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
         0,  0,   0,   0,  0,   0,   0,  0,  0,  0,
         0,  0,   0,   0,  0,   0,   0,  0,  0,  0,
         0,  0,   0,   0,  0,   0,   0,  0,  0,  0,
         0,  0,   0,   0,  0,   0,   0,  0,  0,  0,
         0,  0,   0,   0,  0,   0,   0,  0,  0,  0,
         0,  0,   0,   0,  0,   0,   0,  0,  0,  0,
         0,  0,   0,   0,  0,   0,   0,  0,  0,  0,
         0,  0,   0,   0,  0,   0,   0,  0,  0,  0,
    ]
    assetCollider = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
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
            if assetmap[i] >= 128:
                asset.anime = True
            if assetCollider[i] == 1:
                asset.collider = True
            assets.append(asset)

    plantes = []

    warps = []
# Warp vers Fermier
    warp = Warp.Warp()
    warp.warppos = Position.Position(64, 48)
    warp.colBox = ColliderBox.ColliderBox(4, 4, 8, 8)
    warp.tppos = Position.Position(64, 96)
    warp.sceneId = 3
    warps.append(warp)

    #lights = []
    #light = Light.Light()
    #light.Color = (255, 128, 32)
    #light.Radius = 60
    #light.MaxRadius = 68
    #light.MinRadius = 60
    #light.Speed = 16
    #lights.append(light)

    scene4.ambiant = (192, 128, 96)
    scene4.tiles = tiles
    scene4.assets = assets
    scene4.plantes = plantes
    scene4.warps = warps
    #scene4.lights = lights

    return scene4
