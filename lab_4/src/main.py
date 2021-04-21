from tkinter import Tk, ttk, Radiobutton, Checkbutton, Canvas, Label, Entry, Button, DISABLED, NORMAL, IntVar, BooleanVar
from draw import draw_figure, draw_spectrum, clear_canvas, WINDOW_HEIGHT, WINDOW_WIDTH, CANVAS_WIDTH, CANVAS_HEIGHT
from comparisons import time_comparison

spectrum_var_arr, spectrum_entry_arr, spectrum_widget_arr = [], [], []

def change_figure(rb_entry, figure):
    if figure.get() == True:
        rb_entry.configure(state = NORMAL)
        draw_fields_for_ellipse()
    else:
        rb_entry.configure(state = DISABLED)
        draw_fields_for_circle()

def change_spectrum_entry(step_x_entry, step_y_entry, step_BooleanVar):
    if step_BooleanVar.get() == True:
        step_y_entry.configure(state = NORMAL)
        step_x_entry.configure(state = DISABLED)
    else:
        step_x_entry.configure(state = NORMAL)
        step_y_entry.configure(state = DISABLED)

def activate_fields(spectrum_entry, is_activate):
    if is_activate:
        spectrum_entry.configure(state = NORMAL)
    else:
        spectrum_entry.configure(state = DISABLED)

def choice_fields(spectrum_var_arr, spectrum_entry_arr, index_method):
    if spectrum_var_arr[index_method].get():
        spectrum_var_arr[index_method].set(0)
        return

    size = len(spectrum_var_arr)

    for i in range(size):        
        if i != index_method and spectrum_var_arr[i].get() == False:
            spectrum_var_arr[i].set(1)
            activate_fields(spectrum_entry_arr[i], True)

    activate_fields(spectrum_entry_arr[index_method], False)

def place_forget(spectrum_entry_arr, spectrum_widget_arr):
    for i in spectrum_entry_arr:
        i.place_forget()

    for i in spectrum_widget_arr:
        i.place_forget()

def draw_fields_for_circle():
    global spectrum_var_arr, spectrum_entry_arr, spectrum_widget_arr

    place_forget(spectrum_entry_arr, spectrum_widget_arr)

    beg_radius_intvar   = IntVar()
    end_radius_intvar   = IntVar()
    step_intvar         = IntVar()
    count_figure_intvar = IntVar()

    beg_radius_intvar.set(1)
    step_intvar.set(1)
    count_figure_intvar.set(1)

    beg_radius_Checkbutton = Checkbutton(
        text = "Начальный радиус:", 
        variable = beg_radius_intvar,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w",
        command = lambda : choice_fields(spectrum_var_arr, spectrum_entry_arr, 0))
    beg_radius_Checkbutton.place(width = 200, height = 30, x = CANVAS_WIDTH + 30, y = 475)

    end_radius_Checkbutton = Checkbutton(
        text = "Конечный радиус:", 
        variable = end_radius_intvar,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w",
        command = lambda : choice_fields(spectrum_var_arr, spectrum_entry_arr, 1))
    end_radius_Checkbutton.place(width = 200, height = 30, x = CANVAS_WIDTH + 30, y = 505)

    step_Checkbutton = Checkbutton(
        text = "Шаг построения:", 
        variable = step_intvar,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w",
        command = lambda : choice_fields(spectrum_var_arr, spectrum_entry_arr, 2))
    step_Checkbutton.place(width = 200, height = 30, x = CANVAS_WIDTH + 30, y = 535)

    count_figure_Checkbutton = Checkbutton(
        text = "Количество фигур:", 
        variable = count_figure_intvar,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w",
        command = lambda : choice_fields(spectrum_var_arr, spectrum_entry_arr, 3))
    count_figure_Checkbutton.place(width = 200, height = 30, x = CANVAS_WIDTH + 30, y = 565)


    beg_radius_entry = Entry(font = ("Arial", 16))
    beg_radius_entry.place(width = 60, height = 30, x = CANVAS_WIDTH + 230, y = 475)

    end_radius_entry = Entry(font = ("Arial", 16))
    end_radius_entry.place(width = 60, height = 30, x = CANVAS_WIDTH + 230, y = 505)

    step_entry = Entry(font = ("Arial", 16))
    step_entry.place(width = 60, height = 30, x = CANVAS_WIDTH + 230, y = 535)

    count_figure_entry = Entry(font = ("Arial", 16))
    count_figure_entry.place(width = 60, height = 30, x = CANVAS_WIDTH + 230, y = 565)

    step_entry.insert(0, 10)
    count_figure_entry.insert(0, 15)

    beg_radius_entry.insert(0, 200)
    end_radius_entry.insert(0, 340)
    end_radius_entry.configure(state = DISABLED)

    spectrum_var_arr    = [beg_radius_intvar,      end_radius_intvar, 
                           step_intvar,            count_figure_intvar]
    spectrum_entry_arr  = [beg_radius_entry,       end_radius_entry, 
                           step_entry,             count_figure_entry]
    spectrum_widget_arr = [beg_radius_Checkbutton, end_radius_Checkbutton,
                           step_Checkbutton,       count_figure_Checkbutton]

def draw_fields_for_ellipse():
    global spectrum_var_arr, spectrum_entry_arr, spectrum_widget_arr
    
    place_forget(spectrum_entry_arr, spectrum_widget_arr)

    step_BooleanVar = BooleanVar()
    step_BooleanVar.set(0)

    radius_x_Label = Label(
        text = "Нач. значение Rx:", 
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w")
    radius_x_Label.place(width = 200, height = 30, x = CANVAS_WIDTH + 52, y = 460)

    radius_y_Label = Label(
        text = "Нач. значение Ry:", 
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w")
    radius_y_Label.place(width = 200, height = 30, x = CANVAS_WIDTH + 52, y = 490)

    step_x_Radiobutton = Radiobutton(
        text = "Шаг построения (ΔRx):", 
        variable = step_BooleanVar, value = 0,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w",
        command = lambda : change_spectrum_entry(step_x_entry, step_y_entry, step_BooleanVar))
    step_x_Radiobutton.place(width = 200, height = 30, x = CANVAS_WIDTH + 30, y = 520)

    step_y_Radiobutton = Radiobutton(
        text = "Шаг построения (ΔRy):", 
        variable = step_BooleanVar, value = 1,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w",
        command = lambda : change_spectrum_entry(step_x_entry, step_y_entry, step_BooleanVar))
    step_y_Radiobutton.place(width = 200, height = 30, x = CANVAS_WIDTH + 30, y = 550)

    count_figure_Label = Label(
        text = "Количество фигур:", 
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w")
    count_figure_Label.place(width = 200, height = 30, x = CANVAS_WIDTH + 52, y = 580)


    radius_x_entry = Entry(font = ("Arial", 16))
    radius_x_entry.place(width = 60, height = 30, x = CANVAS_WIDTH + 230, y = 460)

    radius_y_entry = Entry(font = ("Arial", 16))
    radius_y_entry.place(width = 60, height = 30, x = CANVAS_WIDTH + 230, y = 490)

    step_x_entry = Entry(font = ("Arial", 16))
    step_x_entry.place(width = 60, height = 30, x = CANVAS_WIDTH + 230, y = 520)

    step_y_entry = Entry(font = ("Arial", 16))
    step_y_entry.place(width = 60, height = 30, x = CANVAS_WIDTH + 230, y = 550)

    count_figure_entry = Entry(font = ("Arial", 16))
    count_figure_entry.place(width = 60, height = 30, x = CANVAS_WIDTH + 230, y = 580)


    radius_x_entry.insert(0, 200)
    radius_y_entry.insert(0, 100)

    count_figure_entry.insert(0, 20)
    step_x_entry.insert(0, 10)
    step_y_entry.insert(0, 10)
    step_y_entry.configure(state = DISABLED)

    spectrum_var_arr    = [step_BooleanVar]
    spectrum_entry_arr  = [radius_x_entry, radius_y_entry, step_x_entry, step_y_entry,
                           count_figure_entry]
    spectrum_widget_arr = [radius_x_Label, radius_y_Label, step_x_Radiobutton, step_y_Radiobutton, 
                           count_figure_Label]

def main():
    window = Tk()
    window.title("Лабораторная работа №4")
    window.geometry("%dx%d" %(WINDOW_WIDTH, WINDOW_HEIGHT))
    window.resizable(False, False)
    window["bg"] = "#e0e0eb"

    canvas = Canvas(window, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "white")
    canvas.place(x = 0, y = 0)


    Label(text = "ЦВЕТ ПОСТРОЕНИЯ", font = ("Arial", 15, "bold"), bg = "#7575a3",
        fg = "white").place(width = 305, height = 25, x = CANVAS_WIDTH + 5, y = 5)

    color_fg = IntVar()
    color_fg.set(3)

    Radiobutton(text = "Чёрный", variable = color_fg, value = 0,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 110, height = 20, x = CANVAS_WIDTH + 20, y = 40)

    Radiobutton(text = "Фоновый", variable = color_fg, value = 1,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 110, height = 20, x = CANVAS_WIDTH + 20, y = 60)

    Radiobutton(text = "Красный", variable = color_fg, value = 2,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 110, height = 20, x = CANVAS_WIDTH + 180, y = 40)

    Radiobutton(text = "Синий", variable = color_fg, value = 3,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 110, height = 20, x = CANVAS_WIDTH + 180, y = 60)


    Label(text = "АЛГОРИТМ ПОСТРОЕНИЯ", font = ("Arial", 15, "bold"), bg = "#7575a3",
        fg = "white").place(width = 305, height = 25, x = CANVAS_WIDTH + 5, y = 90)

    algorithm = IntVar()
    algorithm.set(0)

    Radiobutton(text = "Каноническое уравнение", variable = algorithm, value = 0,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 250, height = 20, x = CANVAS_WIDTH + 20, y = 125)

    Radiobutton(text = "Параметрическое уравнение", variable = algorithm, value = 1,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 250, height = 20, x = CANVAS_WIDTH + 20, y = 145)

    Radiobutton(text = "Алгоритм Брезенхема", variable = algorithm, value = 2,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 250, height = 20, x = CANVAS_WIDTH + 20, y = 165)

    Radiobutton(text = "Алгоритм средней точки", variable = algorithm, value = 3,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 280, height = 20, x = CANVAS_WIDTH + 20, y = 185)

    Radiobutton(text = "Библиотечная функция", variable = algorithm, value = 4,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 250, height = 20, x = CANVAS_WIDTH + 20, y = 205)


    Label(text = "ВЫБОР ФИГУРЫ", font = ("Arial", 15, "bold"), bg = "#7575a3",
        fg = "white").place(width = 305, height = 25, x = CANVAS_WIDTH + 5, y = 235)

    figure = BooleanVar()
    figure.set(0)

    Radiobutton(text = "Окружность", variable = figure, value = 0,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w",
        command = lambda: change_figure(rb_entry, figure)).\
        place(width = 110, height = 20, x = CANVAS_WIDTH + 20, y = 270)

    Radiobutton(text = "Эллипс", variable = figure, value = 1,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w",
        command = lambda: change_figure(rb_entry, figure)).\
        place(width = 110, height = 20, x = CANVAS_WIDTH + 180, y = 270)


    Label(text = "ПОСТРОЕНИЕ ФИГУРЫ", font = ("Arial", 15, "bold"), bg = "#7575a3",
        fg = "white").place(width = 305, height = 25, x = CANVAS_WIDTH + 5, y = 300)

    Label(text = "Xc\tYc\tRx\tRy  ", font = ("Arial", 16), bg = "#e0e0eb",
        fg = "#29293d").place(width = 260, height = 20, x = CANVAS_WIDTH + 30, y = 330)

    xc_entry = Entry(font = ("Arial", 16))
    xc_entry.place(width = 65, height = 30, x = CANVAS_WIDTH + 30, y = 355)

    yc_entry = Entry(font = ("Arial", 16))
    yc_entry.place(width = 65, height = 30, x = CANVAS_WIDTH + 95, y = 355)

    ra_entry = Entry(font = ("Arial", 16))
    ra_entry.place(width = 65, height = 30, x = CANVAS_WIDTH + 160, y = 355)

    rb_entry = Entry(font = ("Arial", 16))
    rb_entry.place(width = 65, height = 30, x = CANVAS_WIDTH + 225, y = 355)

    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 260, height = 30,  x = CANVAS_WIDTH + 30, y = 390)

    Button(text = "Построить фигуру", font = ("Arial", 16), 
        highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
        command = lambda: draw_figure(canvas, color_fg, algorithm, figure, 
                          xc_entry, yc_entry, ra_entry, rb_entry)).\
        place(width = 256, height = 26,  x = CANVAS_WIDTH + 32, y = 392)


    Label(text = "ПОСТРОЕНИЕ СПЕКТРА", font = ("Arial", 15, "bold"), bg = "#7575a3",
        fg = "white").place(width = 305, height = 25, x = CANVAS_WIDTH + 5, y = 430)

    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 260, height = 30,  x = CANVAS_WIDTH + 30, y = 615)

    Button(text = "Построить cпектр", font = ("Arial", 16), 
        highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
        command = lambda: draw_spectrum(canvas, color_fg, algorithm, figure, 
                          xc_entry, yc_entry, spectrum_var_arr, spectrum_entry_arr)).\
        place(width = 256, height = 26,  x = CANVAS_WIDTH + 32, y = 617)


    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 260, height = 30,  x = CANVAS_WIDTH + 30, y = 655)

    Button(text = "Сравнение времени", font = ("Arial", 16), 
        highlightbackground = "#d1d1e0", highlightthickness = 30, fg = "#33334d",
        command = lambda: time_comparison(canvas, color_fg, algorithm, figure)).\
        place(width = 256, height = 26,  x = CANVAS_WIDTH + 32, y = 657)


    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 260, height = 30,  x = CANVAS_WIDTH + 30, y = 695)

    Button(text = "Очистить экран", font = ("Arial", 16), 
        highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
        command = lambda: clear_canvas(canvas)).\
        place(width = 256, height = 26,  x = CANVAS_WIDTH + 32, y = 697)


    xc_entry.insert(0, int(CANVAS_WIDTH / 2))
    yc_entry.insert(0, int(CANVAS_HEIGHT / 2))

    ra_entry.insert(0, 200)
    rb_entry.insert(0, 150)
    rb_entry.configure(state = DISABLED)

    change_figure(rb_entry, figure)
    
    window.mainloop()

if __name__ == "__main__":
    main()
