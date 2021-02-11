import Utils_Intersect as Intersect

class GetHeart:
    def __init__(self):
        self.scenes = []
        self.player = None
        self.keur = None

    def update(self):
        for scene in self.scenes:
            if scene.state == True:
                for heartItem in scene.heartsItems:
                    if Intersect.intersectXY(self.player.position, self.player.colBox, heartItem.position, heartItem.colBox):
                        if self.player.life != self.player.maxlife:
                            scene.heartsItems.remove(heartItem)
                            self.player.life += 1
                            self.keur.size.w += 8