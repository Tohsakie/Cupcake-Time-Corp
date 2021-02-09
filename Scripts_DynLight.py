import Utils_Time as Time

class DynLight:
    def __init__(self):
        self.scenes = []

    def update(self):
        for scene in self.scenes:
            if scene.state == True:
                for light in scene.lights:
                    if light.Increase == True:
                        if light.Radius >= light.MaxRadius:
                            light.Increase = False
                        else:
                            light.Radius += light.Speed * Time.Time.deltaTime
                    else:
                        if light.Radius <= light.MinRadius:
                            light.Increase = True
                        else:
                            light.Radius -= light.Speed * Time.Time.deltaTime