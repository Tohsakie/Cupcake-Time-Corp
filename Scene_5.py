import Entities_Tile as Tile
import Utils_Position as Position
import Utils_ColliderBox as ColliderBox
import Utils_Scene as Scene
import Entities_Warp as Warp
import Entities_Light as Light
import Entities_Cloud as Cloud
import Utils_Size as Size

def createScene5(window):
    scene5 = Scene.Scene()
    scene5.ambiant = (225, 255, 255)
    print("aha")
    img = window.font.render("Sweet Nightmare", False, (255, 0, 0))
    window.screen.blit(img, (50, 50))
    print("ohoho")

    return scene5