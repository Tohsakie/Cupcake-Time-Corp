import Utils_Model as Model
from enum import Enum

class Items(Enum):
    GRN_PASTEQUE = 0
    GRN_PIMENT = 1
    PASTEQUE = 2
    PIMENT = 3

class Item(Model.Drawable):
    def __init__(self, texture):
        super().__init__(texture)
        self.Item = Items.GRN_PASTEQUE
        self.quantity = 0
        self.current = False