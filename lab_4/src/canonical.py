'''
Каноническое уравнение
'''

from math import sqrt
from pixels import draw_pixels

def canonical_сircle(xc, yc, r, color, canvas, draw):
    sqr_r = r ** 2

    border = round(xc + r / sqrt(2))

    for x in range(xc, border + 1):
        y = yc + sqrt(sqr_r - (x - xc) ** 2)
    
        if draw:
            draw_pixels(canvas, [x, y, color], xc, yc, circle = True)

def canonical_ellipse(xc, yc, ra, rb, color, canvas, draw):
    sqr_ra = ra * ra
    sqr_rb = rb * rb

    border_x = round(xc + ra / sqrt(1 + sqr_rb / sqr_ra))
    border_y = round(yc + rb / sqrt(1 + sqr_ra / sqr_rb))

    for x in range(xc, border_x + 1):
        y = yc + sqrt(sqr_ra * sqr_rb - (x - xc) ** 2 * sqr_rb) / ra

        if draw:
            draw_pixels(canvas, [x, y, color], xc, yc, circle = False)

    for y in range(border_y, yc - 1, -1):
        x = xc + sqrt(sqr_ra * sqr_rb - (y - yc) ** 2 * sqr_ra) / rb

        if draw:
            draw_pixels(canvas, [x, y, color], xc, yc, circle = False)
