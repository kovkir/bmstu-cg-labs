from tkinter import messagebox, END
from time import time

from brezenham import bresenham_int

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 740

CANVAS_WIDTH = WINDOW_WIDTH - 310
CANVAS_HEIGHT = WINDOW_HEIGHT

index_point = 0

def clear_canvas(img, canvas, figures, time_entry, points_listbox, seed_pixel):
    global index_point

    img.put("#ffffff", to = (0, 0, CANVAS_WIDTH, CANVAS_HEIGHT))
    
    seed_pixel[0] = -1
    seed_pixel[1] = -1
    index_point = 0

    points_listbox.delete(0, END)
    time_entry.delete(0, END)

    figures.clear()
    figures.append([[]])

def set_pixel(img, x, y, color):
    img.put(color, (x, y))

def draw_line(img, points):
    for i in points:
        set_pixel(img, i[0], i[1], i[2])

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
        color = "#ffd333"
    else:
        color = "#bd08fc"
    
    return color

def click_left(event, figures, img, color_var, points_listbox):
    global index_point

    x = event.x
    y = event.y

    color = "#ff8000"
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

def click_centre(event, figures, img, color_var):
    if len(figures[-1][-1]) == 0:
        messagebox.showwarning("Ошибка", "Незамкнутых фигур нет!")
        return
    
    if len(figures[-1]) <= 2:
        messagebox.showwarning("Ошибка", "Фигура должна иметь больше 1 ребра!")
        return

    point = figures[-1][0][0]
    figures[-1][-1].append(point)

    color = "#ff8000"

    points = bresenham_int(figures[-1][-1][0], figures[-1][-1][1], color)
    draw_line(img, points)

    figures[-1][-1].append(points)
    figures.append([[]])

def click_right(event, seed_pixel, img, color_var, points_listbox):
    x = event.x
    y = event.y

    seed_pixel[0] = x
    seed_pixel[1] = y

    color = get_color(color_var)
    set_pixel(img, x, y, color)

    pstr = "seed pixel = (%d, %d)" %(x, y)
    points_listbox.insert(END, pstr)

def draw_point(figures, img, color_var, x_entry, y_entry, points_listbox):
    global index_point

    try:
        x = int(x_entry.get())
        y = int(y_entry.get())
    except:
        messagebox.showwarning("Ошибка", 
            "Неверно заданны координаты точки!\n"
            "Ожидался ввод целых чисел.")
        return

    color = "#ff8000"
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

def fill_figure(figures, img, canvas, color_var, mode_var, time_entry, seed_pixel):
    if len(figures[-1][0]) != 0:
        messagebox.showwarning("Ошибка", "Не все фигуры замкнуты!")
        return

    if seed_pixel == [-1, -1]:
        messagebox.showwarning("Ошибка", "Отсутствует затравка!")
        return
        
    mark_color = get_color(color_var)
    border_color = rgb("#ff8000")
    delay = mode_var.get()

    start_time = time()
    method_with_seed(img, canvas, seed_pixel, mark_color, border_color, delay)
    end_time = time()

    time_str = str(round(end_time - start_time, 2)) + "s"
    time_entry.delete(0, END)
    time_entry.insert(0, time_str)

def method_with_seed(img, canvas, seed_pixel, mark_color, border_color_rgb, delay):
    mark_color_rgb = rgb(mark_color)

    stack = [seed_pixel]
    
    while(len(stack)):
        
        seed_pixel = stack.pop()

        x = seed_pixel[0]
        y = seed_pixel[1]

        set_pixel(img, x, y, mark_color)
        x_tmp = x
        y_tmp = y

        #заполняем интервал справа от затравки

        x += 1
        while img.get(x, y) != mark_color_rgb and \
              img.get(x, y) != border_color_rgb and x < CANVAS_WIDTH:

            set_pixel(img, x, y, mark_color)
            x += 1

        x_right = x - 1

        #заполняем интервал слева от затравки

        x = x_tmp - 1
        while img.get(x, y) != mark_color_rgb and \
              img.get(x, y) != border_color_rgb and x > 0:

            set_pixel(img, x, y, mark_color)
            x -= 1

        x_left = x + 1

        # Проход по верхней строке

        x = x_left
        y = y_tmp + 1

        while x <= x_right:
            flag = False

            while img.get(x, y) != mark_color_rgb and \
                  img.get(x, y) != border_color_rgb and x <= x_right:

                flag = True
                x += 1

            # Помещаем в стек крайний справа пиксель

            if flag:
                if x == x_right and img.get(x, y) != mark_color_rgb and \
                                    img.get(x, y) != border_color_rgb:
                    stack.append([x, y])
                else:
                    stack.append([x - 1, y])
            
                flag = False

            # Продолжаем проверку, если интервал был прерван

            x_beg = x
            while (img.get(x, y) == mark_color_rgb or \
                   img.get(x, y) == border_color_rgb) and x < x_right:

                x = x + 1

            if x == x_beg:
                x += 1

        # Проход по нижней строке

        x = x_left
        y = y_tmp - 1

        while x <= x_right:
            flag = False

            while img.get(x, y) != mark_color_rgb and \
                  img.get(x, y) != border_color_rgb and x <= x_right:

                flag = True
                x += 1

            # Помещаем в стек крайний справа пиксель

            if flag:
                if x == x_right and img.get(x, y) != mark_color_rgb and \
                                    img.get(x, y) != border_color_rgb:
                    stack.append([x, y])
                else:
                    stack.append([x - 1, y])
            
                flag = False

            # Продолжаем проверку, если интервал был прерван

            x_beg = x
            while (img.get(x, y) == mark_color_rgb or \
                   img.get(x, y) == border_color_rgb) and x < x_right:

                x = x + 1

            if x == x_beg:
                x += 1
            
        if (delay):
            canvas.update()
