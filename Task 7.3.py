bin_sy = ['11011111', '11011101', '11000111', '11011100', '11011110']
dec_sy = []

for i in bin_sy:
    newDec = int(i, 2)
    dec_sy.append(newDec)
    print(newDec)

print(max(dec_sy), min(dec_sy))
