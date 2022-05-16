import math

def RotateMatrix(before_x,before_y,d):
    d = math.radians(d)
    new_x = before_x*math.cos(d)-before_y*math.sin(d)
    new_y = before_x*math.sin(d)+before_y*math.cos(d)
    return new_x,new_y