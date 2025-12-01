def task_4102():
    a = int(input("?\n"))
    if a < 0:
        a = 1_000_000
        print(a)
    elif a == 0:
        a = 2
        a **= 2
    else:
        a **= 3
