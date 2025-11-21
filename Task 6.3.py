fruits = [["Banana", "apple"],
          ["apricot", "Avocado"],
          ["lime", "lemon"],
           ["Mango", "grapes"]]

upper = []

for row in fruits:
    for elem in row:
        if (elem[0].isupper() == True):
            upper.append(elem)

print(*upper)
