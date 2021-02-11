import Utils_Intersect as Intersect
import Entities_Marchand as Marchand
import Entities_Player as Player
import Entities_Tile as Tile
import Entities_Item as Item
import Utils_Position as Position
import Utils_Size as Size
import Entities_Inventory as Inventory
import pygame

class ScriptMarchand:
    def __init__(self):
        self.scenes = []
        self.items = None
        self.pognon = None
        self.joueur = None
        self.uiTexture = None
        self.assetTexture = None
        self.__ActifUI = 0

    def update(self):
        for scene in self.scenes:
            if scene.state == True:
                for marchand in scene.marchands:
                    if Intersect.intersectXY(self.joueur.position, self.joueur.colBox, marchand.pos, marchand.colBox):

                    # Ouverture du menu de vente
                        if self.joueur.state == Player.PlayerState.PLANTATION:
                            if marchand.etat == Marchand.EtatMarchand.INACTIF:
                                self.joueur.state = Player.PlayerState.DISCUTION
                                marchand.etat = Marchand.EtatMarchand.ACTIF
                                ui = Item.Item(self.uiTexture)
                                ui.position = Position.Position(32, 32)
                                ui.size = Size.Size(96, 64)
                                ui.quantity = 0
                                scene.ui.append(ui)
                                produit0 = Item.Item(self.assetTexture)
                                produit0.position = Position.Position(48, 48)
                                produit0.texPos = Position.Position(224, 16)
                                produit0.quantity = 5
                                __ActifUI = 0
                                scene.ui.append(produit0)
                                produit1 = Item.Item(self.assetTexture)
                                produit1.position = Position.Position(48, 64)
                                produit1.texPos = Position.Position(240, 0)
                                produit1.quantity = 1
                                scene.ui.append(produit1)

                    # Fermeture du menu de vente
                        elif self.joueur.state == Player.PlayerState.SWITCH_ITEM:
                            if marchand.etat == Marchand.EtatMarchand.ACTIF:
                                marchand.etat = Marchand.EtatMarchand.INACTIF
                                scene.ui.clear()

                    # Action du menu de vente
                        if marchand.etat == Marchand.EtatMarchand.ACTIF:

                        # Deplacement bas dans le menu
                            if marchand.inventaireMarchand == Marchand.InventaireMarchand.INVENTAIRE_BAS:
                                self.__ActifUI = 1
                                scene.ui[2].texPos.y = 16
                                scene.ui[1].texPos.y = 0
                                marchand.inventaireMarchand = Marchand.InventaireMarchand.INVENTAIRE_RIEN

                        # Deplacement haut dans le menu
                            if marchand.inventaireMarchand == Marchand.InventaireMarchand.INVENTAIRE_HAUT:
                                self.__ActifUI = 0
                                scene.ui[2].texPos.y = 0
                                scene.ui[1].texPos.y = 16
                                marchand.inventaireMarchand = Marchand.InventaireMarchand.INVENTAIRE_RIEN
                        
                        # Achat dans le menu
                            if marchand.inventaireMarchand == Marchand.InventaireMarchand.INVENTAIRE_ACHAT:
                                if self.__ActifUI == 0: # pasteque
                                    for item in self.items.itemGraines:
                                        if item.Item == Item.Items.GRN_PASTEQUE:
                                            if self.pognon.pognon >= 5:
                                                item.quantity += 1
                                                self.pognon.pognon -= 5
                                if self.__ActifUI == 1: # piment
                                    for item in self.items.itemGraines:
                                        if item.Item == Item.Items.GRN_PIMENT:
                                            if self.pognon.pognon >= 1:
                                                item.quantity += 1
                                                self.pognon.pognon -= 1
                                marchand.inventaireMarchand = Marchand.InventaireMarchand.INVENTAIRE_RIEN