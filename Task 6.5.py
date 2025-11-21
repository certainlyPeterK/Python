y = int(input("Введите количество строк\n"))
x = int(input("Введите количество столбцов\n"))

matrix = []

for i in range(y):
    newRow = []
    for j in range(x):
        newElem = int(input(f"Введите значение элемента [{i}][{j}]:\n"))
        newRow.append(newElem)
    matrix.append(newRow)
    
print("Ваш двумерный массив:")
for row in matrix:
    print(row)
