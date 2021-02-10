import Utils_Time as Time

class Ambiant:
    def __init__(self):
        self.scenes = []
        self.__time = 0.0
        self.__Right = False

    def update(self):
        self.__time += Time.Time.deltaTime
        if self.__time >= 2:
            for scene in self.scenes:
                if self.__Right == True:
                    scene.ambiant = (scene.ambiant[0] + 8, scene.ambiant[1] + 8, scene.ambiant[2] + 8)
                else:
                    scene.ambiant = (scene.ambiant[0] - 8, scene.ambiant[1] - 8, scene.ambiant[2] - 8)   
            if self.__Right == True:
                self.__Right = False
            else:
                self.__Right = True
            self.__time = 0.0