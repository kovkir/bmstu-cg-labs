'''
Каноническое уравнение
'''

from math import sqrt
from brezenham import reflect_dots_diag, reflect_dots_Ox, reflect_dots_Oy

def canonical_сircle(xc, yc, r, color):
    dots = []
    sqr_r = r ** 2

    for x in range(xc, round(xc + r / sqrt(2)) + 1):
        y = yc + sqrt(sqr_r - (x - xc) ** 2)
    
        dots.append([x, y, color])

    reflect_dots_diag(dots, xc, yc)
    reflect_dots_Oy(dots, xc)
    reflect_dots_Ox(dots, yc)

    return dots

def canonical_ellipse(xc, yc, ra, rb, color):
    dots = []

    sqr_ra = ra * ra
    sqr_rb = rb * rb

    border_x = round(xc + ra / sqrt(1 + sqr_rb / sqr_ra))
    border_y = round(yc + rb / sqrt(1 + sqr_ra / sqr_rb))

    for x in range(xc, border_x + 1):
        y = yc + sqrt(sqr_ra * sqr_rb - (x - xc) ** 2 * sqr_rb) / ra

        dots.append([x, y, color])

    for y in range(border_y, yc - 1, -1):
        x = xc + sqrt(sqr_ra * sqr_rb - (y - yc) ** 2 * sqr_ra) / rb

        dots.append([x, y, color])

    reflect_dots_Ox(dots, yc)
    reflect_dots_Oy(dots, xc)

    return dots
