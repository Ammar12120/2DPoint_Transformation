from point2d import Point2D
from translate import Translate
from rotate import Rotate

class Transformation:
    """Generic class for the Transformation of the 2D Point"""
    def __init__(self, translation:Translate, rotation:Rotate) -> None:
        self.translation = translation
        self.rotation = rotation

    def __mul__(self, point:Point2D) -> Point2D:
        assert isinstance (point, Point2D), "Argument should be an object of Point2D"
        translation = self.translation * point
        roation_translation = self.rotation * translation
        return roation_translation

    def __str__(self) -> str:
        return ("{} and {}".format(self.translation, self.rotation)) 