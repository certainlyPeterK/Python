def task_4111():
    prog_num = 0
    a = int(input("?\n"))
    b = int(input("?\n"))
    if (a < 0 and b < 0):
        prog_num = a + b
        print(prog_num)
    elif (a > 0 and b > 0):
        prog_num = abs(a - b)
        print(prog_num)
    else:
        print(False)
