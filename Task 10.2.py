def punct(txt: str):
    a = "!?.,()"
    summ = 0
    for mark in a:
        if mark in txt:
            summ += txt.count(mark)
    if (summ > 0):
        print(summ)
