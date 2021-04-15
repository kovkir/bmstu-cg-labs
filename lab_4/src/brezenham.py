'''
Алгоритм Брезенхема
'''

def reflect_dots_diag(dots, xc, yc):
    count_dots = len(dots)

    for i in range(count_dots):
        dots.append([dots[i][1] - yc + xc, dots[i][0] - xc + yc, dots[i][2]])

def reflect_dots_Oy(dots, xc):
    count_dots = len(dots)

    for i in range(count_dots):
        dots.append([-(dots[i][0] - xc) + xc, dots[i][1], dots[i][2]])

def reflect_dots_Ox(dots, yc):
    count_dots = len(dots)

    for i in range(count_dots):
        dots.append([dots[i][0], -(dots[i][1] - yc) + yc, dots[i][2]])
    
def bresenham_circle(xc, yc, r, color):
    x = 0
    y = r
    dots = [[x + xc, y + yc, color]]

    delta = 2 * (1 - r)

    while x < y:
        if delta <= 0:
            d = 2 * (delta + y) - 1
            x += 1

            if d >= 0 :
                y -= 1
                delta += 2 * (x - y + 1)
            else:
                delta += x + x + 1
        else:
            d = 2 * (delta - x) - 1
            y -= 1

            if d < 0:
                x += 1
                delta += 2 * (x - y + 1)
            else:
                delta += 1 - y - y

        dots.append([x + xc, y + yc, color])

    reflect_dots_diag(dots, xc, yc)
    reflect_dots_Oy(dots, xc)
    reflect_dots_Ox(dots, yc)

    return dots

def bresenham_ellipse(xc, yc, ra, rb, color):
    x = 0
    y = rb
    dots = [[x + xc, y + yc, color]]

    sqr_ra = ra * ra
    sqr_rb = rb * rb
    delta = sqr_rb - sqr_ra * (rb + rb + 1)

    while y >= 0:
        if delta <= 0:
            d = 2 * delta + sqr_ra * (y + y + 2)
            x += 1
            delta += sqr_rb * (x + x + 1)

            if d >= 0:
                y -= 1
                delta += sqr_ra * (- y - y + 1)
        else:
            d = 2 * delta + sqr_rb * (- x - x + 2)
            y -= 1
            delta += sqr_ra * (- y - y + 1)

            if d < 0:
                x += 1
                delta += sqr_rb * (x + x + 1)

        dots.append([x + xc, y + yc, color])

    reflect_dots_Oy(dots, xc)
    reflect_dots_Ox(dots, yc)

    return dots
