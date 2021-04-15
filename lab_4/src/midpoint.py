'''
Алгоритм средней точки
'''

from math import sqrt
from brezenham import reflect_dots_diag, reflect_dots_Ox, reflect_dots_Oy

def midpoint_circle(xc, yc, r, color):
    x = r
    y = 0
    dots = [[x + xc, y + yc, color]]

    delta = 1 - r

    while y < x:
        y += 1

        if delta >= 0:
            x -= 1
            delta -= x + x

        delta += y + y + 1
        dots.append([x + xc, y + yc, color])

    reflect_dots_diag(dots, xc, yc)
    reflect_dots_Oy(dots, xc)
    reflect_dots_Ox(dots, yc)

    return dots

def midpoint_ellipse(xc, yc, ra, rb, color):
    sqr_ra = ra * ra
    sqr_rb = rb * rb

    border = round(ra / sqrt(1 + sqr_rb / sqr_ra))

    x = 0
    y = rb
    dots = [[x + xc, y + yc, color]]

    delta = sqr_rb - round(sqr_ra * (rb - 1 / 4))
    while x < border:
        if delta > 0:
            y -= 1
            delta -= sqr_ra * y * 2

        x += 1
        delta += sqr_rb * (x + x + 1)
        dots.append([x + xc, y + yc, color])

    border = round(rb / sqrt(1 + sqr_ra / sqr_rb))

    x = ra
    y = 0
    dots.append([x + xc, y + yc, color])

    delta = sqr_ra - round(sqr_rb * (x - 1 / 4))
    while y < border:
        if delta > 0:
            x -= 1
            delta -= 2 * sqr_rb * x

        y += 1
        delta += sqr_ra * (y + y + 1)
        dots.append([x + xc, y + yc, color])

    reflect_dots_Ox(dots, yc)
    reflect_dots_Oy(dots, xc)

    return dots
    