'''
Параметрическое уравнение
'''

from math import cos, sin, pi
from pixels import draw_pixels

def parameter_circle(xc, yc, r, color, canvas, draw):
    step = 1 / r

    i = 0
    while i <= pi / 4 + step:
        x = xc + round(r * cos(i))
        y = yc + round(r * sin(i))

        if draw:
            draw_pixels(canvas, [x, y, color], xc, yc, circle = True)
        
        i += step

def parameter_ellipse(xc, yc, ra, rb, color, canvas, draw):
    if ra > rb:
        step = 1 / ra
    else:
        step = 1 / rb

    i = 0
    while i <= pi / 2 + step:
        x = xc + round(ra * cos(i))
        y = yc + round(rb * sin(i))

        if draw:
            draw_pixels(canvas, [x, y, color], xc, yc, circle = False)

        i += step
