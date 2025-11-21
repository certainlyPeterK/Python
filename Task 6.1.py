matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

uneven = []
even = []

for row in matrix:
    for elem in row:
        if elem % 2 == 1:
            uneven.append(elem)
        else:
            even.append(elem)

print("matrix:")
for row in matrix:
    print(row)

print("нечётные числ matrix")
print(*uneven)
print(f"кол-в чётных: {len(even)}")
