import Utils_Position as Pos
import Utils_Size as Siz

def intersectXY(pos1, col1, pos2, col2):
    x1 = ((pos2.x + col2.x) <= (pos1.x + col1.w))
    x2 = ((pos2.x + col2.w) >= (pos1.x + col1.x))
    y1 = ((pos2.y + col2.y) <= (pos1.y + col1.h))
    y2 = ((pos2.y + col2.h) >= (pos1.y + col1.y))
    return (x1 and x2 and y1 and y2)