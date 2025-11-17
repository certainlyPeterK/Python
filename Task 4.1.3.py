a = int(input())
b = int(input())

if (a % 3 == 0 and b % 3 == 0):
    print("True")
elif (a % 3 != 0 and b % 3 != 0):
    print("False")
else:
    print("Одно число делится на 3")
