a = int(input("AAAAAAAAAAAAAAAAAAAAAAAAAAAA"))
b = int(input("BBBBBBBBBBBBBBBBBBBBBBBBBB"))
h = int(input("hhhhhhhhhhhhhhhhhhhhhhhhhh"))
if h in range(a, b+1):
    print("Это нормально")
elif (h > b):
    print("Пересып")
else:
    print("Недосып")
