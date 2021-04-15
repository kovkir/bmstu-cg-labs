from tkinter import messagebox
import colorutils as cu

from brezenham import bresenham_ellipse, bresenham_circle
from canonical import canonical_ellipse, canonical_сircle
from parametric import parameter_ellipse, parameter_circle
from midpoint import midpoint_ellipse, midpoint_circle

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 740

CANVAS_WIDTH = WINDOW_HEIGHT + 150
CANVAS_HEIGHT = WINDOW_HEIGHT

def set_pixel(canvas, x, y, color):
    canvas.create_line(x, y, x + 1, y, fill = color.hex)

def lib_ellipse(canvas, xc, yc, ra, rb, color):
    canvas.create_oval(xc - ra, yc - rb, xc + ra, yc + rb, outline = color.hex)

def get_color(color_fg):
    col_fg = color_fg.get()

    if col_fg == 0:
        color = cu.Color((0, 0, 0))
    elif col_fg == 1:
        color = cu.Color((255, 255, 255))
    elif col_fg == 2:
        color = cu.Color((255, 0, 0))
    else:
        color = cu.Color((0, 0, 255))
    
    return color

def add_ellipse(canvas, color_fg, algorithm, xc, yc, ra, rb, draw = True):
    color = get_color(color_fg)
    alg = algorithm.get()

    if alg == 0:
        dots = canonical_ellipse(xc, yc, ra, rb, color)
    elif alg == 1:
        dots = parameter_ellipse(xc, yc, ra, rb, color)
    elif alg == 2:
        dots = bresenham_ellipse(xc, yc, ra, rb, color)
    elif alg == 3:
        dots = midpoint_ellipse(xc, yc, ra, rb, color)
    else:
        lib_ellipse(canvas, xc, yc, ra, rb, color)
        return

    if draw:
        for i in dots:
            set_pixel(canvas, i[0], i[1], i[2])
    
def add_circle(canvas, color_fg, algorithm, xc, yc, r, draw = True):
    color = get_color(color_fg)
    alg = algorithm.get()

    if alg == 0:
        dots = canonical_сircle(xc, yc, r, color)
    elif alg == 1:
        dots = parameter_circle(xc, yc, r, color)
    elif alg == 2:
        dots = bresenham_circle(xc, yc, r, color)
    elif alg == 3:
        dots = midpoint_circle(xc, yc, r, color)
    else:
        lib_ellipse(canvas, xc, yc, r, r, color)
        return

    if draw:
        for i in dots:
            set_pixel(canvas, i[0], i[1], i[2])

def draw_figure(canvas, color_fg, algorithm, figure, 
                xc_entry, yc_entry, ra_entry, rb_entry):
    try:
        xc = int(xc_entry.get())
        yc = int(yc_entry.get())
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно заданны координаты центра фигуры!\n"
            "Ожидался ввод целых чисел.")
        return
    
    try:
        ra = int(ra_entry.get())

        if figure.get() == True:
            rb = int(rb_entry.get())
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно заданны полуоси фигуры!\n"
            "Ожидался ввод целых чисел.")
        return

    if figure.get() == True:
        add_ellipse(canvas, color_fg, algorithm, xc, yc, ra, rb)
    else:
        add_circle(canvas, color_fg, algorithm, xc, yc, ra)

def draw_spectrum(canvas, color_fg, algorithm, figure, 
                  xc_entry, yc_entry, ra_entry, rb_entry, step_entry, count_fig_entry):
    try:
        xc = int(xc_entry.get())
        yc = int(yc_entry.get())
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно заданны координаты центра фигуры!\n"
            "Ожидался ввод целых чисел.")
        return
    
    try:
        ra = int(ra_entry.get())

        if figure.get() == True:
            rb = int(rb_entry.get())
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно заданны полуоси фигуры!\n"
            "Ожидался ввод целых чисел.")
        return

    try:
        step = int(step_entry.get())
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно задан шаг для построения спектра!\n"
            "Ожидался ввод целого числа.")
        return

    try:
        count_fig = int(count_fig_entry.get())
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно заданно кол-во фигур для построения спектра!\n"
            "Ожидался ввод целого числа.")
        return
    
    if step <= 0:
        messagebox.showwarning("Ошибка", 
            "Шаг для построения спектра должен быть больше 0.")
        return
    elif count_fig <= 0:
        messagebox.showwarning("Ошибка", 
            "Кол-во фигур для построения спектра должно быть больше 0.")
        return

    ellipse = figure.get()

    while count_fig > 0:
        if ellipse:
            add_ellipse(canvas, color_fg, algorithm, xc, yc, ra, rb)

            rb += step
        else:
            add_circle(canvas, color_fg, algorithm, xc, yc, ra)

        ra += step
        count_fig -= 1
    
def clear_canvas(canvas):
    canvas.delete("all")
