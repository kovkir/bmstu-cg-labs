'''
Алгоритмы Брезенхема
'''

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def bresenham_int(beg_point, end_point, color):
    dx = end_point[0] - beg_point[0]
    dy = end_point[1] - beg_point[1]

    if dx == 0 and dy == 0:
        return [[beg_point[0], beg_point[1], color]]

    x_sign = sign(dx)
    y_sign = sign(dy)

    dx = abs(dx)
    dy = abs(dy)

    if dy > dx:
        dx, dy = dy, dx
        exchange = 1
    else:
        exchange = 0

    two_dy = 2 * dy
    two_dx = 2 * dx

    e = two_dy - dx

    x = beg_point[0]
    y = beg_point[1]
    points = []

    i = 0
    while i <= dx:
        points.append([x, y, color])

        if e >= 0:
            if exchange == 1:
                x += x_sign
            else:
                y += y_sign

            e -= two_dx

        if exchange == 1:
            y += y_sign
        else:
            x += x_sign
        
        e += two_dy
        i += 1

    return points
