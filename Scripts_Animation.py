import Utils_Time as Time
import Entities_Tile as Tile

class Animation:
    def __init__(self):
        self.scenes = []
        self.__time = 0.0
        self.__Right = True

    def update(self):
        self.__time += Time.Time.deltaTime
        if self.__time >= 1:
            for scene in self.scenes:
                for asset in scene.assets:
                    if asset.anime == True:
                        if self.__Right == True:
                            asset.texPos.x += 16
                        else:
                            asset.texPos.x -= 16
            if self.__Right == True:
                self.__Right = False
            else:
                self.__Right = True
            self.__time = 0.0
                        