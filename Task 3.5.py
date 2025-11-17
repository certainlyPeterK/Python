n = int(input("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN"))
susch = ""
if (len(str(n)) == 1):
    if (n == 1):
        susch = "программист"
    elif (str(n) in '234'):
        sucsh = "программиста"
    else:
        sucsh = "программистов"
else:
    if (str(n)[-1] == '1' and str(n)[-2] != '1'):
        sucsh = "программист"
    elif (str(n)[-1] in '234' and str(n)[-2] != '1'):
        sucsh = "программиста"
    else:
        sucsh = "программистов"

print(n, sucsh)
