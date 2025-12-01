def task_491():
    a = int(input("?\n"))
    dop = ""
    if a % 2 == 0 and a > 0:
        dop = "even"
    elif a > 0:
        dop = "odd"
    print(a > 0, dop)
