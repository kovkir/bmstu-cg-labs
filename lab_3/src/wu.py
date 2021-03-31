'''
Алгоритм Ву
'''

from brezenham import get_color
from math import floor, fabs

def wu(one_point, two_point, color, step_count = False):

    x1 = one_point[0]
    y1 = one_point[1]
    x2 = two_point[0]
    y2 = two_point[1]

    dx = x2 - x1
    dy = y2 - y1

    if dx == 0 and dy == 0:
        return [[x1, x2, color]]

    m = 1
    step = 1
    steps = 0
    I = 255

    points = []

    if (abs(dy) >= abs(dx)):
        if (dy != 0):
            m = dx / dy
            
        m1 = m

        if (y1 > y2):
            m1 *= -1
            step *= -1

        bord = round(y2) - 1 if dy < dx else round(y2) + 1

        for y in range(round(y1), bord, step):
            d1 = x1 - floor(x1)
            d2 = 1 - d1

            if step_count == False:
                points.append([int(x1) + 1, y, get_color(color, round(fabs(d2) * I))])
                points.append([int(x1), y, get_color(color, round(fabs(d1) * I))])

            elif y < round(y2) and int(x1) != int(x1 + m):
                steps += 1

            x1 += m1
    else:
        if (dx != 0):
            m = dy / dx

        m1 = m

        if (x1 > x2):
            step *= -1
            m1 *= -1

        bord = round(x2) - 1 if dy > dx else round(x2) + 1

        for x in range(round(x1), bord, step):
            d1 = y1 - floor(y1)
            d2 = 1 - d1

            if step_count == False:
                points.append([x, int(y1) + 1, get_color(color, round(fabs(d2) * I))])
                points.append([x, int(y1), get_color(color, round(fabs(d1) * I))])

            elif x < round(x2) and int(y1) != int(y1 + m):
                steps += 1

            y1 += m1

    if step_count:
        return steps
    else:
        return points
