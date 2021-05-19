from tkinter import messagebox, END

from sutherland_cohen import alg_sutherland_cohen

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 740

CANVAS_WIDTH = WINDOW_WIDTH - 310
CANVAS_HEIGHT = WINDOW_HEIGHT

is_set_rectangle = False

def clear_canvas(canvas, lines, rectangle):
    canvas.delete("all")
    
    lines.clear()
    lines.append([])
    
    for i in range(4):
        rectangle[i] = -1

def set_pixel(canvas, x, y, color):
    canvas.create_line(x, y, x + 1, y, fill = color)

def draw_lines(canvas, lines):
    for line in lines:
        if len(line) != 0:
            canvas.create_line(line[0], line[1], fill = line[2])

def rgb(color):
    return (int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16))

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

def click_left(event):
    global is_set_rectangle

    is_set_rectangle = False

def click_left_motion(event, rectangle, lines, canvas, color_var):
    global is_set_rectangle

    color = get_color(color_var)

    if is_set_rectangle == False:
        rectangle[0] = event.x
        rectangle[1] = event.y

        is_set_rectangle = True
    else:
        x = event.x
        y = event.y

        canvas.delete("all")
        draw_lines(canvas, lines)
        canvas.create_rectangle(rectangle[0], rectangle[1], x, y, outline = color)

        rectangle[2] = x
        rectangle[3] = y

def click_right(event, lines, canvas, color_var):
    x = event.x
    y = event.y

    color = get_color(color_var)
    set_pixel(canvas, x, y, color)

    lines[-1].append([x, y])

    if len(lines[-1]) == 2:
        canvas.create_line(lines[-1][0], lines[-1][1], fill = color)

        lines[-1].append(color)
        lines.append([])

def add_line(lines, canvas, color_var, xb_entry, yb_entry, xe_entry, ye_entry):
    if len(lines[-1]) != 0:
        messagebox.showwarning("Ошибка", 
            "Предыдущий отрезок не был достроен!\n")
        return

    try:
        xb = int(xb_entry.get())
        yb = int(yb_entry.get())
        xe = int(xe_entry.get())
        ye = int(ye_entry.get())
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно заданны координаты границ отрезка!\n"
            "Ожидался ввод целых чисел.")
        return

    color = get_color(color_var)

    canvas.create_line([xb, yb], [xe, ye], fill = color)

    lines[-1].append([xb, yb])
    lines[-1].append([xe, ye])
    lines[-1].append(color)
    lines.append([])

def draw_rectangle(rectangle, lines, canvas, color_var, x_top_left_entry, y_top_left_entry,
                   x_lower_right_entry, y_lower_right_entry):
    try:
        xl = int(x_top_left_entry.get())
        yl = int(y_top_left_entry.get())
        xr = int(x_lower_right_entry.get())
        yr = int(y_lower_right_entry.get())
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно заданны координаты вершин прямоугольника!\n"
            "Ожидался ввод целых чисел.")
        return
    
    color = get_color(color_var)

    canvas.delete("all")
    draw_lines(canvas, lines)
    canvas.create_rectangle(xl, yl, xr, yr, outline = color)

    rectangle[0] = xl
    rectangle[1] = yl
    rectangle[2] = xr
    rectangle[3] = yr

def add_vert_horiz_lines(rectangle, lines, canvas, color_var):
    if rectangle[0] == -1:
        messagebox.showerror("Ошибка", "Отсутствует отсекатель")
        return

    color = get_color(color_var)

    x1 = rectangle[0]
    y1 = rectangle[1]
    x2 = rectangle[2]
    y2 = rectangle[3]

    dy = y2 - y1
    dx = x2 - x1

    lines.append([[x1, y1 + 0.1 * dy], [x1, y2 - 0.1 * dy], color])
    lines.append([[x1 + 0.1 * dx, y1], [x2 - 0.1 * dx, y1], color])

    canvas.create_line(x1, y1 + 0.1 * dy, x1, y2 - 0.1 * dy, fill = color)
    canvas.create_line(x1 + 0.1 * dx, y1, x2 - 0.1 * dx, y1, fill = color)

    lines.append([])

def cut_off(rectangle, lines, canvas, color_var):
    if rectangle[0] == -1:
        messagebox.showinfo("Ошибка", "Отсутствует отсекатель")

    rect = [min(rectangle[0], rectangle[2]), max(rectangle[0], rectangle[2]),
            max(rectangle[1], rectangle[3]), min(rectangle[1], rectangle[3])]

    canvas.create_rectangle(rect[0] + 1, rect[3] + 1, rect[1] - 1, rect[2] - 1, 
                            fill = "white", outline = "white")
    
    color = get_color(color_var)
    
    for line in lines:
        if (line):
            alg_sutherland_cohen(rect, line, canvas, color)
