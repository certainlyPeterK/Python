def task_483():
    lamp_1 = 0
    lamp_2 = 0
    a = input("Какую лампочку зажечь?\n")
    if (a == "1"):
        lamp_1 = 1
    elif (a == "2"):
        lamp_2 = 1
    else:
        print("Обе лампочки не горят")
