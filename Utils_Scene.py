from enum import Enum

class TypeScene(Enum):
    EXTERIEUR = 0
    DONJON = 1
    INTERIEUR = 2

class Scene:
    def __init__(self):
        self.state = False
        self.IsDungeon = False
        self.type = TypeScene.DONJON
        self.ambiant = (0, 0, 0)
        self.tiles = []
        self.assets = []
        self.plantes = []
        self.warps = []
        self.lights = []
        self.marchands = []
        self.ui = []
        self.clouds = []
        self.beds = []
        self.monsters = []
        self.heartsItems = []
        self.attackPiment = []