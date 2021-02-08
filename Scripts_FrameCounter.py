import Utils_Time as Time

class FrameCounter:
    def __init__(self):
        self.nbFrame = 0
        self.time = 0.0
    
    def update(self):
        self.time += Time.Time.deltaTime
        if (self.time >= 1):
            print('fps ' + str(self.nbFrame))
            self.nbFrame = 0
            self.time = 0.0
        self.nbFrame += 1
