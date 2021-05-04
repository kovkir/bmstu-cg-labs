from tkinter import messagebox, PhotoImage, END
from math import cos, sin, radians, pi
import colorutils as cu
import time

from brezenham import bresenham_int

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 740

CANVAS_WIDTH = WINDOW_WIDTH - 310
CANVAS_HEIGHT = WINDOW_HEIGHT

index_point = 0

def clear_canvas(img, canvas, figures, p_min, p_max, time_entry, points_listbox):
    global index_point

    img.put("#FFFFFF", to = (0, 0, CANVAS_WIDTH, CANVAS_HEIGHT))

    p_min[0] = CANVAS_WIDTH
    p_min[1] = CANVAS_HEIGHT
    p_max[0] = 0
    p_max[1] = 0
    
    index_point = 0
    points_listbox.delete(0, END)
    time_entry.delete(0, END)
    figures.clear()
    figures.append([[]])

def set_pixel(img, x, y, color):
    img.put(color.hex, (x, y))

def draw_line(img, points):
    for i in points:
        set_pixel(img, i[0], i[1], i[2])

def get_color(color_var):
    col_var = color_var.get()

    if col_var == 0:
        color = cu.Color((0, 0, 0))
    elif col_var == 1:
        color = cu.Color((255, 0, 0))
    elif col_var == 2:
        color = cu.Color((0, 0, 255))
    elif col_var == 3:
        color = cu.Color((62, 189, 51))
    elif col_var == 4:
        color = cu.Color((255, 211, 51))
    else:
        color = cu.Color((189, 8, 252))
    
    return color

def max_min_point(x, y, p_min, p_max):
    if x > p_max[0]:
        p_max[0] = x
    if x < p_min[0]:
        p_min[0] = x
    if y > p_max[1]:
        p_max[1] = y
    if y < p_min[1]:
        p_min[1] = y

def click_left(event, figures, img, color_var, p_min, p_max, points_listbox):
    global index_point

    x = event.x
    y = event.y

    max_min_point(x, y, p_min, p_max)

    color = get_color(color_var)
    set_pixel(img, x, y, color)

    figures[-1][-1].append([x, y])

    index_point += 1
    pstr = "%d. (%d, %d)" %(index_point, x, y)
    points_listbox.insert(END, pstr)

    if len(figures[-1][-1]) == 2:
        points = bresenham_int(figures[-1][-1][0], figures[-1][-1][1], color)
        draw_line(img, points)

        figures[-1][-1].append(points)
        figures[-1].append([figures[-1][-1][1]])

def click_right(event, figures, img, color_var, points_listbox):
    if len(figures[-1][-1]) == 0:
        messagebox.showwarning("Ошибка", "Незамкнутых фигур нет!")
        return
    
    if len(figures[-1]) <= 2:
        messagebox.showwarning("Ошибка", "Фигура должна иметь больше 1 ребра!")
        return

    point = figures[-1][0][0]
    figures[-1][-1].append(point)

    color = get_color(color_var)

    points = bresenham_int(figures[-1][-1][0], figures[-1][-1][1], color)
    draw_line(img, points)

    figures[-1][-1].append(points)
    figures.append([[]])

def draw_point(figures, img, color_var, x_entry, y_entry, p_min, p_max, points_listbox):
    global index_point

    try:
        x = int(x_entry.get())
        y = int(y_entry.get())
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно заданны координаты точки!\n"
            "Ожидался ввод целых чисел.")
        return

    max_min_point(x, y, p_min, p_max)

    color = get_color(color_var)
    set_pixel(img, x, y, color)

    figures[-1][-1].append([x, y])

    index_point += 1
    pstr = "%d. (%d, %d)" %(index_point, x, y)
    points_listbox.insert(END, pstr)

    if len(figures[-1][-1]) == 2:
        points = bresenham_int(figures[-1][-1][0], figures[-1][-1][1], color)
        draw_line(img, points)

        figures[-1][-1].append(points)
        figures[-1].append([figures[-1][-1][1]])

def draw_borders(img, figures):
    for fig in figures:
        for line in fig:
            if len(line) != 0:
                draw_line(img, line[2])

def mark_desired_pixels(img, figures, mark_color):
    for fig in figures:
        for line in fig:
            if len(line) == 0 or line[1][1] == line[0][1]:
                continue

            if line[1][1] > line[0][1]:
                y_max = line[1][1]
                y_min = line[0][1]
            else:
                y_max = line[0][1]
                y_min = line[1][1]

            dx = line[1][0] - line[0][0]
            dy = line[1][1] - line[0][1]

            y = y_min
            while y < y_max:                    
                x = dx / dy * (y - line[0][1]) + line[0][0]

                if img.get(int(x) + 1, y) == mark_color.rgb:
                    set_pixel(img, int(x) + 2, y, mark_color)
                else:
                    set_pixel(img, int(x) + 1, y, mark_color)

                y += 1

def fill_figure(figures, img, canvas, color_var, p_min, p_max, mode_var, time_entry):
    if len(figures[-1][0]) != 0:
        messagebox.showwarning("Ошибка", "Не все фигуры замкнуты!")
        return
        
    mark_color = get_color(color_var) + (1, 1, 1)
    bg_color  = cu.Color((255, 255, 255))
    figure_color = get_color(color_var)

    flag = False
    delay = mode_var.get()

    x_max = p_max[0]
    x_min = p_min[0]
    y_max = p_max[1]
    y_min = p_min[1]
    
    start_time = time.time()

    mark_desired_pixels(img, figures, mark_color)

    for y in range(y_max, y_min, -1):
        for x in range(x_min, x_max + 2):

            if img.get(x, y) == mark_color.rgb:
                flag = not flag

            if flag:
                set_pixel(img, x, y, figure_color)
            else:
                set_pixel(img, x, y, bg_color)

        if delay:
            canvas.update()

    canvas.update()

    end_time = time.time()

    draw_borders(img, figures)

    time_str = str(round(end_time - start_time, 2)) + "s"
    time_entry.delete(0, END)
    time_entry.insert(0, time_str)
