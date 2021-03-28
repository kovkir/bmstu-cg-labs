'''
Нарисовать исходный рисунок, затем осуществить его перенос, масштабирование и поворот.
'''

from tkinter import Tk, ttk, Canvas, Label, Entry, Button, DISABLED, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pylab, patches
import matplotlib.pyplot as plt
import numpy as np
from math import pi, sin, cos, sqrt

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 680

PLOT_WIDTH = WINDOW_WIDTH - 300
PLOT_HEIGHT = WINDOW_HEIGHT

ORIGINAL_VALUE_X = 450
ORIGINAL_VALUE_Y = 340

BODY_WIDTH = 200
BODY_HEIGHT = 100

HEAD_WIDTH = 0.8 * BODY_HEIGHT
EYE_WIDTH = 0.2 * HEAD_WIDTH

NUMB_POINTS = 100

def side(x1, y1, x2, y2):
    '''
    Вычисление длины отрезка по координатам
    '''
    return sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)

def rotation():
    '''
    Поворот изображения на заданный в градусах угол
    '''
    global cat, vers_cat

    try:
        angle_rot = float(angle_rotation.get()) * pi / 180
    except:
        messagebox.showwarning("Ошибка",
             "Неверно задан угол поворота!\n"
             "Ожидался ввод действительного числа (угол задаётся в градусах).")
        return
    
    try:
        xc = float(x_center.get())
        yc = float(y_center.get())
    except:
        messagebox.showwarning("Ошибка",
             "Неверно заданы координаты точки, относительно которой будет производиться "
             "поворот изображения!\n"
             "Ожидался ввод действительных чисел.")
        return

    vers_cat.append(copy_cat(cat))
    M_rot = np.array([[cos(angle_rot) , -sin(angle_rot)], [sin(angle_rot), cos(angle_rot)]])

    for i in range(len(cat)):
        for j in range(len(cat[i])):
            cat[i][j][0] -= xc
            cat[i][j][1] -= yc

            cat[i][j] = np.dot(M_rot, cat[i][j])

            cat[i][j][0] += xc
            cat[i][j][1] += yc
    
    draw_picture()

def movement():
    '''
    Перемещение изображения на dx по Ox и dy по Oy
    '''
    global cat, vers_cat

    try:
        dx = float(dx_movement.get())
    except:
        messagebox.showwarning("Ошибка",
             "Неверно задан Dx!\n"
             "Ожидался ввод действительного числа.")
        return
    
    try:
        dy = float(dy_movement.get())
    except:
        messagebox.showwarning("Ошибка",
             "Неверно задан Dy!\n"
             "Ожидался ввод действительного числа.")
        return

    vers_cat.append(copy_cat(cat))

    for i in range(len(cat)):
        for j in range(len(cat[i])):
            cat[i][j][0] += dx
            cat[i][j][1] += dy

    draw_picture()

def scaling():
    '''
    Масштабирование изображения относительно заданной точки
    '''
    global cat, vers_cat

    try:
        xm = float(x_center.get())
        ym = float(y_center.get())
    except:
        messagebox.showwarning("Ошибка",
             "Неверно заданы координаты точки, относительно которой будет производиться "
             "масштабирование изображения!\n"
             "Ожидался ввод действительных чисел.")
        return
    
    try:
        kx = float(kx_scal.get())
        ky = float(ky_scal.get())
    except:
        messagebox.showwarning("Ошибка",
             "Неверно заданы коэффициенты масштабирования изображения!\n"
             "Ожидался ввод действительных положительных чисел.")
        return

    if kx == 0 or ky == 0:
        messagebox.showwarning("Ошибка",
             "Коэфициенты масштабирования изображения не может равняться 0!")
        return

    vers_cat.append(copy_cat(cat))

    for i in range(len(cat)):
        for j in range(len(cat[i])):
            cat[i][j][0] = kx * (cat[i][j][0] - xm) + xm
            cat[i][j][1] = ky * (cat[i][j][1] - ym) + ym

    draw_picture()

def draw_picture():   
    '''
    Рисование изображения на полотне
    '''
    clear_picture()

    for i in range(len(cat)):
        if i < 4:
            plt.plot([point[0] for point in cat[i]],
                     [point[1] for point in cat[i]], color = 'darkorange')
        else:
            plt.plot([cat[i][0][0], cat[i][1][0]], [cat[i][0][1], cat[i][1][1]], color = 'r')

    plt.text(ORIGINAL_VALUE_X - 35, ORIGINAL_VALUE_Y + 10, 
            "(%d, %d)" %(ORIGINAL_VALUE_X, ORIGINAL_VALUE_Y), color = 'g')
    circal = plt.Circle((ORIGINAL_VALUE_X, ORIGINAL_VALUE_Y), 2.5, color = 'g', fill = True)
    ax.add_patch(circal)

    canvas.draw()

def step_back():
    '''
    Откат на 1 шаг назад
    '''
    global cat, vers_cat

    if len(vers_cat) > 1:
        cat = copy_cat(vers_cat[-1])
        vers_cat.pop(-1)

        draw_picture()
    else:
        messagebox.showwarning("Ошибка",
            "Нельзя откатиться дальше начального состояния!")

def starting_position():
    '''
    Откат до исходного положения
    '''
    global cat, vers_cat
    
    if len(vers_cat) > 1:
        vers_cat = [vers_cat[0]]
        cat = copy_cat(vers_cat[0])

        set_initial_values()
        draw_picture()

def clear_picture():
    '''
    Очищение полотна
    '''
    global ax

    fig.clear()

    ax = fig.add_subplot(111)
    ax.set(facecolor = "#f0f0f5")

    ax.set_xlim([0, PLOT_WIDTH])
    ax.set_ylim([0, PLOT_HEIGHT]) 

    ax.spines["bottom"].set_color("#29293d")
    ax.spines["top"].set_color("#29293d")
    ax.spines["left"].set_color("#29293d")
    ax.spines["right"].set_color("#29293d")

    ax.tick_params(axis = "x", colors = "#29293d")
    ax.tick_params(axis = "y", colors = "#29293d")
    ax.grid(color = "#a3a3c2", linestyle = '--')

    canvas.draw()

def clear_field(field):
    '''
    Очищение поля ввода
    '''
    string = field.get()
    len_str = len(string)
    
    while len_str >= 1:
        field.delete(len_str - 1)
        len_str -= 1

def clear_fields():
    '''
    Очищение всех полей ввода
    '''
    clear_field(x_center)
    clear_field(y_center)
    clear_field(angle_rotation)
    clear_field(dx_movement)
    clear_field(dy_movement)
    clear_field(kx_scal)
    clear_field(ky_scal)

def set_initial_values():
    '''
    Запись в поля ввода исходных значений
    '''
    clear_fields()
    
    x_center.insert(0, ORIGINAL_VALUE_X)
    y_center.insert(0, ORIGINAL_VALUE_Y)

    angle_rotation.insert(0, 0)

    dx_movement.insert(0, 0)
    dy_movement.insert(0, 0)

    kx_scal.insert(0, 1)
    ky_scal.insert(0, 1)

    angle_rotation.focus()

def copy_cat(cat):
    '''
    Копирование трёхмерной матрицы
    '''
    copy_cat = []

    for i in range(len(cat)):
        i_list = []

        for j in range(len(cat[i])):
            j_list = []

            for u in range(len(cat[i][j])):
                j_list.append(cat[i][j][u])
            
            i_list.append(j_list)

        copy_cat.append(i_list)
    
    return copy_cat

def create_cat():
    '''
    Создание трёхмерной матрицы со всеми точками, по которым строится исходный кот
    '''
    angle_rot = np.linspace(0, 2 * pi, NUMB_POINTS)

    x0_body = ORIGINAL_VALUE_X + (BODY_HEIGHT + HEAD_WIDTH) / 4
    y0_body = ORIGINAL_VALUE_Y
    body_array = np.array([x0_body + BODY_WIDTH / 2  * np.cos(angle_rot), 
                           y0_body + BODY_HEIGHT / 2 * np.sin(angle_rot)])
    body = []
    for i in range(len(body_array[0])):
        body.append([body_array[0][i], body_array[1][i]])

    x0_head = x0_body - (BODY_WIDTH + HEAD_WIDTH) / 2
    y0_head = y0_body
    head_array = np.array([x0_head + HEAD_WIDTH / 2 * np.cos(angle_rot), 
                           y0_head + HEAD_WIDTH / 2 * np.sin(angle_rot)])
    head = []
    for i in range(len(head_array[0])):
        head.append([head_array[0][i], head_array[1][i]])

    x0_left_eye = x0_head - HEAD_WIDTH / 5
    y0_left_eye = y0_head + HEAD_WIDTH / 5
    left_eye_array = np.array([x0_left_eye + EYE_WIDTH / 2 * np.cos(angle_rot), 
                               y0_left_eye + EYE_WIDTH / 2 * np.sin(angle_rot)])
    left_eye = []
    for i in range(len(left_eye_array[0])):
        left_eye.append([left_eye_array[0][i], left_eye_array[1][i]])

    x0_right_eye = x0_head + HEAD_WIDTH / 5
    y0_right_eye = y0_head + HEAD_WIDTH / 5
    right_eye_array = np.array([x0_right_eye + EYE_WIDTH / 2 * np.cos(angle_rot), 
                                y0_right_eye + EYE_WIDTH / 2 * np.sin(angle_rot)])
    right_eye = []
    for i in range(len(right_eye_array[0])):
        right_eye.append([right_eye_array[0][i], right_eye_array[1][i]])

    cat = [body, head, left_eye, right_eye]

    x1_mustache = x0_head - HEAD_WIDTH * 2 / 3
    y1_mustache = y0_head - HEAD_WIDTH / 8
    x2_mustache = x0_head + HEAD_WIDTH * 2 / 3
    y2_mustache = y1_mustache
    cat.append([[x1_mustache, y1_mustache], [x2_mustache, y2_mustache]])

    x3_mustache = x1_mustache
    y3_mustache = y1_mustache + HEAD_WIDTH / 4
    x4_mustache = x2_mustache 
    y4_mustache = y2_mustache - HEAD_WIDTH / 4
    cat.append([[x3_mustache, y3_mustache], [x4_mustache, y4_mustache]])

    x5_mustache = x1_mustache
    y5_mustache = y1_mustache - HEAD_WIDTH / 4
    x6_mustache = x2_mustache 
    y6_mustache = y2_mustache + HEAD_WIDTH / 4
    cat.append([[x5_mustache, y5_mustache], [x6_mustache, y6_mustache]])

    x1_left_ear = x0_left_eye - 1 / 2 * EYE_WIDTH
    y1_left_ear = y0_head + HEAD_WIDTH * 2 / 3
    x2_left_ear = sqrt((HEAD_WIDTH / 2) ** 2 - (HEAD_WIDTH / 3) ** 2) * (-1) + x0_head
    y2_left_ear = y0_head + HEAD_WIDTH / 3
    x3_left_ear = sqrt((HEAD_WIDTH / 2) ** 2 - (HEAD_WIDTH * 15 / 31) ** 2) * (-1) + x0_head
    y3_left_ear = y0_head + HEAD_WIDTH * 15 / 31
    cat.append([[x1_left_ear, y1_left_ear], [x2_left_ear, y2_left_ear]])
    cat.append([[x1_left_ear, y1_left_ear], [x3_left_ear, y3_left_ear]])

    x1_right_ear = x0_right_eye + 1 / 2 * EYE_WIDTH
    y1_rifht_ear = y0_head + HEAD_WIDTH * 2 / 3
    x2_right_ear = sqrt((HEAD_WIDTH / 2) ** 2 - (HEAD_WIDTH / 3) ** 2) + x0_head
    y2_right_ear = y0_head + HEAD_WIDTH / 3
    x3_right_ear = sqrt((HEAD_WIDTH / 2) ** 2 - (HEAD_WIDTH * 15 / 31) ** 2) + x0_head
    y3_right_ear = y0_head + HEAD_WIDTH * 15 / 31
    cat.append([[x1_right_ear, y1_rifht_ear], [x2_right_ear, y2_right_ear]])
    cat.append([[x1_right_ear, y1_rifht_ear], [x3_right_ear, y3_right_ear]])        

    x1_left_log = BODY_WIDTH / BODY_HEIGHT * \
                sqrt((BODY_HEIGHT / 2) ** 2 - (BODY_HEIGHT * 7 / 15) ** 2) * (-1) + x0_body
    y1_left_log = y0_body - BODY_HEIGHT * 7 / 15
    x2_left_leg = x1_left_log
    y2_left_leg = y0_body - BODY_HEIGHT * 3 / 4
    x3_left_leg = x2_left_leg - 1 / 9 * BODY_WIDTH
    y3_left_leg = y2_left_leg
    cat.append([[x1_left_log, y1_left_log], [x2_left_leg, y2_left_leg]])
    cat.append([[x2_left_leg, y2_left_leg], [x3_left_leg, y3_left_leg]])

    x1_right_log = BODY_WIDTH / BODY_HEIGHT * \
                sqrt((BODY_HEIGHT / 2) ** 2 - (BODY_HEIGHT * 7 / 15) ** 2) + x0_body
    y1_right_log = y0_body - BODY_HEIGHT * 7 / 15
    x2_right_leg = x1_right_log
    y2_right_leg = y0_body - BODY_HEIGHT * 3 / 4
    x3_right_leg = x2_right_leg + 1 / 9 * BODY_WIDTH
    y3_right_leg = y2_right_leg
    cat.append([[x1_right_log, y1_right_log], [x2_right_leg, y2_right_leg]])
    cat.append([[x2_right_leg, y2_right_leg], [x3_right_leg, y3_right_leg]])

    return cat



if __name__ == "__main__":
    window = Tk()
    window.title("Лабораторная работа №2")
    window.geometry("%dx%d" %(WINDOW_WIDTH, WINDOW_HEIGHT))
    window.resizable(False, False)
    window["bg"] = "#e0e0eb"

    fig = plt.figure()
    ax = fig.add_subplot(111)

    fig.set(facecolor = "#b3b3cc")
    ax.set(facecolor = "#f0f0f5")
    fig.subplots_adjust(right = 0.97, left = 0.06, bottom = 0.06, top = 0.97)

    canvas = FigureCanvasTkAgg(fig, master = window)
    plot = canvas.get_tk_widget()

    ax.set_xlim([0, PLOT_WIDTH])
    ax.set_ylim([0, PLOT_HEIGHT]) 

    ax.spines["bottom"].set_color("#29293d")
    ax.spines["top"].set_color("#29293d")
    ax.spines["left"].set_color("#29293d")
    ax.spines["right"].set_color("#29293d")

    ax.tick_params(axis = "x", colors = "#29293d")
    ax.tick_params(axis = "y", colors = "#29293d")
    ax.grid(color = "#a3a3c2", linestyle = '--')

    plot.place(x = 0, y = 0, width = PLOT_WIDTH, height = PLOT_HEIGHT)



    Label(text = "ЦЕНТР", font = ("Courier New", 22), bg = "#e0e0eb",
        fg = "#33334d").place(width = 240, height = 30, x = PLOT_WIDTH + 30, y = 10)

    Label(text = "(масштабирования и поворота)", font = ("Courier New", 16), bg = "#e0e0eb",
        fg = "#33334d").place(width = 260, height = 20, x = PLOT_WIDTH + 30, y = 40)

    Label(text = "  X \t   Y  ", font = ("Courier New", 19), bg = "#e0e0eb",
        fg = "#33334d").place(width = 240, height = 20, x = PLOT_WIDTH + 30, y = 60)

    x_center = Entry(font = ("Courier New", 19))
    x_center.place(width = 120, height = 35, x = PLOT_WIDTH + 30, y = 85)

    y_center = Entry(font = ("Courier New", 19))
    y_center.place(width = 120, height = 35, x = PLOT_WIDTH + 150, y = 85)

    

    Label(text = "ПОВОРОТ", font = ("Courier New", 22), bg = "#e0e0eb",
        fg = "#33334d").place(width = 240, height = 30, x = PLOT_WIDTH + 30, y = 130)

    Label(text = "Угол°", font = ("Courier New", 19), bg = "#e0e0eb",
        fg = "#33334d").place(width = 60, height = 35, x = PLOT_WIDTH + 65, y = 165)

    angle_rotation = Entry(font = ("Courier New", 19))
    angle_rotation.place(width = 120, height = 35, x = PLOT_WIDTH + 150, y = 165)

    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 240, height = 30,  x = PLOT_WIDTH + 30, y = 210)

    Button(text = "Повернуть", font = ("Courier New", 18), 
        highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
        command = rotation).\
        place(width = 236, height = 26,  x = PLOT_WIDTH + 32, y = 212)



    Label(text = "ПЕРЕМЕЩЕНИЕ", font = ("Courier New", 22), bg = "#e0e0eb",
        fg = "#33334d").place(width = 240, height = 30, x = PLOT_WIDTH + 30, y = 255)

    Label(text = "  Dx \t   Dy  ", font = ("Courier New", 19), bg = "#e0e0eb",
        fg = "#33334d").place(width = 240, height = 20, x = PLOT_WIDTH + 30, y = 290)

    dx_movement = Entry(font = ("Courier New", 19))
    dx_movement.place(width = 120, height = 35, x = PLOT_WIDTH + 30, y = 315)

    dy_movement = Entry(font = ("Courier New", 19))
    dy_movement.place(width = 120, height = 35, x = PLOT_WIDTH + 150, y = 315)

    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 240, height = 30,  x = PLOT_WIDTH + 30, y = 360)

    Button(text = "Переместить", font = ("Courier New", 18), 
        highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
        command = movement).\
        place(width = 236, height = 26,  x = PLOT_WIDTH + 32, y = 362)



    Label(text = "МАСШТАБИРОВАНИЕ", font = ("Courier New", 22), bg = "#e0e0eb",
        fg = "#33334d").place(width = 240, height = 30, x = PLOT_WIDTH + 30, y = 405)

    Label(text = "  kx \t   ky  ", font = ("Courier New", 19), bg = "#e0e0eb",
        fg = "#33334d").place(width = 240, height = 20, x = PLOT_WIDTH + 30, y = 435)

    kx_scal = Entry(font = ("Courier New", 19))
    kx_scal.place(width = 120, height = 35, x = PLOT_WIDTH + 30, y = 460)

    ky_scal = Entry(font = ("Courier New", 19))
    ky_scal.place(width = 120, height = 35, x = PLOT_WIDTH + 150, y = 460)

    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 240, height = 30,  x = PLOT_WIDTH + 30, y = 505)

    Button(text = "Масштабировать", font = ("Courier New", 18), 
        highlightbackground = "#b3b3cc", highlightthickness = 30, fg = "#33334d",
        command = scaling).\
        place(width = 236, height = 26,  x = PLOT_WIDTH + 32, y = 507)



    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 240, height = 45,  x = PLOT_WIDTH + 30, y = 560)

    Button(text = "Шаг назад", font = ("Courier New", 19), 
        highlightbackground = "#d1d1e0", highlightthickness = 30, fg = "#33334d",
        command = step_back).\
        place(width = 236, height = 41,  x = PLOT_WIDTH + 32, y = 562)

    Button(highlightbackground = "#7575a3", highlightthickness = 30, fg = "#e0e0eb", state = DISABLED).\
        place(width = 240, height = 45,  x = PLOT_WIDTH + 30, y = 615)

    Button(text = "Исходное положение", font = ("Courier New", 19), 
        highlightbackground = "#d1d1e0", highlightthickness = 30, fg = "#33334d",
        command = starting_position).\
        place(width = 236, height = 41,  x = PLOT_WIDTH + 32, y = 617)


    cat = create_cat()
    vers_cat = [copy_cat(cat)]

    set_initial_values()
    draw_picture()

    window.mainloop()
