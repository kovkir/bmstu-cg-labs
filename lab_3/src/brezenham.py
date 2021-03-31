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

def get_color(color, light):
    return color + (light , light, light)

def bresenham_float(beg_point, end_point, color, step_count = False):

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

    e = dy / dx - 0.5

    x = beg_point[0]
    y = beg_point[1]
    points = []

    x_buf = x
    y_buf = y
    steps = 0

    i = 0
    while i <= dx:
        if step_count == False:
            points.append([x, y, color])

        if e >= 0:
            if exchange:
                x += x_sign
            else:
                y += y_sign

            e -= 1

        if exchange:
            y += y_sign
        else:
            x += x_sign
        
        e += dy / dx
        i += 1

        if step_count:
            if x_buf != x and y_buf != y:
                steps += 1

            x_buf = x
            y_buf = y

    if step_count:
        return steps
    else:
        return points

def bresenham_int(beg_point, end_point, color, step_count = False):

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

    x_buf = x
    y_buf = y
    steps = 0

    i = 0
    while i <= dx:
        if step_count == False:
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

        if step_count:
            if x_buf != x and y_buf != y:
                steps += 1

            x_buf = x
            y_buf = y

    if step_count:
        return steps
    else:
        return points

def bresenham_antialiased(beg_point, end_point, color, step_count = False):

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

    I = 255

    m = dy / dx
    w = 1 - m
    e = 0.5
    
    x = beg_point[0]
    y = beg_point[1]
    points = []

    x_buf = x
    y_buf = y
    steps = 0

    i = 0
    while i <= dx:
        if step_count == False:
            points.append([x, y, get_color(color, I * e)])

        if e < w:
            if exchange == 0:
                x += x_sign
            else:
                y += y_sign

            e += m

        else:
            x += x_sign
            y += y_sign
            e -= w

        i += 1

        if step_count:
            if x_buf != x and y_buf != y:
                steps += 1

            x_buf = x
            y_buf = y

    if step_count:
        return steps
    else:
        return points
