def task_451():
    a = int(input("\n"))
    b = int(input("\n"))
    if (a > b):
        a = a ** b
        b = a
    elif (b > a):
         b = b ** a
    else:
        b += a

    print(b)
