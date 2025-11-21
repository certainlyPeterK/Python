neg = []
nul = []
pos = []
amount = int(input("Введите количество чисел: "))

for i in range (amount):
    newNum = int(input("Введите числа: "))
    if (newNum < 0):
        neg.append(newNum)
    elif (newNum == 0):
        nul.append(newNum)
    else:
        pos.append(newNum)
print(sum(neg))

try:
    print(sum(pos)/len(pos))
except ZeroDivisionError:
    print("Ну вот что ты делаешь, а?")
  
for nulb in nul:
    nul.pop(0)
    nul.append('*')
  
print(f"Количество звёзд: {len(nul)} {nul}")
