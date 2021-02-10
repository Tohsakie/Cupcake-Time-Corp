import Utils_Model as Model
import Utils_Position as Position

class Cloud(Model.Drawable):
    def __init__(self, texture):
        super().__init__(texture)
        self.origin = Position.Position()
        self.speed = 16
