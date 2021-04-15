from tkinter import Tk, ttk, Radiobutton, Canvas, Label, Entry, Button, DISABLED, NORMAL, IntVar, BooleanVar
from draw import draw_figure, draw_spectrum, clear_canvas, WINDOW_HEIGHT, WINDOW_WIDTH, CANVAS_WIDTH, CANVAS_HEIGHT
from comparisons import time_comparison

def change_figure(rb_entry, figure):
    if figure.get() == True:
        rb_entry.configure(state = NORMAL)
    else:
        rb_entry.configure(state = DISABLED)

def main():
    window = Tk()
    window.title("Лабораторная работа №4")
    window.geometry("%dx%d" %(WINDOW_WIDTH, WINDOW_HEIGHT))
    window.resizable(False, False)
    window["bg"] = "#e0e0eb"

    canvas = Canvas(window, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "white")
    canvas.place(x = 0, y = 0)



    Label(text = "ЦВЕТ ПОСТРОЕНИЯ", font = ("Arial", 16, "bold"), bg = "#7575a3",
        fg = "white").place(width = 305, height = 30, x = CANVAS_WIDTH + 5, y = 10)

    color_fg = IntVar()
    color_fg.set(3)

    Radiobutton(text = "Чёрный", variable = color_fg, value = 0,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 110, height = 20, x = CANVAS_WIDTH + 20, y = 50)

    Radiobutton(text = "Фоновый", variable = color_fg, value = 1,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 110, height = 20, x = CANVAS_WIDTH + 20, y = 70)

    Radiobutton(text = "Красный", variable = color_fg, value = 2,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 110, height = 20, x = CANVAS_WIDTH + 180, y = 50)

    Radiobutton(text = "Синий", variable = color_fg, value = 3,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 110, height = 20, x = CANVAS_WIDTH + 180, y = 70)



    Label(text = "АЛГОРИТМ ПОСТРОЕНИЯ", font = ("Arial", 16, "bold"), bg = "#7575a3",
        fg = "white").place(width = 305, height = 30, x = CANVAS_WIDTH + 5, y = 100)

    algorithm = IntVar()
    algorithm.set(0)

    Radiobutton(text = "Каноническое уравнение", variable = algorithm, value = 0,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 250, height = 20, x = CANVAS_WIDTH + 20, y = 140)

    Radiobutton(text = "Параметрическое уравнение", variable = algorithm, value = 1,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 250, height = 20, x = CANVAS_WIDTH + 20, y = 160)

    Radiobutton(text = "Алгоритм Брезенхема", variable = algorithm, value = 2,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 250, height = 20, x = CANVAS_WIDTH + 20, y = 180)

    Radiobutton(text = "Алгоритм средней точки", variable = algorithm, value = 3,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 280, height = 20, x = CANVAS_WIDTH + 20, y = 200)

    Radiobutton(text = "Библиотечная функция", variable = algorithm, value = 4,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 250, height = 20, x = CANVAS_WIDTH + 20, y = 220)



    Label(text = "ВЫБОР ФИГУРЫ", font = ("Arial", 16, "bold"), bg = "#7575a3",
        fg = "white").place(width = 305, height = 30, x = CANVAS_WIDTH + 5, y = 250)

    figure = BooleanVar()
    figure.set(0)

    Radiobutton(text = "Окружность", variable = figure, value = 0,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w",
        command = lambda: change_figure(rb_entry, figure)).\
        place(width = 110, height = 20, x = CANVAS_WIDTH + 20, y = 290)

    Radiobutton(text = "Эллипс", variable = figure, value = 1,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w",
        command = lambda: change_figure(rb_entry, figure)).\
        place(width = 110, height = 20, x = CANVAS_WIDTH + 180, y = 290)



    Label(text = "ПОСТРОЕНИЕ ФИГУРЫ", font = ("Arial", 16, "bold"), bg = "#7575a3",
        fg = "white").place(width = 305, height = 30, x = CANVAS_WIDTH + 5, y = 320)

    Label(text = "Xc\tYc\tRa\tRb  ", font = ("Arial", 16), bg = "#e0e0eb",
        fg = "#29293d").place(width = 260, height = 20, x = CANVAS_WIDTH + 30, y = 360)

    xc_entry = Entry(font = ("Arial", 16))
    xc_entry.place(width = 65, height = 30, x = CANVAS_WIDTH + 30, y = 390)

    yc_entry = Entry(font = ("Arial", 16))
    yc_entry.place(width = 65, height = 30, x = CANVAS_WIDTH + 95, y = 390)

    ra_entry = Entry(font = ("Arial", 16))
    ra_entry.place(width = 65, height = 30, x = CANVAS_WIDTH + 160, y = 390)

    rb_entry = Entry(font = ("Arial", 16))
    rb_entry.place(width = 65, height = 30, x = CANVAS_WIDTH + 225, y = 390)

    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 260, height = 30,  x = CANVAS_WIDTH + 30, y = 430)

    Button(text = "Построить фигуру", font = ("Arial", 16), 
        highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
        command = lambda: draw_figure(canvas, color_fg, algorithm, figure, 
                          xc_entry, yc_entry, ra_entry, rb_entry)).\
        place(width = 256, height = 26,  x = CANVAS_WIDTH + 32, y = 432)



    Label(text = "ПОСТРОЕНИЕ СПЕКТРА", font = ("Arial", 16, "bold"), bg = "#7575a3",
        fg = "white").place(width = 305, height = 30, x = CANVAS_WIDTH + 5, y = 470)

    Label(text = "Шаг построения:", font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d",
        anchor = "w").place(width = 150, height = 30, x = CANVAS_WIDTH + 30, y = 510)

    step_entry = Entry(font = ("Arial", 16))
    step_entry.place(width = 100, height = 30, x = CANVAS_WIDTH + 190, y = 510)

    Label(text = "Количество фигур:", font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d",
        anchor = "w").place(width = 150, height = 30, x = CANVAS_WIDTH + 30, y = 540)

    count_fig_entry = Entry(font = ("Arial", 16))
    count_fig_entry.place(width = 100, height = 30, x = CANVAS_WIDTH + 190, y = 540)

    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 260, height = 30,  x = CANVAS_WIDTH + 30, y = 580)

    Button(text = "Построить cпектр", font = ("Arial", 16), 
        highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
        command = lambda: draw_spectrum(canvas, color_fg, algorithm, figure, 
                          xc_entry, yc_entry, ra_entry, rb_entry, 
                          step_entry, count_fig_entry)).\
        place(width = 256, height = 26,  x = CANVAS_WIDTH + 32, y = 582)



    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 260, height = 40,  x = CANVAS_WIDTH + 30, y = 630)

    Button(text = "Сравнение времени", font = ("Arial", 16), 
        highlightbackground = "#d1d1e0", highlightthickness = 30, fg = "#33334d",
        command = lambda: time_comparison(canvas, color_fg, algorithm, figure)).\
        place(width = 256, height = 36,  x = CANVAS_WIDTH + 32, y = 632)


    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 260, height = 40,  x = CANVAS_WIDTH + 30, y = 685)

    Button(text = "Очистить экран", font = ("Arial", 16), 
        highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
        command = lambda: clear_canvas(canvas)).\
        place(width = 256, height = 36,  x = CANVAS_WIDTH + 32, y = 687)



    step_entry.insert(0, 10)
    count_fig_entry.insert(0, 15)

    xc_entry.insert(0, int(CANVAS_WIDTH / 2))
    yc_entry.insert(0, int(CANVAS_HEIGHT / 2))

    ra_entry.insert(0, 200)
    rb_entry.insert(0, 150)
    rb_entry.configure(state = DISABLED)

    window.mainloop()

if __name__ == "__main__":
    main()
