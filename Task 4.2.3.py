def task_423():
    r = int(input())
    g = int(input())
    b = int(input())
    if (r == g and g == b and b == 0):
        print("Чёрный цвет")
    elif (r == g and g == b and b == 255):
        print("Белый цвет")
    elif (r == 255 and g == b and b == 0):
        print("Красный цвет")
    elif (g == 255 and r == b and b == 0):
        print("Зелёный цвет")
    elif (b == 255 and r == g and r == 0):
        print("Синий цвет")
    else:
        print("Нет цвета")
