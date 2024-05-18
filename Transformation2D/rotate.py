import numpy as np
from point2d import Point2D
class Rotate:
    """Generic class for the Rotation of the 2D Point"""
    def __init__(self, theta:float) -> None:
        self.theta = theta  
        
    def __add__(self, other):
        assert isinstance (other, Rotate), "Cant add Rotate object to {} since it is not an object of Rotate".format(other)
        theta = self.theta + other.theta
        return Rotate(theta)
    
    def __sub__(self, other):
        assert isinstance (other, Rotate), "Cant subtract Rotate object to {} since it is not an object of Rotate".format(other)
        theta = self.theta - other.theta
        return Rotate(theta)
    
    def __mul__(self, point:Point2D) -> Point2D:
        assert isinstance (point, Point2D), "Argument should be an object of Point2D"
        cos_theta = np.cos(self.theta)
        sin_theta = np.sin(self.theta)
        x = point.x * cos_theta - point.y * sin_theta
        y = point.x * sin_theta + point.y * cos_theta
        return Point2D(x, y)
    
    def __str__(self) -> str:
        return ("Roation of {} degrees ".format(np.rad2deg(self.theta)))
