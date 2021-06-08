from tkinter import Tk, Radiobutton, Canvas, Label, Entry, Button, DISABLED, IntVar
from draw import WINDOW_HEIGHT, WINDOW_WIDTH, CANVAS_WIDTH, CANVAS_HEIGHT, \
                 clear_canvas, click_left, click_right, click_centre, \
                 add_line, add_vertex_figure, cut_off

def main():
    window = Tk()
    window.title("Лабораторная работа №8")
    window.geometry("%dx%d" %(WINDOW_WIDTH, WINDOW_HEIGHT))
    window.resizable(False, False)
    window["bg"] = "#e0e0eb"

    canvas = Canvas(window, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "white")
    canvas.place(x = 0, y = 0)

    lines = [[]]
    cutter_figure = []

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



    Label(text = "ЦВЕТ ОТРЕЗКА", font = ("Arial", 16, "bold"), bg = "#7575a3",
        fg = "white").place(width = 305, height = 25, x = CANVAS_WIDTH + 5, y = 95)

    color_line_var = IntVar()
    color_line_var.set(3)

    Radiobutton(text = "Чёрный", variable = color_line_var, value = 0,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 20, y = 125)

    Radiobutton(text = "Красный", variable = color_line_var, value = 1,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 112010, height = 20, x = CANVAS_WIDTH + 20, y = 145)

    Radiobutton(text = "Синий", variable = color_line_var, value = 2,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 20, y = 165)

    Radiobutton(text = "Зелёный", variable = color_line_var, value = 3,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 180, y = 125)

    Radiobutton(text = "Жёлтый", variable = color_line_var, value = 4,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 180, y = 145)

    Radiobutton(text = "Фиолетовый", variable = color_line_var, value = 5,
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



    Label(text = "ПОСТРОЕНИЕ ОТРЕЗКА", font = ("Arial", 16, "bold"), bg = "#7575a3",
        fg = "white").place(width = 305, height = 25, x = CANVAS_WIDTH + 5, y = 285)

    Label(text = "Xн\tYн\tXк\tYк", font = ("Arial", 16), bg = "#e0e0eb",
        fg = "#29293d").place(width = 268, height = 20, x = CANVAS_WIDTH + 25, y = 320)

    xb_entry = Entry(font = ("Arial", 16))
    xb_entry.place(width = 67, height = 30, x = CANVAS_WIDTH + 25, y = 345)

    yb_entry = Entry(font = ("Arial", 16))
    yb_entry.place(width = 67, height = 30, x = CANVAS_WIDTH + 92, y = 345)

    xe_entry = Entry(font = ("Arial", 16))
    xe_entry.place(width = 67, height = 30, x = CANVAS_WIDTH + 159, y = 345)

    ye_entry = Entry(font = ("Arial", 16))
    ye_entry.place(width = 67, height = 30, x = CANVAS_WIDTH + 226, y = 345)

    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 268, height = 30,  x = CANVAS_WIDTH + 25, y = 385)

    Button(text = "Построить отрезок", font = ("Arial", 16), 
        highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
        command = lambda: add_line(lines, canvas, color_line_var, 
                                   xb_entry, yb_entry, xe_entry, ye_entry)).\
        place(width = 264, height = 26,  x = CANVAS_WIDTH + 27, y = 387)



    Label(text = "ПОСТР. ВЕРШИНЫ ОТСЕКАТЕЛЯ", font = ("Arial", 16, "bold"), bg = "#7575a3",
        fg = "white").place(width = 305, height = 25, x = CANVAS_WIDTH + 5, y = 425)

    Label(text = "X\t\tY", font = ("Arial", 16), bg = "#e0e0eb",
        fg = "#29293d").place(width = 268, height = 20, x = CANVAS_WIDTH + 25, y = 460)

    x_cut_entry = Entry(font = ("Arial", 16))
    x_cut_entry.place(width = 134, height = 30, x = CANVAS_WIDTH + 25, y = 485)

    y_cut_entry = Entry(font = ("Arial", 16))
    y_cut_entry.place(width = 134, height = 30, x = CANVAS_WIDTH + 159, y = 485)

    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 268, height = 30,  x = CANVAS_WIDTH + 25, y = 525)

    Button(text = "Постр. вершину отсекателя", font = ("Arial", 16), 
        highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
        command = lambda: 
        add_vertex_figure(lines, cutter_figure, canvas, color_cut_var, x_cut_entry, y_cut_entry)).\
        place(width = 264, height = 26,  x = CANVAS_WIDTH + 27, y = 527)
    


    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 268, height = 45,  x = CANVAS_WIDTH + 25, y = 570)

    Button(text = "Замкнуть отсекатель", font = ("Arial", 16), 
        highlightbackground = "#d1d1e0", highlightthickness = 30, fg = "#33334d",
        command = lambda event = '<3>': 
        click_centre(event, cutter_figure, canvas, color_cut_var)).\
        place(width = 264, height = 41,  x = CANVAS_WIDTH + 27, y = 572)

    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 268, height = 45,  x = CANVAS_WIDTH + 25, y = 625)

    Button(text = "Отсечь", font = ("Arial", 16), 
        highlightbackground = "#d1d1e0", highlightthickness = 30, fg = "#33334d",
        command = lambda: cut_off(cutter_figure, lines, canvas, color_cut_var, color_res_var)).\
        place(width = 264, height = 41,  x = CANVAS_WIDTH + 27, y = 627)

    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 268, height = 45,  x = CANVAS_WIDTH + 25, y = 680)

    Button(text = "Очистить экран", font = ("Arial", 16), 
        highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
        command = lambda: clear_canvas(canvas, lines, cutter_figure)).\
        place(width = 264, height = 41,  x = CANVAS_WIDTH + 27, y = 682)


    canvas.bind('<1>', 
        lambda event: click_left(event, lines, canvas, color_line_var))
    canvas.bind('<2>', 
        lambda event: click_right(event, lines, cutter_figure, canvas, color_cut_var))
    canvas.bind('<3>',
        lambda event: click_centre(event, cutter_figure, canvas, color_cut_var))

    xb_entry.insert(0, 100)
    yb_entry.insert(0, 200)

    xe_entry.insert(0, 800)
    ye_entry.insert(0, 500)

    x_cut_entry.insert(0, 200)
    y_cut_entry.insert(0, 100)
    
    window.mainloop()

if __name__ == "__main__":
    main()
