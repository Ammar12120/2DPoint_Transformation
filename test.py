#!/usr/bin/env python3
from Transformation2D.rotate import Rotate
from Transformation2D.point2d import Point2D
# from Transformation2D.translate import *
# from Transformation2D.rotate import Rotate
# from Transformation2D.transformation import *
import numpy as np

# Addeition and Subtaction of two points test
def add_sub(x):
    p1 = x
    p2= Point2D(1,1) + p1
    p2 = p2 - Point2D(1,1)
    return p2

# # # Point Rotation test
# def rot(x):
#     r1 = Rotate(np.pi/8)
#     p2 = r1 * x
#     print(p2)



p1 = Point2D()
assert add_sub(p1) == p1
# assert rot(p1) == p1