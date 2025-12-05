length = int(input("Всего числе будет: "))

nums = []

for i in range(length):
    newNum = int(input("Введите новое числе: "))
    nums.append(newNum)

print(list(filter(lambda x: x % 3 == 0 and x % 5 == 0, nums)))
