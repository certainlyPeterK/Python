A = [[-446, 281, -80],
     [465, 432, -122],
     [13, "error", 8]]

for row in A:
    for i, elem in enumerate(row):
        if(isinstance(elem, str) == True):
            row[i] = len(elem)

print(sum(sum(row) for row in A))
