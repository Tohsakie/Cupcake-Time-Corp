import Entities_Tile as Tile
import Utils_Position as Position
import Utils_ColliderBox as ColliderBox
import Utils_Scene as Scene
import Entities_Warp as Warp
import Entities_Light as Light
import Entities_Bed as Bed

def createScene2(tileTexture, assetTexture):
    scene2 = Scene.Scene()

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
            if tilemap[i] >= 128:
                tile.anime = True
            tiles.append(tile)

    assetmap = [
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,108,  0,  0,  0,  0,  0,  0,  0,
        0,  0,124,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,109,110,  0,  0,
        0,  0, 78, 79,  0,  0,125,126,  0,  0,
        0,  0, 94, 95,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0, 24,  0,  0,  0,  0,  0,
    ]
    assetCollider = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
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
# Warp devant la maison
    warp = Warp.Warp()
    warp.warppos = Position.Position(64, 112)
    warp.colBox = ColliderBox.ColliderBox(4, 4, 8, 8)
    warp.tppos = Position.Position(0, 64)
    warp.sceneId = 1
    warps.append(warp)

    beds = []
    bed = Bed.Bed()
    bed.pos = Position.Position(48, 16)
    bed.colBox = ColliderBox.ColliderBox(0, 0, 16, 32)
    beds.append(bed)

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

    scene2.ambiant = (160, 192, 128)
    scene2.type = Scene.TypeScene.INTERIEUR
    scene2.tiles = tiles
    scene2.assets = assets
    scene2.plantes = plantes
    scene2.lights = lights
    scene2.warps = warps
    scene2.beds = beds

    return scene2