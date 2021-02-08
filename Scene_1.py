import Entities_Tile as Tile
import Utils_Position as Position
import Utils_Size as Size
import Utils_Scene as Scene
import Entities_Warp as Warp

def createScene1(tileTexture, assetTexture):
    scene1 = Scene.Scene()

    tilemap = [
        2,  2,  2,  2,  2,  2,  2,  2,  1,  1,
        2,  2,  4,  4,  4,  4,  4,  1,  2,  1,
        2,  2,  3,  3,  3,  3,  3,  2,  1,  2,
        2,  2,  3,  3,  2,  3,  3,  2,  1,  2,
        2,  2,  2,  2,  2,  2,  2,  2,  2,  2,
        2,  2,  2,  2,  2,  2,  1,  1,  2,  2,
        2,  2,  1,  2,  2,  1,  1,  2,  2,  1,
        1,  2,  2,  2,  2,  2,  1,  2,  1,  1,
        2,  1,  1,  2,  2,  2,  1,  1,  1,  1,
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
            tiles.append(tile)

    assetmap = [
        0,  0,   0,   0,  0,   0,   0,  0,  0,  0,
        0,  0,   0,   0,  0,   0,   0,  0,  0,  0,
        0,  0,  96,  97,  0,  96,  97,  0,  0,  0,
        0,  0, 112, 113, 26, 112, 113,  0,  0,  0,
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
    warp = Warp.Warp()
    warp.warppos = Position.Position(0, 144)
    warp.size = Size.Size(160, 16)
    warp.tppos = Position.Position(0, 0)
    warp.sceneId = 0
    warps.append(warp)

    scene1.tiles = tiles
    scene1.assets = assets
    scene1.plantes = plantes
    scene1.warps = warps

    return scene1