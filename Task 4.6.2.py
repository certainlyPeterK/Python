def task_462():
    a = int(input(">>> "))
    if (a % 2 == 0 or a % 3 == 0):
        if (a % 2 == 0):
            a **= 2
        if (a % 3 == 0):
            a **= 3
    else:
        a *= 100
