import Utils_Model as Model

class Tile(Model.Drawable):
    def __init__(self, texture):
        super().__init__(texture)
        self.collider = False
        self.anime = False