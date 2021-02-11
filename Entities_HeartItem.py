import Utils_Model as Model

class HeartItem(Model.Drawable):
    def __init__(self, texture):
        super().__init__(texture)
        self.heart = True