'''
Алгоритм средней точки
'''

from math import sqrt
from pixels import draw_pixels

def midpoint_circle(xc, yc, r, color, canvas, draw):
    x = r
    y = 0
    
    if draw:
        draw_pixels(canvas, [x + xc, y + yc, color], xc, yc, circle = True)

    delta = 1 - r

    while y <= x:
        if delta >= 0:
            x -= 1
            delta -= x + x

        y += 1
        delta += y + y + 1
        
        if draw:
            draw_pixels(canvas, [x + xc, y + yc, color], xc, yc, circle = True)

def midpoint_ellipse(xc, yc, ra, rb, color, canvas, draw):
    sqr_ra = ra * ra
    sqr_rb = rb * rb

    x = 0
    y = rb

    if draw:
        draw_pixels(canvas, [x + xc, y + yc, color], xc, yc, circle = False)

    border = round(ra / sqrt(1 + sqr_rb / sqr_ra))
    delta = sqr_rb - round(sqr_ra * (rb - 1 / 4))

    while x <= border:
        if delta > 0:
            y -= 1
            delta -= sqr_ra * y * 2

        x += 1
        delta += sqr_rb * (x + x + 1)
        
        if draw:
            draw_pixels(canvas, [x + xc, y + yc, color], xc, yc, circle = False)

    x = ra
    y = 0
    
    if draw:
        draw_pixels(canvas, [x + xc, y + yc, color], xc, yc, circle = False)

    border = round(rb / sqrt(1 + sqr_ra / sqr_rb))
    delta = sqr_ra - round(sqr_rb * (x - 1 / 4))

    while y <= border:
        if delta > 0:
            x -= 1
            delta -= 2 * sqr_rb * x

        y += 1
        delta += sqr_ra * (y + y + 1)
        
        if draw:
            draw_pixels(canvas, [x + xc, y + yc, color], xc, yc, circle = False)
