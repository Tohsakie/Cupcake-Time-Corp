import Entities_Tile as Tile
import Entities_Marchand as Marchand
import Utils_Position as Position
import Utils_Scene as Scene
import Entities_Warp as Warp
import Utils_ColliderBox as ColliderBox

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
        28,  15,  15,  15,   3,  15,  15,  15,  15,  29,
    ]
    tileCollider = [
        1, 1,  1, 1, 1, 1, 1, 1, 1, 1,
        1, 0,  0, 0, 0, 0, 0, 0, 0, 1,
        1, 0,  0, 0, 0, 0, 0, 0, 0, 1,
        1, 0,  0, 0, 0, 0, 0, 0, 0, 1,
        1, 0,  0, 0, 0, 0, 0, 0, 0, 1,
        1, 0,  0, 0, 0, 0, 0, 0, 0, 1,
        1, 0,  0, 0, 0, 0, 0, 0, 0, 1,
        1, 1,  1, 1, 0, 1, 1, 1, 1, 1,
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
        0,  0,   0,   0,  24,   0,   0,   0,  0,  0,
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
    warp.warppos = Position.Position(64, 112)
    warp.colBox = ColliderBox.ColliderBox(4, 4, 8, 8)
    warp.tppos = Position.Position(0, 64)
    warp.sceneId = 4
    warps.append(warp)

    marchands = []
    marchand = Marchand.Marchand()
    marchand.pos = Position.Position(32, 48)
    marchands.append(marchand)

    scene3.ambiant = (224, 255, 192)
    scene3.tiles = tiles
    scene3.assets = assets
    scene3.plantes = plantes
    scene3.marchands = marchands
    scene3.warps = warps

    return scene3