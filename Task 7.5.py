matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

res = 0

for i, row in enumerate(matrix):
    for j, elem in enumerate(row):
        if i == j:
            res += matrix[i][j]

print(res)
