import Utils_DungeonGen as DungeonGen
import Utils_Scene as Scene
import Entities_Tile as Tile
import Utils_Position as Position
import Entities_Warp as Warp
import Utils_ColliderBox as ColliderBox

def createDungeonScenes(scenes, tileTexture, assetTexture, dungeonMatrix):
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
    sceneId = 5
    for x in range(0, 5):
        for y in range(0, 5):
            if dungeonMatrix[x][y].State == DungeonGen.CellState.OPEN:
                scenesMat[x][y] = sceneId
                sceneId += 1

    for row in scenesMat:
        for val in row:
            if val > 0:
                print('x ', end='')
            else:
                print('O ', end='')
        print()

# Ajouts des maps de la matrice dans le monde
    for x in range(0, 5):
        for y in range(0, 5):
            if dungeonMatrix[x][y].State == DungeonGen.CellState.OPEN:

            # Generation d'une map
                scene = Scene.Scene()

                # Gen TileMap
                tilemap = [3 for i in range(80)]
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
                    tilemap[40] = 3
                if dungeonMatrix[x][y].Down == DungeonGen.CellState.OPEN:
                    tilemap[75] = 3
                    tilemap[74] = 3
                if dungeonMatrix[x][y].Right == DungeonGen.CellState.OPEN:
                    tilemap[39] = 3
                    tilemap[49] = 3
                if dungeonMatrix[x][y].Up == DungeonGen.CellState.OPEN:
                    tilemap[4] = 3
                    tilemap[5] = 3

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
                scene.ambiant = (255, 255, 255)
                scene.IsDungeon = True
                scene.tiles = tiles
                if dungeonMatrix[x][y].Primary == True:
                    scene.state = True

                # Warps
                warps = []
                if dungeonMatrix[x][y].Left == DungeonGen.CellState.OPEN:
                    warp = Warp.Warp()
                    warp.warppos = Position.Position(0, 48)
                    warp.colBox = ColliderBox.ColliderBox(0, 0, 16, 32)
                    warp.tppos = Position.Position(128, 48)
                    warp.sceneId = scenesMat[x - 1][y]
                    warps.append(warp)
                if dungeonMatrix[x][y].Down == DungeonGen.CellState.OPEN:
                    warp = Warp.Warp()
                    warp.warppos = Position.Position(64, 112)
                    warp.colBox = ColliderBox.ColliderBox(0, 0, 32, 16)
                    warp.tppos = Position.Position(48, 96)
                    warp.sceneId = scenesMat[x][y + 1]
                    warps.append(warp)
                if dungeonMatrix[x][y].Right == DungeonGen.CellState.OPEN:
                    warp = Warp.Warp()
                    warp.warppos = Position.Position(144, 48)
                    warp.colBox = ColliderBox.ColliderBox(0, 0, 16, 32)
                    warp.tppos = Position.Position(16, 48)
                    warp.sceneId = scenesMat[x + 1][y]
                    warps.append(warp)
                if dungeonMatrix[x][y].Up == DungeonGen.CellState.OPEN:
                    warp = Warp.Warp()
                    warp.warppos = Position.Position(64, 0)
                    warp.colBox = ColliderBox.ColliderBox(0, 0, 32, 16)
                    warp.tppos = Position.Position(48, 96)
                    warp.sceneId = scenesMat[x][y - 1]
                    warps.append(warp)
                scene.warps = warps

            # Ajout de la map
                scenes.append(scene)