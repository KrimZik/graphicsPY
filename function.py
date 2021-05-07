from graphics import *
def inbetween(pt1, pt2, pt3):
    between = False
    if (pt1.getX() <= pt2.getX() <= pt3.getX()) and (pt1.getY() <= pt2.getY() <= pt3.getY()):
        between = True
    return between
