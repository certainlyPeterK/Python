hadANum = False
while not hadANum:
    a = input("число: ") 
    try:
        a = int(a)
    except ValueError:
        print(f"{a} - не число. Повторите ввод.")
    else:
        hadANum = True
        print(*range(0, a+1))
        
