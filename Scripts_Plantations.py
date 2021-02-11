import Entities_Player as Player
import Entities_Plante as Plante
import Entities_Item as Item
import Utils_Position as Position
import Utils_Intersect as Intersect
import Utils_Scene as Scene

class Plantations:
    def __init__(self):
        self.player = None
        self.scenes = []
        self.texture = None
        self.items = None
        self.son = None
        self.__state = False
        self.__recup = False

    def update(self):
        if self.player.state == Player.PlayerState.SWITCH_ITEM:
            if self.__state == False:
                for i in range(0, len(self.items.itemGraines)):
                    if self.items.itemGraines[i].current == True:
                        if i == len(self.items.itemGraines) - 1:
                            self.items.itemGraines[0].texPos.y += 16
                            self.items.itemGraines[0].current = True
                        else:
                            self.items.itemGraines[i + 1].texPos.y += 16
                            self.items.itemGraines[i + 1].current = True
                        self.items.itemGraines[i].texPos.y -= 16
                        self.items.itemGraines[i].current = False
                        self.__state = True
                        break

        if self.player.state == Player.PlayerState.IDLE:
            self.__state = False

        if self.player.state == Player.PlayerState.PLANTATION:
            self.son.play()
            if self.__state == False:
                self.__recup = False
                for scene in self.scenes:
                    if scene.state == True:
                        for i in range(0, len(scene.plantes)):
                            if Intersect.intersectXY(self.player.position, self.player.colBox, scene.plantes[i].position, scene.plantes[i].colBox):
                                if scene.plantes[i].type == Plante.PlanteType.PASTEQUE:
                                    if scene.plantes[i].state == Plante.PlanteState.POUSSE:
                                        for item in self.items.itemGraines:
                                            if item.Item == Item.Items.GRN_PASTEQUE:
                                                item.quantity += 1
                                    if scene.plantes[i].state == Plante.PlanteState.FRUIT:
                                        for item in self.items.itemLegumes:
                                            if item.Item == Item.Items.PASTEQUE:
                                                item.quantity += 1
                                if scene.plantes[i].type == Plante.PlanteType.PIMENT:
                                    if scene.plantes[i].state == Plante.PlanteState.POUSSE:
                                        for item in self.items.itemGraines:
                                            if item.Item == Item.Items.GRN_PIMENT:
                                                item.quantity += 1
                                    if scene.plantes[i].state == Plante.PlanteState.FRUIT:
                                            for item in self.items.itemLegumes:
                                                if item.Item == Item.Items.PIMENT:
                                                    item.quantity += 1
                                scene.plantes.pop(i)
                                self.__recup = True
                                self.__state = True
                                break
                if self.__recup == False:
                    for item in self.items.itemGraines:
                        if item.current == True and item.quantity > 0:
                            self.__state = True
                            plante = Plante.Plante(self.texture)
                            plante.position = Position.Position(self.player.position.x, self.player.position.y)
                            if item.Item == Item.Items.GRN_PASTEQUE:
                                plante.texPos = Position.Position(96, 16)
                                plante.type = Plante.PlanteType.PASTEQUE
                            if item.Item == Item.Items.GRN_PIMENT:
                                plante.texPos = Position.Position(96, 16)
                                plante.type = Plante.PlanteType.PIMENT
                            item.quantity -= 1
                            for scene in self.scenes:
                                if scene.state == True:
                                    scene.plantes.append(plante)

        for scene in self.scenes:
            if scene.state == True:
                for plante in scene.plantes:
                    if plante.state == Plante.PlanteState.FRUIT:
                        if plante.type == Plante.PlanteType.PASTEQUE:
                            plante.texPos = Position.Position(112, 16)
                        if plante.type == Plante.PlanteType.PIMENT:
                            plante.texPos = Position.Position(144, 0)