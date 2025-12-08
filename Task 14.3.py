any_list = []
i = 0
while i < 5:
    a = input()
    try:
        a = int(a)
    except ValueError:
        pass
        i -= 1
    else:
        any_list.append(a)
    i += 1
print(f"Числа в списке: {any_list}")
