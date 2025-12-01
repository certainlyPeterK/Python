def task_4101():
    a = input("?\n")
    if len(a) == 0:
        print(None)
    elif len(a) <= 5:
        print("short")
    elif len(a) <= 10:
        print("normal")
    else:
        print("long")
