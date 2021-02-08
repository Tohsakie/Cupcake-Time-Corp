import Entities_Tile as Tile
import Utils_Position as Position
import Utils_Scene as Scene

def createSceneHouse(tileTexture, assetTexture):
    scene2 = Scene.Scene()

    tilemap = [
        12,  14,  4,  14,  14,  14,  14,  4,  14,  13,
        44,  20,  20,  20,  20,  20,  20,  20,  20,  45,
        44,  20,  20,  20,  20,  20,  20,  20,  20,  45,
        44,  20,  20,  20,  20,  20,  20,  20,  20,  45,
        44,  20,  20,  20,  20,  20,  20,  20,  20,  45,
        44,  20,  20,  20,  20,  20,  20,  20,  20,  45,
        44,  20,  20,  20,  20,  20,  20,  20,  20,  45,
        44,  20,  20,  20,  20,  20,  20,  20,  20,  45,
        28,  15,  15,  15,  15,  15,  15,  15,  15,  29,
    ]
    tileCollider = [
        1, 1,  1, 1, 1, 1, 1, 1, 1, 1,
        1, 0,  0, 0, 0, 0, 0, 0, 0, 1,
        1, 0,  0, 0, 0, 0, 0, 0, 0, 1,
        1, 0,  0, 0, 0, 0, 0, 0, 0, 1,
        1, 0,  0, 0, 0, 0, 0, 0, 0, 1,
        1, 0,  0, 0, 0, 0, 0, 0, 0, 1,
        1, 0,  0, 0, 0, 0, 0, 0, 0, 1,
        1, 0,  0, 0, 0, 0, 0, 0, 0, 1,
        1, 1,  1, 0, 0, 0, 1, 1, 1, 1,
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
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  35,  0,  0,  0,  0,  0,
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

    scene2.tiles = tiles
    scene2.assets = assets
    scene2.plantes = plantes

    return scene2