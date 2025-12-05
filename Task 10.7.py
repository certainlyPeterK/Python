def CustomFilter(workingList: list):
    summa = 0
    for i in workingList:
        if isinstance(i, int):
            if i % 7 == 0:
                summa += i
    print(not summa > 83)
