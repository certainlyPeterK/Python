bilet = input(">>> ")
if (sum([int(char) for char in bilet[0:3]]) == sum([int(char) for char in bilet[3:7]])):
    print("Счастливый")
else:
    print(":(")
