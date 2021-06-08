from tkinter import Tk, Radiobutton, Canvas, Label, Entry, Button, DISABLED, IntVar
from draw import WINDOW_HEIGHT, WINDOW_WIDTH, CANVAS_WIDTH, CANVAS_HEIGHT, \
                 clear_canvas, click_left, click_right, close_figure, add_vertex, cut_off

def main():
    window = Tk()
    window.title("Лабораторная работа №9")
    window.geometry("%dx%d" %(WINDOW_WIDTH, WINDOW_HEIGHT))
    window.resizable(False, False)
    window["bg"] = "#e0e0eb"

    canvas = Canvas(window, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "white")
    canvas.place(x = 0, y = 0)

    figure = []
    cutter = []

    Label(text = "ЦВЕТ ОТСЕКАТЕЛЯ", font = ("Arial", 16, "bold"), bg = "#7575a3",
        fg = "white").place(width = 305, height = 25, x = CANVAS_WIDTH + 5, y = 0)

    color_cut_var = IntVar()
    color_cut_var.set(2)

    Radiobutton(text = "Чёрный", variable = color_cut_var, value = 0,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 20, y = 30)

    Radiobutton(text = "Красный", variable = color_cut_var, value = 1,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 112010, height = 20, x = CANVAS_WIDTH + 20, y = 50)

    Radiobutton(text = "Синий", variable = color_cut_var, value = 2,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 20, y = 70)

    Radiobutton(text = "Зелёный", variable = color_cut_var, value = 3,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 180, y = 30)

    Radiobutton(text = "Жёлтый", variable = color_cut_var, value = 4,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 180, y = 50)

    Radiobutton(text = "Фиолетовый", variable = color_cut_var, value = 5,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 180, y = 70)



    Label(text = "ЦВЕТ ФИГУРЫ", font = ("Arial", 16, "bold"), bg = "#7575a3",
        fg = "white").place(width = 305, height = 25, x = CANVAS_WIDTH + 5, y = 95)

    color_fig_var = IntVar()
    color_fig_var.set(3)

    Radiobutton(text = "Чёрный", variable = color_fig_var, value = 0,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 20, y = 125)

    Radiobutton(text = "Красный", variable = color_fig_var, value = 1,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 112010, height = 20, x = CANVAS_WIDTH + 20, y = 145)

    Radiobutton(text = "Синий", variable = color_fig_var, value = 2,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 20, y = 165)

    Radiobutton(text = "Зелёный", variable = color_fig_var, value = 3,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 180, y = 125)

    Radiobutton(text = "Жёлтый", variable = color_fig_var, value = 4,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 180, y = 145)

    Radiobutton(text = "Фиолетовый", variable = color_fig_var, value = 5,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 180, y = 165)



    Label(text = "ЦВЕТ РЕЗУЛЬТАТА", font = ("Arial", 16, "bold"), bg = "#7575a3",
        fg = "white").place(width = 305, height = 25, x = CANVAS_WIDTH + 5, y = 190)

    color_res_var = IntVar()
    color_res_var.set(1)

    Radiobutton(text = "Чёрный", variable = color_res_var, value = 0,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 20, y = 220)

    Radiobutton(text = "Красный", variable = color_res_var, value = 1,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 112010, height = 20, x = CANVAS_WIDTH + 20, y = 240)

    Radiobutton(text = "Синий", variable = color_res_var, value = 2,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 20, y = 260)

    Radiobutton(text = "Зелёный", variable = color_res_var, value = 3,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 180, y = 220)

    Radiobutton(text = "Жёлтый", variable = color_res_var, value = 4,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 180, y = 240)

    Radiobutton(text = "Фиолетовый", variable = color_res_var, value = 5,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 180, y = 260)



    Label(text = "ПОСТР. ВЕРШИНЫ ФИГУРЫ", font = ("Arial", 16, "bold"), bg = "#7575a3",
        fg = "white").place(width = 305, height = 25, x = CANVAS_WIDTH + 5, y = 285)

    Label(text = "X\t\tY", font = ("Arial", 16), bg = "#e0e0eb",
        fg = "#29293d").place(width = 268, height = 20, x = CANVAS_WIDTH + 25, y = 320)

    x_fig_entry = Entry(font = ("Arial", 16))
    x_fig_entry.place(width = 134, height = 30, x = CANVAS_WIDTH + 25, y = 345)

    y_fig_entry = Entry(font = ("Arial", 16))
    y_fig_entry.place(width = 134, height = 30, x = CANVAS_WIDTH + 159, y = 345)

    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 268, height = 30,  x = CANVAS_WIDTH + 25, y = 385)

    Button(text = "Постр. вершину фигуры", font = ("Arial", 16), 
        highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
        command = lambda: 
        add_vertex(cutter, figure, canvas, color_fig_var, color_cut_var, x_fig_entry, y_fig_entry)).\
        place(width = 264, height = 26,  x = CANVAS_WIDTH + 27, y = 387)
    
    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 268, height = 30,  x = CANVAS_WIDTH + 25, y = 420)

    Button(text = "Замкнуть фигуру", font = ("Arial", 16), 
        highlightbackground = "#d1d1e0", highlightthickness = 30, fg = "#33334d",
        command = lambda: close_figure(figure, canvas, color_fig_var, fig_str = "Фигура должна")).\
        place(width = 264, height = 26,  x = CANVAS_WIDTH + 27, y = 422)



    Label(text = "ПОСТР. ВЕРШИНЫ ОТСЕКАТЕЛЯ", font = ("Arial", 16, "bold"), bg = "#7575a3",
        fg = "white").place(width = 305, height = 25, x = CANVAS_WIDTH + 5, y = 460)

    Label(text = "X\t\tY", font = ("Arial", 16), bg = "#e0e0eb",
        fg = "#29293d").place(width = 268, height = 20, x = CANVAS_WIDTH + 25, y = 495)

    x_cut_entry = Entry(font = ("Arial", 16))
    x_cut_entry.place(width = 134, height = 30, x = CANVAS_WIDTH + 25, y = 520)

    y_cut_entry = Entry(font = ("Arial", 16))
    y_cut_entry.place(width = 134, height = 30, x = CANVAS_WIDTH + 159, y = 520)

    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 268, height = 30,  x = CANVAS_WIDTH + 25, y = 560)

    Button(text = "Постр. вершину отсекателя", font = ("Arial", 16), 
        highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
        command = lambda: 
        add_vertex(figure, cutter, canvas, color_cut_var, color_fig_var, x_cut_entry, y_cut_entry)).\
        place(width = 264, height = 26,  x = CANVAS_WIDTH + 27, y = 562)
    
    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 268, height = 30,  x = CANVAS_WIDTH + 25, y = 595)

    Button(text = "Замкнуть отсекатель", font = ("Arial", 16), 
        highlightbackground = "#d1d1e0", highlightthickness = 30, fg = "#33334d",
        command = lambda: close_figure(cutter, canvas, color_cut_var, fig_str = "Отсекатель должен")).\
        place(width = 264, height = 26,  x = CANVAS_WIDTH + 27, y = 597)



    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 268, height = 40,  x = CANVAS_WIDTH + 25, y = 635)

    Button(text = "Отсечь", font = ("Arial", 16), 
        highlightbackground = "#d1d1e0", highlightthickness = 30, fg = "#33334d",
        command = lambda: cut_off(cutter, figure, canvas, color_res_var)).\
        place(width = 264, height = 36,  x = CANVAS_WIDTH + 27, y = 637)

    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 268, height = 40,  x = CANVAS_WIDTH + 25, y = 680)

    Button(text = "Очистить экран", font = ("Arial", 16), 
        highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
        command = lambda: clear_canvas(canvas, figure, cutter)).\
        place(width = 264, height = 36,  x = CANVAS_WIDTH + 27, y = 682)


    canvas.bind('<1>', 
        lambda event: click_left(event, cutter, figure, canvas, color_fig_var, color_cut_var))
    canvas.bind('<2>', 
        lambda event: click_right(event, figure, cutter, canvas, color_cut_var, color_fig_var))

    x_fig_entry.insert(0, 100)
    y_fig_entry.insert(0, 200)

    x_cut_entry.insert(0, 200)
    y_cut_entry.insert(0, 100)
    
    window.mainloop()

if __name__ == "__main__":
    main()
