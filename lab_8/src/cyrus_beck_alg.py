def get_vector(dot1, dot2):
    return [dot2[0] - dot1[0], dot2[1] - dot1[1]]

def vector_mul(vec1, vec2):
    return (vec1[0] * vec2[1] - vec1[1] * vec2[0])

def scalar_mul(vec1, vec2):
    return (vec1[0] * vec2[0] + vec1[1] * vec2[1])

def check_polygon(cutter_figure): 
    if (len(cutter_figure) < 4):
        return False

    if vector_mul(get_vector(cutter_figure[1], cutter_figure[2]), 
                  get_vector(cutter_figure[0], cutter_figure[1])) > 0:
        sign = 1 # по часовой стрелке
    else:
        sign = -1 # против часовой стрелки

    for i in range(3, len(cutter_figure)):
        if sign * vector_mul(get_vector(cutter_figure[i - 1], cutter_figure[i]),
                             get_vector(cutter_figure[i - 2], cutter_figure[i - 1])) < 0:
            return False

    return True

def get_normal(dot1, dot2, dot3):
    vector = get_vector(dot1, dot2)

    if vector[1]:
        normal = [1, - vector[0] / vector[1]]
    else:
        normal = [0, 1]

    if scalar_mul(get_vector(dot2, dot3), normal) < 0:
        normal[0] = - normal[0]
        normal[1] = - normal[1]

    return normal

def cyrus_beck_algorithm(line, cutter_figure, res_color, canvas):
    t_beg = 0
    t_end = 1

    dot1 = line[0]
    dot2 = line[1]

    d = [dot2[0] - dot1[0], dot2[1] - dot1[1]] #директриса

    for i in range(-2, len(cutter_figure) - 2):
        normal = get_normal(cutter_figure[i], cutter_figure[i + 1], cutter_figure[i + 2])

        w = [dot1[0] - cutter_figure[i][0],
             dot1[1] - cutter_figure[i][1]]

        d_scalar = scalar_mul(d, normal)
        w_scalar = scalar_mul(w, normal)

        if d_scalar == 0:
            if w_scalar < 0:
                return
            else:
                continue

        t = - w_scalar / d_scalar

        if d_scalar > 0:
            if t <= 1:
                t_beg = max(t_beg, t)
            else:
                return

        elif d_scalar < 0:
            if t >= 0:
                t_end = min(t_end, t)
            else:
                return

        if t_beg > t_end:
            break

    if t_beg <= t_end:
        dot1_res = [round(dot1[0] + d[0] * t_beg), round(dot1[1] + d[1] * t_beg)]
        dot2_res = [round(dot1[0] + d[0] * t_end), round(dot1[1] + d[1] * t_end)]

        canvas.create_line(dot1_res, dot2_res, fill = res_color)
