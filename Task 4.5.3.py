def task_453():
    a = int(input("\n"))
    b = int(input("\n"))
    diff = abs(a - b)
    if (a > b):
        print(f"A длиннее на {diff}")
    elif (b > a):
        print(f"B длиннее на {diff}")
    else:
        print("Они равны")
    
task_453()
