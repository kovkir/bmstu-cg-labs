from tkinter import Tk, Radiobutton, Canvas, Label, Entry, Button, DISABLED, IntVar
from draw import WINDOW_HEIGHT, WINDOW_WIDTH, CANVAS_WIDTH, CANVAS_HEIGHT, \
                 clear_canvas, build_graph, spin_x, spin_y, spin_z, scale_graph

def main():
    window = Tk()
    window.title("Лабораторная работа №10")
    window.geometry("%dx%d" %(WINDOW_WIDTH, WINDOW_HEIGHT))
    window.resizable(False, False)
    window["bg"] = "#e0e0eb"

    canvas = Canvas(window, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "white")
    canvas.place(x = 0, y = 0)



    Label(text = "ЦВЕТ", font = ("Arial", 16, "bold"), bg = "#7575a3",
        fg = "white").place(width = 305, height = 25, x = CANVAS_WIDTH + 5, y = 0)

    color_var = IntVar()
    color_var.set(2)

    Radiobutton(text = "Чёрный", variable = color_var, value = 0,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 20, y = 30)

    Radiobutton(text = "Красный", variable = color_var, value = 1,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 112010, height = 20, x = CANVAS_WIDTH + 20, y = 50)

    Radiobutton(text = "Синий", variable = color_var, value = 2,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 20, y = 70)

    Radiobutton(text = "Зелёный", variable = color_var, value = 3,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 180, y = 30)

    Radiobutton(text = "Жёлтый", variable = color_var, value = 4,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 180, y = 50)

    Radiobutton(text = "Фиолетовый", variable = color_var, value = 5,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 180, y = 70)



    Label(text = "ФУНКЦИЯ", font = ("Arial", 16, "bold"), bg = "#7575a3",
        fg = "white").place(width = 305, height = 25, x = CANVAS_WIDTH + 5, y = 95)

    func_var = IntVar()
    func_var.set(0)

    Radiobutton(text = "sin(x) * cos(z)", variable = func_var, value = 0,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 200, height = 25, x = CANVAS_WIDTH + 80, y = 125)

    Radiobutton(text = "sin(cos(x)) * sin(z)", variable = func_var, value = 1,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 200, height = 25, x = CANVAS_WIDTH + 80, y = 150)

    Radiobutton(text = "cos(x) * z / 4", variable = func_var, value = 2,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 200, height = 25, x = CANVAS_WIDTH + 80, y = 175)

    Radiobutton(text = "cos(x) * cos(sin(z))", variable = func_var, value = 3,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 200, height = 25, x = CANVAS_WIDTH + 80, y = 200)



    Label(text = "ПРЕДЕЛЫ", font = ("Arial", 16, "bold"), bg = "#7575a3",
        fg = "white").place(width = 305, height = 25, x = CANVAS_WIDTH + 5, y = 235)

    Label(text = "Ox", font = ("Arial", 16), bg = "#e0e0eb",
        fg = "#29293d").place(width = 20, height = 25, x = CANVAS_WIDTH + 15, y = 300)

    Label(text = "от\tдо\tшаг", font = ("Arial", 16), bg = "#e0e0eb",
        fg = "#29293d").place(width = 210, height = 20, x = CANVAS_WIDTH + 70, y = 270)

    x_from_entry = Entry(font = ("Arial", 16))
    x_from_entry.place(width = 80, height = 30, x = CANVAS_WIDTH + 50, y = 300)

    x_to_entry = Entry(font = ("Arial", 16))
    x_to_entry.place(width = 80, height = 30, x = CANVAS_WIDTH + 130, y = 300)

    x_step_entry = Entry(font = ("Arial", 16))
    x_step_entry.place(width = 80, height = 30, x = CANVAS_WIDTH + 210, y = 300)

    Label(text = "Oz", font = ("Arial", 16), bg = "#e0e0eb",
        fg = "#29293d").place(width = 20, height = 25, x = CANVAS_WIDTH + 15, y = 340)

    z_from_entry = Entry(font = ("Arial", 16))
    z_from_entry.place(width = 80, height = 30, x = CANVAS_WIDTH + 50, y = 340)

    z_to_entry = Entry(font = ("Arial", 16))
    z_to_entry.place(width = 80, height = 30, x = CANVAS_WIDTH + 130, y = 340)

    z_step_entry = Entry(font = ("Arial", 16))
    z_step_entry.place(width = 80, height = 30, x = CANVAS_WIDTH + 210, y = 340)



    Label(text = "МАСШТАБИРОВАНИЕ", font = ("Arial", 16, "bold"), bg = "#7575a3",
        fg = "white").place(width = 305, height = 25, x = CANVAS_WIDTH + 5, y = 380)

    Label(text = "Коэффициент = ", font = ("Arial", 16), bg = "#e0e0eb",
        fg = "#29293d").place(width = 150, height = 20, x = CANVAS_WIDTH + 40, y = 420)

    scale_entry = Entry(font = ("Arial", 16))
    scale_entry.place(width = 80, height = 30, x = CANVAS_WIDTH + 190, y = 415)
    
    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 268, height = 30,  x = CANVAS_WIDTH + 25, y = 450)

    Button(text = "Масштабировать", font = ("Arial", 16), 
        highlightbackground = "#d1d1e0", highlightthickness = 30, fg = "#33334d",
        command = lambda: scale_graph(
            scale_entry, canvas, color_var, func_var,
            x_from_entry, x_to_entry, x_step_entry,
            z_from_entry, z_to_entry, z_step_entry)).\
        place(width = 264, height = 26,  x = CANVAS_WIDTH + 27, y = 452)



    Label(text = "ВРАЩЕНИЕ", font = ("Arial", 16, "bold"), bg = "#7575a3",
        fg = "white").place(width = 305, height = 25, x = CANVAS_WIDTH + 5, y = 490)

    Label(text = "Ox", font = ("Arial", 16), bg = "#e0e0eb",
        fg = "#29293d").place(width = 25, height = 30, x = CANVAS_WIDTH + 25, y = 525)

    Label(text = "Oy", font = ("Arial", 16), bg = "#e0e0eb",
        fg = "#29293d").place(width = 25, height = 30, x = CANVAS_WIDTH + 25, y = 560)
    
    Label(text = "Oz", font = ("Arial", 16), bg = "#e0e0eb",
        fg = "#29293d").place(width = 25, height = 30, x = CANVAS_WIDTH + 25, y = 595)

    x_spin_entry = Entry(font = ("Arial", 16))
    x_spin_entry.place(width = 80, height = 30, x = CANVAS_WIDTH + 70, y = 525)

    y_spin_entry = Entry(font = ("Arial", 16))
    y_spin_entry.place(width = 80, height = 30, x = CANVAS_WIDTH + 70, y = 560)

    z_spin_entry = Entry(font = ("Arial", 16))
    z_spin_entry.place(width = 80, height = 30, x = CANVAS_WIDTH + 70, y = 595)
    
    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 120, height = 30,  x = CANVAS_WIDTH + 170, y = 525)

    Button(text = "Повернуть", font = ("Arial", 16), 
        highlightbackground = "#d1d1e0", highlightthickness = 30, fg = "#33334d",
        command = lambda: spin_x(
            x_spin_entry, canvas, color_var, func_var,
            x_from_entry, x_to_entry, x_step_entry,
            z_from_entry, z_to_entry, z_step_entry)).\
        place(width = 116, height = 26,  x = CANVAS_WIDTH + 172, y = 527)

    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 120, height = 30,  x = CANVAS_WIDTH + 170, y = 560)

    Button(text = "Повернуть", font = ("Arial", 16), 
        highlightbackground = "#d1d1e0", highlightthickness = 30, fg = "#33334d",
        command = lambda: spin_y(
            y_spin_entry, canvas, color_var, func_var,
            x_from_entry, x_to_entry, x_step_entry,
            z_from_entry, z_to_entry, z_step_entry)).\
        place(width = 116, height = 26,  x = CANVAS_WIDTH + 172, y = 562)

    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 120, height = 30,  x = CANVAS_WIDTH + 170, y = 595)

    Button(text = "Повернуть", font = ("Arial", 16), 
        highlightbackground = "#d1d1e0", highlightthickness = 30, fg = "#33334d",
        command = lambda: spin_z(
            z_spin_entry, canvas, color_var, func_var,
            x_from_entry, x_to_entry, x_step_entry,
            z_from_entry, z_to_entry, z_step_entry)).\
        place(width = 116, height = 26,  x = CANVAS_WIDTH + 172, y = 597)



    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 268, height = 40,  x = CANVAS_WIDTH + 25, y = 635)

    Button(text = "Построить", font = ("Arial", 16), 
        highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
        command = lambda: build_graph(
            canvas, color_var, func_var, 
            x_from_entry, x_to_entry, x_step_entry,
            z_from_entry, z_to_entry, z_step_entry, new_graph = True)).\
        place(width = 264, height = 36,  x = CANVAS_WIDTH + 27, y = 637)

    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 268, height = 40,  x = CANVAS_WIDTH + 25, y = 680)

    Button(text = "Очистить экран", font = ("Arial", 16), 
        highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
        command = lambda: clear_canvas(canvas)).\
        place(width = 264, height = 36,  x = CANVAS_WIDTH + 27, y = 682)


    x_from_entry.insert(0, "-10")
    x_to_entry.insert  (0,  "10")
    x_step_entry.insert(0, "0.2")

    z_from_entry.insert(0, "-10")
    z_to_entry.insert  (0,  "10")
    z_step_entry.insert(0, "0.2")

    scale_entry.insert(0, "43")
    
    x_spin_entry.insert(0, "30")
    y_spin_entry.insert(0, "30")
    z_spin_entry.insert(0, "30")

    window.mainloop()

if __name__ == "__main__":
    main()
