from point2d import Point2D


class Translate:
    """Generic class for the Translation of the 2D Point"""
    def __init__(self, dx:int, dy:int) -> None:
        self.dx = dx
        self.dy = dy
        
    def __add__(self, other):
        assert isinstance (other, Translate), "Cant add Translate object to {} since it is not an object of Translate".format(other)
        dx = self.dx + other.dx
        dy = self.dy + other.dy
        return Translate(dx,dy)
    
    def __sub__(self, other):
        assert isinstance (other, Translate), "Cant subtract Translate object to {} since it is not an object of Translate".format(other)
        dx = self.dx - other.dx
        dy = self.dy - other.dy
        return Translate(dx,dy)
    
    def __mul__(self, point:Point2D) -> Point2D:
        assert isinstance (point, Point2D), "Argument should be an object of Point2D"
        return Point2D(point.x + self.dx, point.y + self.dy)

    def __str__(self) -> str:
        return ("Translation to: ({}, {}) ".format(self.dx, self.dy))
        