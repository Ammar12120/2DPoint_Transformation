from matplotlib import pyplot as plt


class Point2D:
    """Generic class to define 2D Points"""
    def __init__(self, x=0, y=0) -> None:
        """Point class constructor defult (0,0)"""
        self.x = x
        self.y = y    
        
    def __add__(self, other):
        assert isinstance (other, Point2D), "Cant add Point2D object to {} since it is not an object of Point2D".format(other)
        x = self.x + other.x
        y = self.y + other.y
        return Point2D(x,y)
  
    
    def __sub__(self, other):
        assert isinstance (other, Point2D), "Cant subtract Point2D object to {} since it is not an object of Point2D".format(other)
        x = self.x - other.x
        y = self.y - other.y
        return Point2D(x,y)
    
    def __lt__(self, other) -> bool:
        assert isinstance (other, Point2D), "Cant get the less than of Point2D object and {} since it is not an object of Point2D".format(other)
        if self.x < other.x or (self.x == other.x and self.y < other.y):
            return True
        else:
            return False
    
    def __eq__(self, other) -> bool:
        assert isinstance (other, Point2D), "Cant check if equal between Point2D object and {} since it is not an object of Point2D".format(other)
        return (self.x == other.x) and (self.y == other.y)
    
    def plot(self, color='b'):
        plt.plot(self.x, self.y, marker='o', color=color)

    def __str__(self) -> str:
        return ("Point: ({}, {})".format(self.x, self.y))