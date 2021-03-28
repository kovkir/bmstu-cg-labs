'''
На плоскости дано множество точек.
Найти такой треугольник с вершинами в этих точках, 
у которого разность площадей треугольника и вписанного круга максимальна.
'''

from math import pi, sqrt
from tkinter import Tk, Canvas, Label, Entry, Button, DISABLED, messagebox

WINDOW_WIDTH = 1105
WINDOW_HEIGHT = 630

CANVAS_WIDTH = WINDOW_WIDTH - 280
CANVAS_HEIGHT = WINDOW_HEIGHT - 120

EPS = 1e-6

def read_point(field_x, index):
    string = field_x.get()

    try:
        x = float(string)
    except:
        messagebox.showwarning("Ошибка",
             "Неверно введены координаты точки №%d!\n"
             "Ожидался ввод двух действительных чисел." %(index + 1))
        return 1, 0

    return 0, x

def tranc_coord(y):
    return (-1) * y + CANVAS_HEIGHT

def tranc_coord_back(y):
    return (CANVAS_HEIGHT - y)

def search_coef_scaling():
    x_min = point_coord[0][0]
    y_min = point_coord[0][1]

    x_max = point_coord[0][0]
    y_max = point_coord[0][1]

    for i in point_coord:
        x_min = min(i[0], x_min)
        y_min = max(i[1], y_min)

        x_max = max(i[0], x_max)
        y_max = min(i[1], y_max)

    y_min = tranc_coord_back(y_min)
    y_max = tranc_coord_back(y_max)

    if x_max != x_min:
        k_x = (0.8 * CANVAS_WIDTH) / (x_max - x_min)
    else:
        k_x = 0

    if y_max != y_min:
        k_y = (0.8 * CANVAS_HEIGHT) / (y_max - y_min)
    else:
        k_y = 0

    return k_x, k_y, x_min, y_min

def build_points():
    point_coord.clear()
    new_point_coord.clear()
    canvas.delete("all")

    if numb_points == 0:
        messagebox.showwarning("Ошибка",
            "Для начала работы необходимо задать кол-во точек!")
        return 1

    for i in range(numb_points):
        r, x = read_point(point_list[i][1], i)
        if (r):
            return 1
        
        r, y = read_point(point_list[i][2], i)
        if (r):
            return 1

        y = tranc_coord(y)
        point_coord.append([x, y])
    
    k_x, k_y, x_min, y_min = search_coef_scaling()
    
    if k_x != 0 and k_y != 0:
        indent_x = 0.1 * CANVAS_WIDTH
        indent_y = 0.1 * CANVAS_HEIGHT

        k_x = min(k_x, k_y)
        k_y = k_x

    elif k_x == 0 and k_y != 0:
        indent_x = 0.5 * CANVAS_WIDTH
        indent_y = 0.1 * CANVAS_HEIGHT
    elif k_x != 0 and k_y == 0:
        indent_x = 0.1 * CANVAS_WIDTH
        indent_y = 0.5 * CANVAS_HEIGHT
    else:
        indent_x = 0.5 * CANVAS_WIDTH
        indent_y = 0.5 * CANVAS_HEIGHT

    for i in range(numb_points):
        x = (point_coord[i][0] - x_min) * k_x + indent_x
        y = tranc_coord((tranc_coord_back(point_coord[i][1]) - y_min) * k_y + indent_y)
        new_point_coord.append([x, y])

        r = 3.5
        canvas.create_oval(x - r, y - r, x + r, y + r,
                           width = 1, outline = "red", fill = "red")

        canvas.create_text(x, y - 15, 
                           text = "%d [%.1f,%.1f]" %(i + 1, point_coord[i][0], tranc_coord_back(point_coord[i][1])),
                           font = ("Courier New", 16, "bold"), fill = "darkmagenta")

def sides_triangle(triangle):
    x1 = triangle[0][0] 
    y1 = triangle[0][1]
    x2 = triangle[1][0]
    y2 = triangle[1][1]
    x3 = triangle[2][0]
    y3 = triangle[2][1]
    
    ab = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    bc = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    ac = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

    return ab, bc, ac
    
def triangle_check(triangle):
    ab, bc, ac = sides_triangle(triangle)
    
    if ac < ab + bc and bc < ab + ac and ab < bc + ac:
        return 1, ab, bc, ac
    else:
        return 0, 0, 0, 0

def area_difference(ab, bc, ac):
    p = (ab + bc + ac) / 2
    s_tr = sqrt(p * (p - ab) * (p - bc) * (p - ac))

    r = s_tr / p
    s_c = pi * (r ** 2)

    return s_tr - s_c

def radius_inscribed_circle(triangle):    
    ab, bc, ac = sides_triangle(triangle)

    p = (ab + bc + ac) / 2
    s_tr = sqrt(p * (p - ab) * (p - bc) * (p - ac))

    return s_tr / p
    
def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0] * p2[1] - p2[0] * p1[1])

    return A, B, -C

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False

def build_triangle():
    if numb_points == 0:
        messagebox.showwarning("Ошибка",
            "Для начала работы необходимо задать кол-во точек!")
        return
    elif (numb_points < 3):
        messagebox.showwarning("Ошибка",
            "Для построения треугольника необходимо задать не менее 3 точек!")
        return

    r = build_points()
    if (r):
        return

    canvas.delete("all")

    res_triangle = []
    res_area_diff = 0
    
    for i in range(len(point_coord)):
        for j in range(i + 1, len(point_coord)):
            for u in range(j + 1, len(point_coord)):

                triangle = [new_point_coord[i], new_point_coord[j], new_point_coord[u]]
                r, ab, bc, ac = triangle_check(triangle)

                if (r):
                    area_diff = area_difference(ab, bc, ac)

                    if area_diff > res_area_diff:
                        res_triangle = [new_point_coord[i], new_point_coord[j], new_point_coord[u]]
                        res_area_diff = area_diff

                        triangle_points[0] = i
                        triangle_points[1] = j
                        triangle_points[2] = u

    if len(res_triangle) != 0:
        canvas.create_line(res_triangle[0], res_triangle[1], width = 4, fill = "green")
        canvas.create_line(res_triangle[1], res_triangle[2], width = 4, fill = "green")
        canvas.create_line(res_triangle[0], res_triangle[2], width = 4, fill = "green")

        L1 = line(res_triangle[0], res_triangle[1])
        L2 = line(res_triangle[0], res_triangle[2])

        den1 = sqrt(L2[0] ** 2 + L2[1] ** 2)
        den2 = sqrt(L1[0] ** 2 + L1[1] ** 2)

        L12_b = [L1[0] * den1 + L2[0] * den2, 
                 L1[1] * den1 + L2[1] * den2, 
                 L1[2] * den1 + L2[2] * den2]

        L3 = line(res_triangle[0], res_triangle[2])
        L4 = line(res_triangle[1], res_triangle[2])

        den3 = sqrt(L4[0] ** 2 + L4[1] ** 2)
        den4 = sqrt(L3[0] ** 2 + L3[1] ** 2)

        L34_b = [L3[0] * den3 + L4[0] * den4, 
                 L3[1] * den3 + L4[1] * den4, 
                 L3[2] * den3 + L4[2] * den4]

        x, y = intersection(L12_b, L34_b)
        R = radius_inscribed_circle(res_triangle)

        if R > 4:
            R -= 4
            
        canvas.create_oval(x - R, y - R, x + R, y + R, width = 4, outline = "yellow")
    else:
        messagebox.showwarning("Ошибка",
            "Невозможно построить треугольник!")
        return
    
    min_y = min(res_triangle[0][1], res_triangle[1][1], res_triangle[2][1])
    max_y = max(res_triangle[0][1], res_triangle[1][1], res_triangle[2][1])

    for i in range(numb_points):
        x = new_point_coord[i][0]
        y = new_point_coord[i][1]
        r = 3.5
        canvas.create_oval(x - r, y - r, x + r, y + r,
                           width = 1, outline = "red", fill = "red")
        
        for j in range(len(triangle_points)):
            if i != triangle_points[j] and j == len(triangle_points) - 1:
                canvas.create_text(x, y - 15, 
                    text = "%d [%.1f,%.1f]" %(i + 1, point_coord[i][0], tranc_coord_back(point_coord[i][1])),
                    font = ("Courier New", 16, "bold"), fill = "darkmagenta")

            elif i == triangle_points[j]:
                if abs(y - min_y) < EPS:
                    canvas.create_text(x, y - 15, 
                        text = "%d [%.1f,%.1f]" %(i + 1, point_coord[i][0], tranc_coord_back(point_coord[i][1])),
                        font = ("Courier New", 16, "bold"), fill = "darkmagenta")

                elif abs(y - max_y) < EPS:
                    canvas.create_text(x, y + 15, 
                        text = "%d [%.1f,%.1f]" %(i + 1, point_coord[i][0], tranc_coord_back(point_coord[i][1])),
                        font = ("Courier New", 16, "bold"), fill = "darkmagenta")
                
                else:
                    res_triangle.pop(j)
                    res_triangle.sort(key = lambda array: array[1])

                    x_min_y = res_triangle[0][0]
                    x_max_y = res_triangle[1][0]

                    if abs(x - x_min_y) > abs(x - x_max_y):
                        canvas.create_text(x, y - 15, 
                            text = "%d [%.1f,%.1f]" %(i + 1, point_coord[i][0], tranc_coord_back(point_coord[i][1])),
                            font = ("Courier New", 16, "bold"), fill = "darkmagenta")
                    else:
                        canvas.create_text(x, y + 15, 
                            text = "%d [%.1f,%.1f]" %(i + 1, point_coord[i][0], tranc_coord_back(point_coord[i][1])),
                            font = ("Courier New", 16, "bold"), fill = "darkmagenta")
                break


def enter_points(numb_points):
    clear_table()

    for i in range(numb_points):
        point_list[i][0] = Label(window, text = str(i + 1) + ") ", font = ("Courier New", 16))
        point_list[i][0].place(width = 40, height = 30, x = WINDOW_WIDTH - 245, y = 70 + i * 40)

        point_list[i][1] = Entry(window, font = ("Courier New", 16))
        point_list[i][1].place(width = 90, height = 30, x = WINDOW_WIDTH - 215, y = 70 + i * 40)

        point_list[i][2] = Entry(window, font = ("Courier New", 16))
        point_list[i][2].place(width = 90, height = 30, x = WINDOW_WIDTH - 115, y = 70 + i * 40)

def read_numb_points():
    global numb_points
    string = point_txt.get()

    try:
        numb_points = int(string)

        if numb_points < 1 or numb_points > 10:
            messagebox.showwarning("Ошибка",
                "Неверно введено кол-во точек!\n"
                "Ожидался ввод целого числа от 1 до 10.")
            return
    except:
        messagebox.showwarning("Ошибка",
             "Неверно введено кол-во точек!\n"
             "Ожидался ввод целого числа от 1 до 10.")
        return
    
    clear_fields(del_point_txt)
    del_point_txt.insert(0, numb_points)

    enter_points(numb_points)
    point_list[0][1].focus()

def add_point():
    global numb_points, triangle_points

    if numb_points < 10:
        i = numb_points
        numb_points += 1

        point_list[i][0] = Label(window, text = str(i + 1) + ") ", font = ("Courier New", 16))
        point_list[i][0].place(width = 40, height = 30, x = WINDOW_WIDTH - 245, y = 70 + i * 40)

        point_list[i][1] = Entry(window, font = ("Courier New", 16))
        point_list[i][1].place(width = 90, height = 30, x = WINDOW_WIDTH - 215, y = 70 + i * 40)

        point_list[i][2] = Entry(window, font = ("Courier New", 16))
        point_list[i][2].place(width = 90, height = 30, x = WINDOW_WIDTH - 115, y = 70 + i * 40)

        point_list[i][1].focus()

        clear_fields(point_txt)
        point_txt.insert(0, numb_points)
        
        clear_fields(del_point_txt)
        del_point_txt.insert(0, numb_points)

        triangle_points = [-1, -1, -1]
    else:
        messagebox.showinfo("Замечание",
            "Нельзя использовать больше 10 точек!")

def del_point():
    global numb_points, triangle_points

    numb_p = len(point_coord)

    if numb_p == 0:
        messagebox.showwarning("Ошибка", "Нет заданных точек!")
        return

    string = del_point_txt.get()

    try:
        number = int(string)

        if number < 1 or number > numb_p:
            messagebox.showwarning("Ошибка",
                "Неверно введен номер удаляемой точки!\n"
                "Ожидался ввод целова числа от 1 до %d." %(numb_p))
            return
    except:
        messagebox.showwarning("Ошибка",
             "Неверно введён номер точки!\n"
             "Ожидался ввод целова числа от 1 до %d." %(numb_p))
        return

    points_str_array = []

    for i in range(numb_points):
        if i + 1 != number:
            points_str_array.append([point_list[i][1].get(), point_list[i][2].get()])

    numb_points -= 1
    
    clear_table()
    enter_points(numb_points)

    point_coord.pop(number - 1)
    new_point_coord.pop(number - 1)

    for i in range(numb_points):
        point_list[i][1].insert(0, points_str_array[i][0])
        point_list[i][2].insert(0, points_str_array[i][1])

    clear_fields(point_txt)
    point_txt.insert(0, numb_points)
        
    clear_fields(del_point_txt)
    del_point_txt.insert(0, numb_points)

    triangle_points = [-1, -1, -1]

def display_results():
    if triangle_points[0] == -1:
        messagebox.showwarning("Ошибка",
             "Перед выводом результатов необходимо построить треугольник!")
        return

    triangle = [[point_coord[triangle_points[0]][0], tranc_coord_back(point_coord[triangle_points[0]][1])],
                [point_coord[triangle_points[1]][0], tranc_coord_back(point_coord[triangle_points[1]][1])],
                [point_coord[triangle_points[2]][0], tranc_coord_back(point_coord[triangle_points[2]][1])]]

    ab, bc, ac = sides_triangle(triangle)
    area_dif = area_difference(ab, bc, ac)

    print(triangle_points)

    messagebox.showinfo("Результаты работы программы",
        "Условие задачи:\n\tНа плоскости дано множество точек. "
        "Найти такой треугольник с вершинами в этих точках, "
        "у которого разность площадей треугольника и вписанного круга максимальна.\n\n"
        
        "\t\tРезультаты вычислений\n\n"
        "Вершины треугольника:\n\t%2d) [%.2f, %.2f]\n\t%2d) [%.2f, %.2f]\n\t%2d) [%.2f, %.2f]\n\n"
        "Разность площадей = %.2f"
        %(triangle_points[0] + 1, triangle[0][0], triangle[0][1],
          triangle_points[1] + 1, triangle[1][0], triangle[1][1],
          triangle_points[2] + 1, triangle[2][0], triangle[2][1],
          area_dif))

def clear_fields(field):
    string = field.get()
    len_str = len(string)
    
    while len_str >= 1:
        field.delete(len_str - 1)
        len_str -= 1

def clear_table():
    for i in range(10):
        point_list[i][0].place_forget()
        point_list[i][1].place_forget()
        point_list[i][2].place_forget()

def clear_canvas():
    global numb_points, triangle_points

    numb_points = 0
    point_coord.clear()
    new_point_coord.clear()
    triangle_points = [-1, -1, -1]

    clear_fields(point_txt)
    clear_fields(del_point_txt)
    canvas.delete("all")

    for i in range(numb_points):
        clear_fields(point_list[i][1])
        clear_fields(point_list[i][2])

    clear_table()
    Entry(window, font = ("Courier New", 16), bd = 3, state = DISABLED).\
          place(width = 250, height = 420, x = CANVAS_WIDTH + 20, y = 60)
          
    point_txt.focus()

def task():
    messagebox.showinfo("Условие задачи",
        "\tНа плоскости дано множество точек. "
        "Найти такой треугольник с вершинами в этих точках, "
        "у которого разность площадей треугольника и вписанного круга максимальна.")

if __name__ == "__main__":
    window = Tk()
    window.title("Лабораторная работа №1")
    window.geometry("%dx%d" %(WINDOW_WIDTH, WINDOW_HEIGHT))
    window.resizable(False, False)

    canvas = Canvas(window, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "lightgray")
    canvas.place(x = 0, y = 120)

    point_coord = []
    new_point_coord = []
    triangle_points = [-1, -1, -1]
    numb_points = 0

    Label(window, height = 2, text = "Количество точек:",
                font = ("Courier New", 16)).place(x = 10, y = 10)

    point_txt = Entry(window, font = ("Courier New", 16))
    point_txt.place(width = 180, height = 40, x = 205, y = 10)
    point_txt.focus()


    Entry(window, font = ("Courier New", 15), bd = 3, state = DISABLED).\
        place(width = 250, height = 50, x = CANVAS_WIDTH + 20, y = 10)

    Label(window, text = " №     X        Y    ", font = ("Courier New", 18)).\
        place(width = 240, height = 40, x = CANVAS_WIDTH + 25, y = 15)

    Entry(window, font = ("Courier New", 16), bd = 3, state = DISABLED).\
        place(width = 250, height = 420, x = CANVAS_WIDTH + 20, y = 60)

    point_1_lbl = Label(); point_1x_txt = Entry(); point_1y_txt = Entry()
    point_2_lbl = Label(); point_2x_txt = Entry(); point_2y_txt = Entry()
    point_3_lbl = Label(); point_3x_txt = Entry(); point_3y_txt = Entry()
    point_4_lbl = Label(); point_4x_txt = Entry(); point_4y_txt = Entry()
    point_5_lbl = Label(); point_5x_txt = Entry(); point_5y_txt = Entry()
    point_6_lbl = Label(); point_6x_txt = Entry(); point_6y_txt = Entry()
    point_7_lbl = Label(); point_7x_txt = Entry(); point_7y_txt = Entry()
    point_8_lbl = Label(); point_8x_txt = Entry(); point_8y_txt = Entry()
    point_9_lbl = Label(); point_9x_txt = Entry(); point_9y_txt = Entry()
    point_10_lbl = Label(); point_10x_txt = Entry(); point_10y_txt = Entry()

    point_list = [[point_1_lbl, point_1x_txt, point_1y_txt],
                  [point_2_lbl, point_2x_txt, point_2y_txt],
                  [point_3_lbl, point_3x_txt, point_3y_txt],
                  [point_4_lbl, point_4x_txt, point_4y_txt],
                  [point_5_lbl, point_5x_txt, point_5y_txt],
                  [point_6_lbl, point_6x_txt, point_6y_txt],
                  [point_7_lbl, point_7x_txt, point_7y_txt],
                  [point_8_lbl, point_8x_txt, point_8y_txt],
                  [point_9_lbl, point_9x_txt, point_9y_txt],
                  [point_10_lbl, point_10x_txt, point_10y_txt]]

    Label(window, text = "№ удаляемой точки:", font = ("Courier New", 15)).\
        place(height = 50,  x = CANVAS_WIDTH + 20, y = 535)

    del_point_txt = Entry(window, font = ("Courier New", 15))
    del_point_txt.place(width = 250, height = 40, x = CANVAS_WIDTH + 20, y = 575)


    Button(text = "Ввести точки", font = ("Courier New", 15), command = read_numb_points).\
        place(width = 180, height = 40, x = 400, y = 10)

    Button(text = "Очистить все поля", font = ("Courier New", 15), command = clear_canvas).\
        place(width = 180, height = 40, x = 400, y = 60)

    Button(text = "Построить точки", font = ("Courier New", 15), command = build_points).\
        place(width = 230, height = 40, x = 595, y = 10)

    Button(text = "Построить треугольник", font = ("Courier New", 15), command = build_triangle).\
        place(width = 230, height = 40, x = 595, y = 60)

    Button(text = "Вывести результаты", font = ("Courier New", 15), command = display_results).\
        place(width = 180, height = 40, x = 205, y = 60)

    Button(text = "Условие задачи", font = ("Courier New", 15), command = task).\
        place(width = 180, height = 40, x = 10, y = 60)

    Button(text = "Добавить\nточку", font = ("Courier New", 15), command = add_point).\
        place(width = 120, height = 50,  x = CANVAS_WIDTH + 20, y = 490)

    Button(text = "Удалить\nточку", font = ("Courier New", 15), command = del_point).\
        place(width = 120, height = 50,  x = CANVAS_WIDTH + 150, y = 490)

    window.mainloop()
