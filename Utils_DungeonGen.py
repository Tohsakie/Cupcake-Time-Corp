import random
from enum import Enum

class CellState(Enum):
    UNKNOW = 0
    OPEN = 1
    CLOSE = 2

class Cell:
    def __init__(self):
        self.State = CellState.UNKNOW
        self.Primary = False
        self.Last = False
        self.IdRoom = 0
        self.IsInit = False
        self.X = None
        self.Y = None
        self.Left = None
        self.Down = None
        self.Right = None
        self.Up = None

class DungeonGen:
    def __init__(self):
        self.genMatrix = [[Cell(), Cell(), Cell(), Cell(), Cell()],
                          [Cell(), Cell(), Cell(), Cell(), Cell()],
                          [Cell(), Cell(), Cell(), Cell(), Cell()],
                          [Cell(), Cell(), Cell(), Cell(), Cell()],
                          [Cell(), Cell(), Cell(), Cell(), Cell()],
                          [Cell(), Cell(), Cell(), Cell(), Cell()]]
        self.PrimaryX = None
        self.PrimaryY = None
        self.NbRoom = 0

# Tete de la Generation
    def Gen(self):
        rnd = random.randint(0, 25)
        PrimaryX = int(rnd % 5)
        PrimaryY = int(rnd / 5)

        while self.NbRoom < 5 or self.NbRoom > 16:
            self.genMatrix = [[Cell(), Cell(), Cell(), Cell(), Cell()],
                          [Cell(), Cell(), Cell(), Cell(), Cell()],
                          [Cell(), Cell(), Cell(), Cell(), Cell()],
                          [Cell(), Cell(), Cell(), Cell(), Cell()],
                          [Cell(), Cell(), Cell(), Cell(), Cell()],
                          [Cell(), Cell(), Cell(), Cell(), Cell()]]
            self.NbRoom = 0
            cell = self.InitCell(PrimaryX, PrimaryY)
            for row in self.genMatrix:
                for column in row:
                    if column.IdRoom == self.NbRoom:
                        column.Last = True

# Initialistion des donnes de la cellule
    def InitCell(self, posx, posy):
        self.NbRoom += 1
        cell = Cell()
        cell.X = posx
        cell.Y = posy
        cell.State = CellState.OPEN

        if posx == 0:
            cell.Left = CellState.CLOSE
        else:
            if self.genMatrix[posx - 1][posy].State != CellState.UNKNOW:
                cell.Left = self.genMatrix[posx - 1][posy].State
                self.genMatrix[posx - 1][posy].Right = CellState.OPEN
            else:
                if random.randint(0, 1) == 0:
                    cell.Left = CellState.CLOSE
                else:
                    cell.Left = CellState.OPEN

        if posx >= 4:
            cell.Right = CellState.CLOSE
        else:
            if self.genMatrix[posx + 1][posy].State != CellState.UNKNOW:
                cell.Right = self.genMatrix[posx + 1][posy].State
                self.genMatrix[posx + 1][posy].Left = CellState.OPEN
            else:
                if random.randint(0, 1) == 0:
                    cell.Right = CellState.CLOSE
                else:
                    cell.Right = CellState.OPEN

        if posy == 0:
            cell.Up = CellState.CLOSE
        else:
            if self.genMatrix[posx][posy - 1].State != CellState.UNKNOW:
                cell.Up = self.genMatrix[posx][posy - 1].State
                self.genMatrix[posx][posy - 1].Down = CellState.OPEN
            else:
                if random.randint(0, 1) == 0:
                    cell.Up = CellState.CLOSE
                else:
                    cell.Up = CellState.OPEN

        if posy == 4:
            cell.Down = CellState.CLOSE
        else:
            if self.genMatrix[posx][posy + 1].State != CellState.UNKNOW:
                cell.Down = self.genMatrix[posx][posy + 1].State
                self.genMatrix[posx][posy + 1].Up = CellState.OPEN
            else:
                if random.randint(0, 1) == 0:
                    cell.Down = CellState.CLOSE
                else:
                    cell.Down = CellState.OPEN

        cell.IsInit = True
        self.genMatrix[posx][posy] = cell
        if self.NbRoom == 1:
            cell.Primary = True
        cell.IdRoom = self.NbRoom

        self.RecGen(cell)

        return cell

# Prepare les cellules adjacentes
    def RecGen(self, cell):
        if cell.Left == CellState.OPEN:
            if self.genMatrix[cell.X - 1][cell.Y].IsInit == False:
                self.InitCell(cell.X - 1, cell.Y)
        if cell.Down == CellState.OPEN:
            if self.genMatrix[cell.X][cell.Y + 1].IsInit == False:
                self.InitCell(cell.X, cell.Y + 1)
        if cell.Right == CellState.OPEN:
            if self.genMatrix[cell.X + 1][cell.Y].IsInit == False:
                self.InitCell(cell.X + 1, cell.Y)
        if cell.Up == CellState.OPEN:
            if self.genMatrix[cell.X][cell.Y - 1].IsInit == False:
                self.InitCell(cell.X, cell.Y - 1)