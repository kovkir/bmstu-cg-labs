from tkinter import messagebox
from cyrus_beck_alg import check_polygon, cyrus_beck_algorithm, get_vector, vector_mul
from itertools import combinations

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 740

CANVAS_WIDTH = WINDOW_WIDTH - 310
CANVAS_HEIGHT = WINDOW_HEIGHT

def clear_canvas(canvas, lines, cutter_figure):
    canvas.delete("all")
    
    lines.clear()
    lines.append([])
    
    cutter_figure.clear()

def clear_cutter_figure(canvas, lines, cutter_figure):
    canvas.delete("all")

    draw_lines(canvas, lines)
    cutter_figure.clear()

def set_pixel(canvas, x, y, color):
    canvas.create_line(x, y, x + 1, y, fill = color)

def draw_lines(canvas, lines):
    for line in lines:
        if len(line) == 3:
            canvas.create_line(line[0], line[1], fill = line[2])

def get_color(color_var):
    col_var = color_var.get()

    if col_var == 0:
        color = "#000000"
    elif col_var == 1:
        color = "#ff0000"
    elif col_var == 2:
        color = "#0000ff"
    elif col_var == 3:
        color = "#3ebd33"
    elif col_var == 4:
        color = "#ffa600"
    else:
        color = "#bd08fc"
    
    return color

def click_left(event, lines, canvas, color_var):
    x = event.x
    y = event.y

    color = get_color(color_var)
    set_pixel(canvas, x, y, color)

    lines[-1].append([x, y])

    if len(lines[-1]) == 2:
        canvas.create_line(lines[-1][0], lines[-1][1], fill = color)

        lines[-1].append(color)
        lines.append([])

def click_right(event, lines, cutter_figure, canvas, color_var):
    if (len(cutter_figure) > 3 and cutter_figure[0] == cutter_figure[-1]):
        clear_cutter_figure(canvas, lines, cutter_figure)

    x = event.x
    y = event.y

    if (len(cutter_figure) > 0 and cutter_figure[-1][0] == x and 
                                   cutter_figure[-1][1] == y):
        return

    color = get_color(color_var)
    set_pixel(canvas, x, y, color)

    cutter_figure.append([x, y])

    if len(cutter_figure) >= 2:
        canvas.create_line(cutter_figure[-2], cutter_figure[-1], fill = color)

def click_centre(event, cutter_figure, canvas, color_var):
    if len(cutter_figure) < 3:
        messagebox.showwarning("Ошибка", 
            "Отсекатель должен иметь >= 3 вершин!\n")
        return

    if cutter_figure[0] == cutter_figure[-1]:
        return
        
    color = get_color(color_var)
    cutter_figure.append(cutter_figure[0])

    canvas.create_line(cutter_figure[-2], cutter_figure[-1], fill = color)

def add_line(lines, canvas, color_var, xb_entry, yb_entry, xe_entry, ye_entry):
    if len(lines[-1]) != 0:
        messagebox.showwarning("Ошибка", 
            "Предыдущий отрезок не был достроен!\n")
        return

    try:
        xb = int(xb_entry.get())
        yb = int(yb_entry.get())
        xe = int(xe_entry.get())
        ye = int(ye_entry.get())
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно заданны координаты границ отрезка!\n"
            "Ожидался ввод целых чисел.")
        return

    color = get_color(color_var)

    canvas.create_line([xb, yb], [xe, ye], fill = color)

    lines[-1].append([xb, yb])
    lines[-1].append([xe, ye])
    lines[-1].append(color)
    lines.append([])

def add_vertex_figure(lines, cutter_figure, canvas, color_var, x_cut_entry, y_cut_entry):
    try:
        x = int(x_cut_entry.get())
        y = int(y_cut_entry.get())
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно заданны координаты вершины отсекателя!\n"
            "Ожидался ввод целых чисел.")
        return
    
    if (len(cutter_figure) > 3 and cutter_figure[0] == cutter_figure[-1]):
        clear_cutter_figure(canvas, lines, cutter_figure)

    color = get_color(color_var)
    set_pixel(canvas, x, y, color)

    cutter_figure.append([x, y])

    if len(cutter_figure) >= 2:
        canvas.create_line(cutter_figure[-2], cutter_figure[-1], fill = color)

def find_starting_dot(cutter_figure):
    max_y = cutter_figure[0][1]
    i_max = 0
    
    for i in range(len(cutter_figure)):
        if cutter_figure[i][1] > max_y:
            max_y = cutter_figure[i][1]
            i_max = i

    cutter_figure.pop()

    for i in range(i_max):
        cutter_figure.append(cutter_figure.pop(0))

    cutter_figure.append(cutter_figure[0])

    if vector_mul(get_vector(cutter_figure[1], cutter_figure[2]), 
                  get_vector(cutter_figure[0], cutter_figure[1])) < 0:
        cutter_figure.reverse()

def line_koefs(x1, y1, x2, y2):
    a = y1 - y2
    b = x2 - x1
    c = x1 * y2 - x2 * y1

    return a, b, c

def solve_lines_intersection(a1, b1, c1, a2, b2, c2):
    opr =    a1  *   b2  -   a2  *   b1
    opr1 = (-c1) *   b2  -   b1  * (-c2)
    opr2 =   a1  * (-c2) - (-c1) *   a2

    if opr == 0:
        return -1, -1 # прямые параллельны

    x = opr1 / opr
    y = opr2 / opr

    return x, y

def is_coord_between(left_coord, right_coord, dot_coord):
    return min(left_coord, right_coord) <= dot_coord and \
           max(left_coord, right_coord) >= dot_coord

def is_dot_between(dot_left, dot_right, dot_intersec):
    return is_coord_between(dot_left[0], dot_right[0], dot_intersec[0]) and \
           is_coord_between(dot_left[1], dot_right[1], dot_intersec[1])

def are_connected_sides(line1, line2):
    if (line1[0][0] == line2[0][0] and line1[0][1] == line2[0][1]) or \
       (line1[1][0] == line2[1][0] and line1[1][1] == line2[1][1]) or \
       (line1[0][0] == line2[1][0] and line1[0][1] == line2[1][1]) or \
       (line1[1][0] == line2[0][0] and line1[1][1] == line2[0][1]):
        return True

    return False

def extra_check_polygon(cutter_figure): 
    # есть ли пересечения между несоседними сторонами
    cutter_lines = []

    for i in range(len(cutter_figure) - 1):
        cutter_lines.append([cutter_figure[i], cutter_figure[i + 1]])

    combs_lines = list(combinations(cutter_lines, 2)) # все возможные комбинации сторон

    for i in range(len(combs_lines)):
        line1 = combs_lines[i][0]
        line2 = combs_lines[i][1]

        if are_connected_sides(line1, line2):
            continue

        a1, b1, c1 = line_koefs(line1[0][0], line1[0][1], line1[1][0], line1[1][1])
        a2, b2, c2 = line_koefs(line2[0][0], line2[0][1], line2[1][0], line2[1][1])

        dot_intersec = solve_lines_intersection(a1, b1, c1, a2, b2, c2)

        if is_dot_between(line1[0], line1[1], dot_intersec) and \
           is_dot_between(line2[0], line2[1], dot_intersec):
            return True

    return False

def cut_off(cutter_figure, lines, canvas, color_cut_var, color_res_var):
    if len(cutter_figure) < 4:
        messagebox.showinfo("Ошибка", "Отсутствует отсекатель")
        return
    
    if cutter_figure[0] != cutter_figure[-1]:
        messagebox.showwarning("Ошибка", "Отсекатель не замкнут!\n")
        return

    if not check_polygon(cutter_figure):
        messagebox.showinfo("Ошибка", "Отсекатель должен быть выпуклым многоугольником")
        return

    if extra_check_polygon(cutter_figure[:]):
        messagebox.showinfo("Ошибка", "Отсекатель должен быть многоугольником")
        return

    cut_color = get_color(color_cut_var)
    res_color = get_color(color_res_var)

    canvas.create_polygon(cutter_figure, outline = cut_color, fill = "white")
    find_starting_dot(cutter_figure)

    for line in lines:
        if (len(line) == 3):
            cyrus_beck_algorithm(line, cutter_figure, res_color, canvas)
