import Entities_Tile as Tile
import Utils_Position as Position
import Utils_ColliderBox as ColliderBox
import Utils_Scene as Scene
import Entities_Warp as Warp
import Entities_Light as Light
import Entities_Cloud as Cloud
import Utils_Size as Size

def createScene5(reglesTexture):
    scene5 = Scene.Scene()

    tilemap = [
           0,   1,   2,   3,   4,   5,   6,   7,   8,   9,
          16,  17,  18,  19,  20,  21,  22,  23,  24,  25,
          32,  33,  34,  35,  36,  37,  38,  39,  40,  41,
          48,  49,  50,  51,  52,  53,  54,  55,  56,  57,
          128,  65,  66,  67,  68,  69,  70,  71,  72,  73,
          80,  81,  82,  83,  84,  85,  86,  87,  88,  89,
          96,  97,  98,  99, 100, 101, 102, 103, 104, 105,
         112, 113, 114, 115, 116, 117, 118, 119, 120, 121,
    ]
    
    tileCollider = [
        1, 1,  1, 1, 1, 1, 1, 1, 1, 1,
        1, 0,  0, 0, 0, 0, 0, 0, 0, 1,
        1, 0,  0, 0, 0, 0, 0, 0, 0, 1,
        1, 0,  0, 0, 0, 0, 0, 0, 0, 1,
        0, 0,  0, 0, 0, 0, 0, 0, 0, 1,
        1, 0,  0, 0, 0, 0, 0, 0, 0, 1,
        1, 0,  0, 0, 0, 0, 0, 0, 0, 1,
        1, 1,  1, 1, 1, 1, 1, 1, 1, 1,
    ]
    tiles = []
    for i in range(0, len(tilemap)):
        if tilemap[i] >= 0:
            tile = Tile.Tile(reglesTexture)
            tile.position = Position.Position(i % 10 * 16, int(i / 10) * 16)
            tile.texPos = Position.Position(tilemap[i] % 16 * 16, int(tilemap[i] / 16) * 16)
            if tileCollider[i] == 1:
                tile.collider = True
            if tilemap[i] >= 128:
                tile.anime = True
            tiles.append(tile)

    plantes = []
    warps = []
    #lights = []
    #light = Light.Light()
    #light.Color = (255, 128, 32)
    #light.Radius = 60
    #light.MaxRadius = 68
    #light.MinRadius = 60
    #light.Speed = 16
    #lights.append(light)

    # Warp vers Devant maison
    warp = Warp.Warp()
    warp.warppos = Position.Position(0,64)
    warp.colBox = ColliderBox.ColliderBox(4, 4, 8, 8)
    warp.tppos = Position.Position(128, 0)
    warp.sceneId = 1
    warps.append(warp)  

    scene5.ambiant = (255, 255, 255)
    scene5.type = Scene.TypeScene.EXTERIEUR
    scene5.tiles = tiles
    scene5.plantes = plantes
    scene5.warps = warps
    #scene5.lights = lights

    return scene5