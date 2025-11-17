import math
type = int(input("Тип какой? 1 - треугольник, 2 - прямоугольник, 3 - круг:\n"))
if type == 1:
    a = int(input("Стороны какие? Давай ашку "))
    b = int(input("Давай бешку "))
    c = int(input("Давай цешку "))
    p = (a + b + c)/2.0
    print(math.sqrt(p * (p-a) * (p-b) * (p-c)))
elif type == 2:
    a = int(input("Стороны какие? Давай ашку "))
    b = int(input("Давай бешку "))
    print(a * b)
else:
    r = int(input("ААААААААААААААААААААААААА, давай радиус"))
    print("Приближённо", 3.14 * (r**2))
