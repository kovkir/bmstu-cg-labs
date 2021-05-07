from tkinter import Tk, ttk, messagebox, Radiobutton, Canvas, Label, Entry, Button, \
                    PhotoImage, DISABLED, IntVar, BooleanVar, Listbox, Scrollbar
from draw import WINDOW_HEIGHT, WINDOW_WIDTH, CANVAS_WIDTH, CANVAS_HEIGHT, \
                 clear_canvas, click_left, click_right, click_centre, draw_point, fill_figure
                 
def main():
    window = Tk()
    window.title("Лабораторная работа №6")
    window.geometry("%dx%d" %(WINDOW_WIDTH, WINDOW_HEIGHT))
    window.resizable(False, False)
    window["bg"] = "#e0e0eb"

    canvas = Canvas(window, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "white")
    canvas.place(x = 0, y = 0)

    figures = [[[]]]

    Label(text = "ЦВЕТ ЗАКРАСКИ", font = ("Arial", 16, "bold"), bg = "#7575a3",
        fg = "white").place(width = 305, height = 30, x = CANVAS_WIDTH + 5, y = 10)

    color_var = IntVar()
    color_var.set(3)

    Radiobutton(text = "Чёрный", variable = color_var, value = 0,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 20, y = 50)

    Radiobutton(text = "Красный", variable = color_var, value = 1,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 112010, height = 20, x = CANVAS_WIDTH + 20, y = 70)

    Radiobutton(text = "Синий", variable = color_var, value = 2,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 20, y = 90)

    Radiobutton(text = "Зелёный", variable = color_var, value = 3,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 180, y = 50)

    Radiobutton(text = "Жёлтый", variable = color_var, value = 4,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 180, y = 70)

    Radiobutton(text = "Фиолетовый", variable = color_var, value = 5,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 120, height = 20, x = CANVAS_WIDTH + 180, y = 90)


    Label(text = "РЕЖИМ ЗАКРАСКИ", font = ("Arial", 16, "bold"), bg = "#7575a3",
        fg = "white").place(width = 305, height = 30, x = CANVAS_WIDTH + 5, y = 120)

    mode_var = BooleanVar()
    mode_var.set(1)

    Radiobutton(text = "Без задержки", variable = mode_var, value = 0,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 250, height = 20, x = CANVAS_WIDTH + 20, y = 160)

    Radiobutton(text = "С задержкой", variable = mode_var, value = 1,
        font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d", anchor = "w").\
        place(width = 280, height = 20, x = CANVAS_WIDTH + 180, y = 160)


    Label(text = "ПОСТРОЕНИЕ ТОЧКИ", font = ("Arial", 16, "bold"), bg = "#7575a3",
        fg = "white").place(width = 305, height = 30, x = CANVAS_WIDTH + 5, y = 190)


    Label(text = "X\t\tY", font = ("Arial", 16), bg = "#e0e0eb",
        fg = "#29293d").place(width = 250, height = 20, x = CANVAS_WIDTH + 30, y = 230)

    x_entry = Entry(font = ("Arial", 16))
    x_entry.place(width = 125, height = 30, x = CANVAS_WIDTH + 30, y = 250)

    y_entry = Entry(font = ("Arial", 16))
    y_entry.place(width = 125, height = 30, x = CANVAS_WIDTH + 155, y = 250)

    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 250, height = 30,  x = CANVAS_WIDTH + 30, y = 290)

    Button(text = "Построить точку", font = ("Arial", 16), 
        highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
        command = lambda: draw_point(figures, img, color_var, x_entry, y_entry,points_listbox)).\
        place(width = 246, height = 26,  x = CANVAS_WIDTH + 32, y = 292)


    points_listbox = Listbox(font = ("Arial", 16))
    points_listbox.place(width = 250, height = 125, x = CANVAS_WIDTH + 30, y = 330)


    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 250, height = 30,  x = CANVAS_WIDTH + 30, y = 465)

    Button(text = "Замкнуть фигуру", font = ("Arial", 16), 
        highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
        command = lambda event = "<3>": click_centre(event, figures, img, color_var)).\
        place(width = 246, height = 26,  x = CANVAS_WIDTH + 32, y = 467)


    Label(text = "ПОСТРОЕНИЕ С ПОМОЩЬЮ МЫШИ",
          font = ("Arial", 16, "bold"), bg = "#7575a3", fg = "white").\
          place(width = 305, height = 30, x = CANVAS_WIDTH + 5, y = 505)

    Label(text = "Левая кнопка - добавить точку",
          font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d").\
          place(height = 25, x = CANVAS_WIDTH + 30, y = 545)

    Label(text = "Правая кнопка - добавить затравку",
          font = ("Arial", 16), bg = "#e0e0eb", fg = "#29293d").\
          place(height = 25, x = CANVAS_WIDTH + 30, y = 570)


    Label(text = "Время закраски:", font = ("Arial", 16), bg = "#e0e0eb",
        fg = "#29293d").place(width = 125, height = 30, x = CANVAS_WIDTH + 30, y = 605)

    time_entry = Entry(font = ("Arial", 16))
    time_entry.place(width = 120, height = 30, x = CANVAS_WIDTH + 160, y = 605)


    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 250, height = 35,  x = CANVAS_WIDTH + 30, y = 645)

    Button(text = "Выполнить закраску", font = ("Arial", 16), 
        highlightbackground = "#d1d1e0", highlightthickness = 30, fg = "#33334d",
        command = lambda: fill_figure(figures, img, canvas, color_var, mode_var, time_entry, seed_pixel)).\
        place(width = 246, height = 31,  x = CANVAS_WIDTH + 32, y = 647)

    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 250, height = 35,  x = CANVAS_WIDTH + 30, y = 690)

    Button(text = "Очистить экран", font = ("Arial", 16), 
        highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
        command = lambda: clear_canvas(img, canvas, figures, time_entry, points_listbox, seed_pixel)).\
        place(width = 246, height = 31,  x = CANVAS_WIDTH + 32, y = 692)

    img = PhotoImage(width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
    canvas.create_image(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, image = img, state='normal')
    
    seed_pixel = [-1, -1]

    canvas.bind('<1>', 
        lambda event: click_left(event, figures, img, color_var, points_listbox))
    canvas.bind('<3>', 
        lambda event: click_centre(event, figures, img, color_var))
    canvas.bind('<2>', 
        lambda event: click_right(event, seed_pixel, img, color_var, points_listbox))

    x_entry.insert(0, 100)
    y_entry.insert(0, 100)
    
    window.mainloop()

if __name__ == "__main__":
    main()
