def task_4123():
    a = int(input(">>> print(\'(221 - 13) * 2\')\n>>> "))
    ans = (221 - 13) * 2
    if (a > ans):
        print(">")
    elif (a == ans):
        print(True)
    else:
        print("<")
