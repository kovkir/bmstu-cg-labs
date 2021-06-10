"""
    Алгоритм цифрового дифференциального анализатора
"""

def dda(beg_point, end_point, color, step_count = False):
    
    dx = (end_point[0] - beg_point[0])
    dy = (end_point[1] - beg_point[1])

    if dx == 0 and dy == 0:
        return [[round(beg_point[0]), round(beg_point[1]), color]]

    l = abs(dx) if abs(dx) >= abs(dy) else abs(dy)
    
    dx /= l
    dy /= l

    x = beg_point[0]
    y = beg_point[1]

    points = [[round(x), round(y), color]]
    steps = 0

    i = 1
    while i <= l:
        if step_count:
            x_buf = x
            y_buf = y

        x += dx
        y += dy

        if step_count == False:
            points.append([round(x), round(y), color])

        elif round(x_buf) != round(x) and \
             round(y_buf) != round(y):
            steps += 1

        i += 1

    if step_count:
        return steps
    else:
        return points
