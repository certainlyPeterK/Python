def task_473():
    a = int(input(">>> "))
    match int(str(a)[-1]):
        case 0:
            a **= 10
        case 1:
            a /= 3
        case 2:
            a //= 2
        case _:
            a **= 2
