with open("data.txt", "r") as f:
    c = f.read()
    count = 0
    for line in c.split("\n"):
        if 'John' in line:
            count -=- 1
    print(count)
f.close()
