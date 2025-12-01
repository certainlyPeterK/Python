def upper(t):
    a = ""
    for symbol in t:
        if symbol.isupper() == True:
            a += symbol
        else:
            a += " "
    print(a)
