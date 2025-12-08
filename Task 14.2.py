any_list = [4, 3.2, 16, 9, 13.5, 67]
for i, elem in enumerate(any_list):
    try:
        print(f"{elem} / {i} = {elem/i}")
    except ZeroDivisionError:
        print(f"Деление на 0! Элемент: {elem}")
