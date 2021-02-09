import Entities_Tile as Tile
import Utils_Position as Position
import Utils_ColliderBox as ColliderBox
import Utils_Scene as Scene
import Entities_Warp as Warp

def createScene0(tileTexture, assetTexture):
    scene0 = Scene.Scene()

    tilemap = [
        2,  2,  2,  2,  2,  2,  2,  2,  1,  1,
        2,  2,  1,  2,  2,  1,  1,  1,  2,  1,
        2,  1,  1,  1,  2,  1,  2,  1,  1,  2,
        2, 16, 17, 17, 17, 17, 17, 17, 18,  2,
        2, 32, 33, 33, 33, 33, 33, 33, 34,  2,
        2, 32, 33, 33, 33, 33, 33, 33, 34,  1,
        1, 48, 49, 49, 49, 49, 49, 49, 50,  1,
        2,  1,  1,  2,  2,  2,  1,  1,  1,  1,
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
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0, 21,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0, 51, 52,  0,  0,
        0,  0,  0,  0,  0,  0, 67, 68,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    ]
    assetCollider = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 1, 1, 0, 0,
        0, 0, 0, 0, 0, 0, 1, 1, 0, 0,
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
            if assetmap[i] >= 128:
                asset.anime = True
            assets.append(asset)

    plantes = []

    warps = []
    warp = Warp.Warp()
    warp.warppos = Position.Position(0, -16)
    warp.colBox = ColliderBox.ColliderBox(0, 0, 160, 16)
    warp.tppos = Position.Position(0, 128)
    warp.sceneId = 1
    warps.append(warp)

    scene0.ambiant = (192, 128, 96)
    scene0.tiles = tiles
    scene0.assets = assets
    scene0.plantes = plantes
    scene0.warps = warps

    return scene0