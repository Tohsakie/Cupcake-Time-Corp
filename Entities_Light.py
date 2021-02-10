import Utils_Position as Position

class Light:
    def __init__(self):
        self.Color = (0, 0, 0)
        self.position = Position.Position()
        self.Radius = 16
        self.MaxRadius = 17
        self.MinRadius = 15
        self.Increase = True
        self.Speed = 5