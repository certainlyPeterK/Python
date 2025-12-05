def square(y: int, x: int):
    print(" _ " * x)
    for i in range(y):
        newLine = ""
        for i in range(1, x+1):
            newLine += f"|{i}|"
        print(newLine)
    print(" ¯ " * x)
