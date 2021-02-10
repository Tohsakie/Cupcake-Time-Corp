import Utils_Time as Time

class CloudsTranslation:
    def __init__(self):
        self.scenes = []

    def update(self):
        for scene in self.scenes:
            if scene.state == True:
                for cloud in scene.clouds:
                    if cloud.position.x + cloud.size.w <= 0 or cloud.position.y + cloud.size.h <= 0:
                        cloud.position.x = cloud.origin.x
                        cloud.position.y = cloud.origin.y
                    cloud.position.x -= cloud.speed * Time.Time.deltaTime
                    cloud.position.y -= cloud.speed * Time.Time.deltaTime