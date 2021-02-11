import Utils_Scene as Scene

class Music:
    def __init__(self):
        self.interieur = None
        self.exterieur = None
        self.donjon = None
        self.scenes = []
        self.__lastState = None

    def update(self):
        for scene in self.scenes:
            if scene.state == True:
                if scene.type != self.__lastState:
                    if scene.type == Scene.TypeScene.INTERIEUR:
                        self.interieur.play()
                        self.exterieur.stop()
                        self.donjon.stop()
                        self.__lastState = Scene.TypeScene.INTERIEUR
                    elif scene.type == Scene.TypeScene.EXTERIEUR:
                        self.exterieur.play()
                        self.interieur.stop()
                        self.donjon.stop()
                        self.__lastState = Scene.TypeScene.EXTERIEUR
                    elif scene.type == Scene.TypeScene.DONJON:
                        self.donjon.play()
                        self.interieur.stop()
                        self.exterieur.stop()
                        self.__lastState = Scene.TypeScene.DONJON