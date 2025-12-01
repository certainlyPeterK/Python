def task_463():
    a = int(input(">>> "))
    b = int(input(">>> "))
    if (a < 0):
        a += 1000
        print(b)
    if (b < 0):
        b += 1000
        print(a)
    if ((a > 0 and b > 0) or (a < 0 and b < 0)):
        print((a > 0 and b > 0))
