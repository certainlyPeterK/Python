def task_491():
    switch_1 = False
    switch_2 = False
    a = input("Включить?\n")
    if (a == "да"):
        switch_1 = True
        switch_2 = True
        print("Всё включено")
    else:
        print(switch_1, switch_2)
