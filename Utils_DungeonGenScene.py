import Utils_DungeonGen as DungeonGen
import Utils_Scene as Scene
import Entities_Tile as Tile
import Utils_Position as Position
import Entities_Warp as Warp
import Utils_ColliderBox as ColliderBox
import random
import Entities_Light as Light
import Entities_Ennemy as Ennemy
import Entities_HeartItem as HeartItem
import Utils_Size as Size

def createDungeonScenes(player, scenes, tileTexture, assetTexture, ennemyTexture, keurTexture, dungeonMatrix):
# Desactivation de toutes les maps
    for scene in scenes:
        if scene.state == True:
            scene.state = False

# Matrice de scene
    scenesMat = [[0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0]]
    sceneId = 6
    for x in range(0, 5):
        for y in range(0, 5):
            if dungeonMatrix[x][y].State == DungeonGen.CellState.OPEN:
                scenesMat[x][y] = sceneId
                sceneId += 1

# Ajouts des maps de la matrice dans le monde
    for x in range(0, 5):
        for y in range(0, 5):
            if dungeonMatrix[x][y].State == DungeonGen.CellState.OPEN:

            # Generation d'une map
                scene = Scene.Scene()

                lights = []

                # Gen TileMap
                tilemap = [3 for i in range(80)]
                assetmap = [0 for i in range(80)]
                for i in range(0, len(tilemap)):
                    if int(i / 10) == 0: # Mur haut
                        tilemap[i] = 14
                    if int(i / 10) == 7: # Mur Bas
                        tilemap[i] = 15
                    if int(i % 10) == 0: # Mur Gauche
                        tilemap[i] = 44
                    if int(i % 10) == 9: # Mur Droit
                        tilemap[i] = 45
                    if i == 0:           # Coin Haut-Gauche
                        tilemap[i] = 12
                    if i == 9:           # Coin Haut-Gauche
                        tilemap[i] = 13
                    if i == 70:          # Coin Haut-Gauche
                        tilemap[i] = 28
                    if i == 79:          # Coin Haut-Gauche
                        tilemap[i] = 29
                if dungeonMatrix[x][y].Left == DungeonGen.CellState.OPEN:
                    tilemap[30] = 3
                    light = Light.Light()
                    light.Color = (255, 224, 192)
                    light.position = Position.Position(8, 40)
                    light.Radius = 24
                    light.MaxRadius = 26
                    light.MinRadius = 22
                    light.Speed = 4
                    lights.append(light)
                    tilemap[40] = 3
                    light = Light.Light()
                    light.Color = (255, 224, 192)
                    light.position = Position.Position(8, 88)
                    light.Radius = 24
                    light.MaxRadius = 26
                    light.MinRadius = 22
                    light.Speed = 4
                    lights.append(light)
                if dungeonMatrix[x][y].Down == DungeonGen.CellState.OPEN:
                    tilemap[75] = 3
                    light = Light.Light()
                    light.Color = (255, 224, 192)
                    light.position = Position.Position(56, 120)
                    light.Radius = 24
                    light.MaxRadius = 26
                    light.MinRadius = 22
                    light.Speed = 4
                    lights.append(light)
                    tilemap[74] = 3
                    light = Light.Light()
                    light.Color = (255, 224, 192)
                    light.position = Position.Position(104, 120)
                    light.Radius = 24
                    light.MaxRadius = 26
                    light.MinRadius = 22
                    light.Speed = 4
                    lights.append(light)
                if dungeonMatrix[x][y].Right == DungeonGen.CellState.OPEN:
                    tilemap[39] = 3
                    light = Light.Light()
                    light.Color = (255, 224, 192)
                    light.position = Position.Position(152, 40)
                    light.Radius = 24
                    light.MaxRadius = 26
                    light.MinRadius = 22
                    light.Speed = 4
                    lights.append(light)
                    tilemap[49] = 3
                    light = Light.Light()
                    light.Color = (255, 224, 192)
                    light.position = Position.Position(152, 88)
                    light.Radius = 24
                    light.MaxRadius = 26
                    light.MinRadius = 22
                    light.Speed = 4
                    lights.append(light)
                if dungeonMatrix[x][y].Up == DungeonGen.CellState.OPEN:
                    tilemap[4] = 3
                    light = Light.Light()
                    light.Color = (255, 224, 192)
                    light.position = Position.Position(56, 8)
                    light.Radius = 24
                    light.MaxRadius = 26
                    light.MinRadius = 22
                    light.Speed = 4
                    lights.append(light)
                    tilemap[5] = 3
                    light = Light.Light()
                    light.Color = (255, 224, 192)
                    light.position = Position.Position(104, 8)
                    light.Radius = 24
                    light.MaxRadius = 26
                    light.MinRadius = 22
                    light.Speed = 4
                    lights.append(light)

                if dungeonMatrix[x][y].Last == True:
                    tilemap[34] = 84

                # Gen TileCollider
                tileCollider = [0 for i in range(80)]
                for i in range(0, len(tileCollider)):
                    if int(i / 10) == 0: # Mur haut
                        tileCollider[i] = 1
                    if int(i / 10) == 7: # Mur Bas
                        tileCollider[i] = 1
                    if int(i % 10) == 0: # Mur Gauche
                        tileCollider[i] = 1
                    if int(i % 10) == 9: # Mur Droit
                        tileCollider[i] = 1
                if dungeonMatrix[x][y].Left == DungeonGen.CellState.OPEN:
                    tileCollider[30] = 0
                    tileCollider[40] = 0
                if dungeonMatrix[x][y].Down == DungeonGen.CellState.OPEN:
                    tileCollider[75] = 0
                    tileCollider[74] = 0
                if dungeonMatrix[x][y].Right == DungeonGen.CellState.OPEN:
                    tileCollider[39] = 0
                    tileCollider[49] = 0
                if dungeonMatrix[x][y].Up == DungeonGen.CellState.OPEN:
                    tileCollider[4] = 0
                    tileCollider[5] = 0

                # Gen assetMap
                # Decoration
                heartItems = []

                if random.randint(0, 2) == 0:
                    assetmap[11] = 28
                    assetmap[12] = 28
                    assetmap[21] = 28
                elif random.randint(0, 8) == 0:
                    heartItem = HeartItem.HeartItem(keurTexture)
                    heartItem.position = Position.Position(16, 16)
                    heartItem.size = Size.Size(8, 8)
                    heartItems.append(heartItem)
                if random.randint(0, 2) == 0:
                    assetmap[17] = 28
                    assetmap[18] = 28
                    assetmap[28] = 28
                elif random.randint(0, 8) == 0:
                    heartItem = HeartItem.HeartItem(keurTexture)
                    heartItem.position = Position.Position(136, 16)
                    heartItem.size = Size.Size(8, 8)
                    heartItems.append(heartItem)
                if random.randint(0, 2) == 0:
                    assetmap[68] = 28
                    assetmap[67] = 28
                    assetmap[58] = 28
                elif random.randint(0, 8) == 0:
                    heartItem = HeartItem.HeartItem(keurTexture)
                    heartItem.position = Position.Position(136, 104)
                    heartItem.size = Size.Size(8, 8)
                    heartItems.append(heartItem)
                if random.randint(0, 2) == 0:
                    assetmap[61] = 28
                    assetmap[62] = 28
                    assetmap[51] = 28
                elif random.randint(0, 8) == 0:
                    heartItem = HeartItem.HeartItem(keurTexture)
                    heartItem.position = Position.Position(16, 104)
                    heartItem.size = Size.Size(8, 8)
                    heartItems.append(heartItem)
                # Asset portes
                if dungeonMatrix[x][y].Left == DungeonGen.CellState.OPEN:
                    assetmap[30] = 18
                    assetmap[20] = 60
                    assetmap[40] = 34
                    assetmap[50] = 60
                if dungeonMatrix[x][y].Down == DungeonGen.CellState.OPEN:
                    assetmap[73] = 61
                    assetmap[74] = 32
                    assetmap[75] = 33
                    assetmap[76] = 61
                if dungeonMatrix[x][y].Right == DungeonGen.CellState.OPEN:
                    assetmap[29] = 45
                    assetmap[39] = 19
                    assetmap[49] = 35
                    assetmap[59] = 45
                if dungeonMatrix[x][y].Up == DungeonGen.CellState.OPEN:
                    assetmap[3] = 44
                    assetmap[4] = 16
                    assetmap[5] = 17
                    assetmap[6] = 44

                # Assign
                tiles = []
                for i in range(0, len(tilemap)):
                    if tilemap[i] != 0:
                        tile = Tile.Tile(tileTexture)
                        tile.position = Position.Position(i % 10 * 16, int(i / 10) * 16)
                        tile.texPos = Position.Position(tilemap[i] % 16 * 16, int(tilemap[i] / 16) * 16)
                        tiles.append(tile)
                        if tileCollider[i] == 1:
                            tile.collider = True
                assets = []
                for i in range(0, len(assetmap)):
                    if assetmap[i] != 0:
                        asset = Tile.Tile(assetTexture)
                        asset.position = Position.Position(i % 10 * 16, int(i / 10) * 16)
                        asset.texPos = Position.Position(assetmap[i] % 16 * 16, int(assetmap[i] / 16) * 16)
                        if assetmap[i] == 28:
                            asset.collider = True
                        assets.append(asset)
                scene.ambiant = (192, 160, 128)
                scene.IsDungeon = True
                scene.tiles = tiles
                scene.assets = assets
                scene.lights = lights
                if dungeonMatrix[x][y].Primary == True:
                    scene.state = True

                # Warps
                warps = []
                if dungeonMatrix[x][y].Left == DungeonGen.CellState.OPEN:
                    warp = Warp.Warp()
                    warp.warppos = Position.Position(0, 48)
                    warp.colBox = ColliderBox.ColliderBox(4, 4, 8, 24)
                    warp.tppos = Position.Position(128, 48)
                    warp.sceneId = scenesMat[x - 1][y]
                    warps.append(warp)
                if dungeonMatrix[x][y].Down == DungeonGen.CellState.OPEN:
                    warp = Warp.Warp()
                    warp.warppos = Position.Position(64, 112)
                    warp.colBox = ColliderBox.ColliderBox(4, 4, 24, 8)
                    warp.tppos = Position.Position(48, 16)
                    warp.sceneId = scenesMat[x][y + 1]
                    warps.append(warp)
                if dungeonMatrix[x][y].Right == DungeonGen.CellState.OPEN:
                    warp = Warp.Warp()
                    warp.warppos = Position.Position(144, 48)
                    warp.colBox = ColliderBox.ColliderBox(4, 4, 8, 24)
                    warp.tppos = Position.Position(16, 48)
                    warp.sceneId = scenesMat[x + 1][y]
                    warps.append(warp)
                if dungeonMatrix[x][y].Up == DungeonGen.CellState.OPEN:
                    warp = Warp.Warp()
                    warp.warppos = Position.Position(64, 0)
                    warp.colBox = ColliderBox.ColliderBox(4, 4, 24, 8)
                    warp.tppos = Position.Position(48, 96)
                    warp.sceneId = scenesMat[x][y - 1]
                    warps.append(warp)
                if dungeonMatrix[x][y].Last == True:
                    warp = Warp.Warp()
                    warp.warppos = Position.Position(64, 48)
                    warp.colBox = ColliderBox.ColliderBox(4, 4, 8, 8)
                    warp.tppos = Position.Position(32, 32)
                    warp.sceneId = 2
                    warp.purgeDungeon = True
                    warps.append(warp)
                scene.warps = warps

                # Gen Mob
                monsters = []

                if dungeonMatrix[x][y].Last == False and dungeonMatrix[x][y].Primary == False:
                    for i in range(0, random.randint(0, player.nbJour)):
                        monster = Ennemy.Ennemy(ennemyTexture)
                        monster.position = Position.Position(64, 64)
                        monster.colBox = ColliderBox.ColliderBox(0, 0, 16, 16)
                        monsters.append(monster)

                scene.monsters = monsters
                scene.heartsItems = heartItems
            # Ajout de la map
                scenes.append(scene)