word_numb = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]

numb = int(input("Введите число от 0 до 9: "))
if (numb in range(0, 10)):
    for i in word_numb[:numb+1]:
        print(i)
else:
    print("Введите число <= 9")
