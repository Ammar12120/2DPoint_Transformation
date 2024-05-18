#!/usr/bin/env python3
from Transformation2D.point2d import Point2D
import numpy as np

# Addeition of two points test
def add(x):
    p2= Point2D(1,1) + x
    return p2

# Subtaction of two points test
def sub(x):
    p2 = x - Point2D(1,1)
    return p2

# check if less than of two points test
def less(x):
    p2 = Point2D(1,1)
    if x < p2:
        return True
    else: 
        return False
    
# check if equal of two points
def equal(x):
    p2 = Point2D()
    if x == p2:
        return True
    else: 
        return False



p1 = Point2D()
assert add(p1) == Point2D(1,1)
assert sub(p1) == Point2D(-1,-1)
assert less(p1) == True
assert equal(p1) == True