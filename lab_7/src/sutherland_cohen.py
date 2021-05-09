'''
Алгоритм Сазерленда - Коэна
'''

def get_point_bits(rectangle, point):
    bits = 0b0000

    if point[0] < rectangle[0]:
        bits += 0b0001

    if point[0] > rectangle[1]:
        bits += 0b0010
    
    if point[1] > rectangle[2]:
        bits += 0b0100
        
    if point[1] < rectangle[3]:
        bits += 0b1000

    return bits

def get_visibility(p1_bits, p2_bits):
    visibility = 0 # 0 - частично видимый; 1 - видим; -1 - не видим

    if p1_bits == 0 and p2_bits == 0:
        visibility = 1
    elif p1_bits & p2_bits:
        visibility = -1

    return visibility

def get_bit(point_bits, i):
    return (point_bits >> i) & 1

def alg_sutherland_cohen(rectangle, line, canvas, color):
    p1 = [line[0][0], line[0][1]]
    p2 = [line[1][0], line[1][1]]

    flag = 1 # при горизонтальности = 0; при вертикальности = -1 

    if p1[0] == p2[0]:
        flag = -1
    else:
        m = (p2[1] - p1[1]) / (p2[0] - p1[0])

        if m == 0:
            flag = 0

    for i in range(4):
        p1_bits = get_point_bits(rectangle, p1)
        p2_bits = get_point_bits(rectangle, p2)

        visibility = get_visibility(p1_bits, p2_bits)

        if visibility == -1:
            return
        elif visibility == 1:
            break

        if get_bit(p1_bits, i) == get_bit(p2_bits, i):
            continue

        if get_bit(p1_bits, i) == 0:
            p1, p2 = p2, p1

        if flag != -1:
            if i < 2:
                p1[1] = m * (rectangle[i] - p1[0]) + p1[1]
                p1[0] = rectangle[i]
                continue
            else:
                p1[0] = (1 / m) * (rectangle[i] - p1[1]) + p1[0]

        p1[1] = rectangle[i]

    canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill = color)
    