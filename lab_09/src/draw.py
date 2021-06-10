from tkinter import messagebox
from itertools import combinations
import copy
from sutherland_hodgman_alg import check_polygon, sutherland_hodgman_algorythm, remove_odd_sides

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 740

CANVAS_WIDTH = WINDOW_WIDTH - 310
CANVAS_HEIGHT = WINDOW_HEIGHT

def clear_canvas(canvas, figure, cutter):
    canvas.delete("all")
    figure.clear()
    cutter.clear()

def clear_cutter(canvas, figure, cutter, color_fig_var):
    canvas.delete("all")

    draw_figure(canvas, figure, color_fig_var)
    cutter.clear()

def set_pixel(canvas, x, y, color):
    canvas.create_line(x, y, x + 1, y, fill = color)

def draw_figure(canvas, figure, color_var):
    color = get_color(color_var)

    for i in range(len(figure) - 1):
        canvas.create_line(figure[i], figure[i + 1], fill = color)

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

def click_left(event, figure, cutter, canvas, color_cut_var, color_fig_var):
    click_right(event, figure, cutter, canvas, color_cut_var, color_fig_var)

def click_right(event, figure, cutter, canvas, color_cut_var, color_fig_var):
    if len(cutter) > 3 and cutter[0] == cutter[-1]:
        clear_cutter(canvas, figure, cutter, color_fig_var)

    x = event.x
    y = event.y

    if len(cutter) > 0 and cutter[-1][0] == x and cutter[-1][1] == y:
        return

    color = get_color(color_cut_var)
    set_pixel(canvas, x, y, color)

    cutter.append([x, y])

    if len(cutter) >= 2:
        canvas.create_line(cutter[-2], cutter[-1], fill = color)

def close_figure(figure, canvas, color_var, fig_str):
    if len(figure) < 3:
        messagebox.showwarning("Ошибка", "%s иметь >= 3 вершин!\n" %(fig_str))
        return

    if figure[0] == figure[-1]:
        return
        
    color = get_color(color_var)
    figure.append(figure[0])

    canvas.create_line(figure[-2], figure[-1], fill = color)

def add_vertex(figure, cutter, canvas, color_cut_var, color_fig_var, x_entry, y_entry):
    try:
        x = int(x_entry.get())
        y = int(y_entry.get())
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно заданны координаты вершины!\n"
            "Ожидался ввод целых чисел.")
        return
    
    if len(cutter) > 3 and cutter[0] == cutter[-1]:
        clear_cutter(canvas, figure, cutter, color_fig_var)

    color = get_color(color_cut_var)
    set_pixel(canvas, x, y, color)

    cutter.append([x, y])

    if len(cutter) >= 2:
        canvas.create_line(cutter[-2], cutter[-1], fill = color)

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

def extra_check_polygon(cutter): 
    # есть ли пересечения между несоседними сторонами
    cutter_figure = []

    for i in range(len(cutter) - 1):
        cutter_figure.append([cutter[i], cutter[i + 1]])

    combs_figure = list(combinations(cutter_figure, 2)) # все возможные комбинации сторон

    for i in range(len(combs_figure)):
        line1 = combs_figure[i][0]
        line2 = combs_figure[i][1]

        if are_connected_sides(line1, line2):
            continue

        a1, b1, c1 = line_koefs(line1[0][0], line1[0][1], line1[1][0], line1[1][1])
        a2, b2, c2 = line_koefs(line2[0][0], line2[0][1], line2[1][0], line2[1][1])

        dot_intersec = solve_lines_intersection(a1, b1, c1, a2, b2, c2)

        if is_dot_between(line1[0], line1[1], dot_intersec) and \
           is_dot_between(line2[0], line2[1], dot_intersec):
            return True

    return False

def cut_off(cutter, figure, canvas, color_res_var):
    if len(cutter) < 4:
        messagebox.showinfo("Ошибка", "Отсутствует отсекатель")
        return

    if len(figure) < 4:
        messagebox.showinfo("Ошибка", "Отсутствует фигура")
        return
    
    if cutter[0] != cutter[-1]:
        messagebox.showwarning("Ошибка", "Отсекатель не замкнут!\n")
        return
    
    if figure[0] != figure[-1]:
        messagebox.showwarning("Ошибка", "Фигура не замкнута!\n")
        return

    if not check_polygon(cutter) or extra_check_polygon(cutter):
        messagebox.showinfo("Ошибка", "Отсекатель должен быть выпуклым многоугольником")
        return
    
    if extra_check_polygon(figure):
        messagebox.showinfo("Ошибка", "Фигура должна быть многоугольником")
        return
    
    res_color = get_color(color_res_var)
    result = copy.deepcopy(figure)

    for index in range(-1, len(cutter) - 1):
        line = [cutter[index], cutter[index + 1]]
        position_dot = cutter[index + 1]

        result = sutherland_hodgman_algorythm(line, position_dot, result)

        if len(result) <= 2:
            return

    draw_result_figure(result, canvas, res_color)

def draw_result_figure(figure_dots, canvas, res_color):
    fixed_figure = remove_odd_sides(figure_dots)

    for line in fixed_figure:
        canvas.create_line(line[0], line[1], fill = res_color)
