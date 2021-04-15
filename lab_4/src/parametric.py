'''
Параметрическое уравнение
'''

from math import cos, sin, pi
from brezenham import reflect_dots_diag, reflect_dots_Ox, reflect_dots_Oy

def parameter_circle(xc, yc, r, color):
    dots = []
    step = 1 / r

    i = 0
    while i <= pi / 4 + step:
        x = xc + r * cos(i)
        y = yc + r * sin(i)

        dots.append([x, y, color])
        
        i += step

    reflect_dots_diag(dots, xc, yc)
    reflect_dots_Oy(dots, xc)
    reflect_dots_Ox(dots, yc)

    return dots

def parameter_ellipse(xc, yc, ra, rb, color):
    dots = []

    if ra > rb:
        step = 1 / ra
    else:
        step = 1 / rb

    i = 0
    while i <= pi / 2 + step:
        x = xc + ra * cos(i)
        y = yc + rb * sin(i)

        dots.append([x, y, color])

        i += step

    reflect_dots_Oy(dots, xc)
    reflect_dots_Ox(dots, yc)

    return dots
    