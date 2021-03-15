import pos
import math
def calc_r(nox, noy, gox, goy):
    global rect
    dx = gox - nox
    dy = goy - noy
    rect = [dx, dy]
    return rect
def calc_angle(a, b):
    c = math.sqrt(a**2+b**2)
    angle = 90 - math.degrees(math.asin(rect[1] / c))
    return angle
def goto(x, y):
    g = pos.get_gyro()
    l = pos.get_loc()
    rect = calc_r(l[0], l[1], x, y)
    anglem = calc_angle(rect[0], rect[1])
    angle = g[2] - anglem
    if angle > 180:
        angle = -360 + angle
    return angle