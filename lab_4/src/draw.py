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

def clear_canvas(canvas):
    canvas.delete("all")
    
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
        canonical_ellipse(xc, yc, ra, rb, color, canvas, draw)
    elif alg == 1:
        parameter_ellipse(xc, yc, ra, rb, color, canvas, draw)
    elif alg == 2:
        bresenham_ellipse(xc, yc, ra, rb, color, canvas, draw)
    elif alg == 3:
        midpoint_ellipse(xc, yc, ra, rb, color, canvas, draw)
    else:
        lib_ellipse(canvas, xc, yc, ra, rb, color)
        return
    
def add_circle(canvas, color_fg, algorithm, xc, yc, r, draw = True):
    color = get_color(color_fg)
    alg = algorithm.get()

    if alg == 0:
        canonical_сircle(xc, yc, r, color, canvas, draw)
    elif alg == 1:
        parameter_circle(xc, yc, r, color, canvas, draw)
    elif alg == 2:
        bresenham_circle(xc, yc, r, color, canvas, draw)
    elif alg == 3:
        midpoint_circle(xc, yc, r, color, canvas, draw)
    else:
        lib_ellipse(canvas, xc, yc, r, r, color)
        return

def draw_figure(canvas, color_fg, algorithm, figure, 
                xc_entry, yc_entry, ra_entry, rb_entry):
    ellipse = figure.get()

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

        if ellipse == True:
            rb = int(rb_entry.get())
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно заданны полуоси фигуры!\n"
            "Ожидался ввод целых чисел.")
        return
    
    if ra <= 0 or ellipse and rb <= 0:
        messagebox.showwarning("Ошибка", 
            "Значения полуосей фигуры должны быть больше 0.")
        return

    if ellipse:
        add_ellipse(canvas, color_fg, algorithm, xc, yc, ra, rb)
    else:
        add_circle(canvas, color_fg, algorithm, xc, yc, ra)

def draw_spectrum_ellipse(canvas, color_fg, algorithm, xc, yc,
                          spectrum_var_arr, spectrum_entry_arr):

    radius_x_entry     = spectrum_entry_arr[0]
    radius_y_entry     = spectrum_entry_arr[1]
    step_x_entry       = spectrum_entry_arr[2]
    step_y_entry       = spectrum_entry_arr[3]
    count_figure_entry = spectrum_entry_arr[4]

    try:
        ra = int(radius_x_entry.get())
        rb = int(radius_y_entry.get())
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно заданны полуоси фигуры!\n"
            "Ожидался ввод целых чисел.")
        return

    try:
        if spectrum_var_arr[0].get():
            step = int(step_y_entry.get())
        else:
            step = int(step_x_entry.get())
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно задан шаг для построения спектра!\n"
            "Ожидался ввод целого числа.")
        return

    try:
        count_fig = int(count_figure_entry.get())
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
    elif ra <= 0 or rb <= 0:
        messagebox.showwarning("Ошибка", 
            "Значения полуосей эллипса должны быть больше 0.")
        return

    constant = ra / rb 

    while count_fig > 0:
        add_ellipse(canvas, color_fg, algorithm, xc, yc, ra, rb)

        if spectrum_var_arr[0].get():
            rb += step
            ra = round(rb * constant)
        else:
            ra += step
            rb = round(ra / constant)

        count_fig -= 1

def get_necessary_data_for_spectrum(r_beg, r_end, step, count_fig):
    if r_beg == 0:
        r_beg = r_end - (count_fig - 1) * step
    elif step == 0:
        if count_fig == 0:
            step = int(r_end - r_beg) + 1
        else:
            step = int((r_end - r_beg) / (count_fig - 1))
    elif count_fig == 0:
        count_fig = int((r_end - r_beg) / step) + 1

    return r_beg, step, count_fig

def draw_spectrum_circle(canvas, color_fg, algorithm, xc, yc,
                         spectrum_var_arr, spectrum_entry_arr):

    beg_radius_entry   = spectrum_entry_arr[0]
    end_radius_entry   = spectrum_entry_arr[1]
    step_entry         = spectrum_entry_arr[2]
    count_figure_entry = spectrum_entry_arr[3]

    beg_radius_intvar   = spectrum_var_arr[0]
    end_radius_intvar   = spectrum_var_arr[1]
    step_intvar         = spectrum_var_arr[2]
    count_figure_intvar = spectrum_var_arr[3]

    r_beg, r_end, step, count_fig = 0, 0, 0, 0

    if beg_radius_intvar.get():
        try:
            r_beg = int(beg_radius_entry.get())
        except:
            messagebox.showwarning("Ошибка", 
                "Неверно заданн радиус окружности!\n"
                "Ожидался ввод целого числа.")
            return
        
        if r_beg <= 0:
            messagebox.showwarning("Ошибка", 
                "Радиус окружности должен быть больше 0.")
            return

    if end_radius_intvar.get():
        try:
            r_end = int(end_radius_entry.get())
        except:
            messagebox.showwarning("Ошибка", 
                "Неверно заданн радиус окружности!\n"
                "Ожидался ввод целого числа.")
            return
        
        if r_end <= 0:
            messagebox.showwarning("Ошибка", 
                "Радиус окружности должен быть больше 0.")
            return
        elif r_end <= r_beg:
            messagebox.showwarning("Ошибка", 
                "Конечный радиус окружности должен быть больше начального.")
            return

    if step_intvar.get():
        try:
            step = int(step_entry.get())
        except:
            messagebox.showwarning("Ошибка", 
                "Неверно задан шаг для построения спектра!\n"
                "Ожидался ввод целого числа.")
            return
        
        if step <= 0:
            messagebox.showwarning("Ошибка", 
                "Шаг для построения спектра должен быть больше 0.")
            return

    if count_figure_intvar.get():
        try:
            count_fig = int(count_figure_entry.get())
        except:
            messagebox.showwarning("Ошибка", 
                "Неверно заданно кол-во фигур для построения спектра!\n"
                "Ожидался ввод целого числа.")
            return
        
        if count_fig <= 0:
            messagebox.showwarning("Ошибка", 
                "Кол-во фигур для построения спектра должно быть больше 0.")
            return

    r, step, count_fig = get_necessary_data_for_spectrum(r_beg, r_end, step, count_fig)

    while count_fig > 0:
        add_circle(canvas, color_fg, algorithm, xc, yc, r)

        r += step
        count_fig -= 1
    
def draw_spectrum(canvas, color_fg, algorithm, figure, xc_entry, yc_entry,
                  spectrum_var_arr, spectrum_entry_arr):
    try:
        xc = int(xc_entry.get())
        yc = int(yc_entry.get())
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно заданны координаты центра фигуры!\n"
            "Ожидался ввод целых чисел.")
        return
    
    if figure.get():
        draw_spectrum_ellipse(canvas, color_fg, algorithm, xc, yc,
                              spectrum_var_arr, spectrum_entry_arr)
    else:
        draw_spectrum_circle(canvas, color_fg, algorithm, xc, yc,
                              spectrum_var_arr, spectrum_entry_arr)
