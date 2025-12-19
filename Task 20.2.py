file = open("input.txt", "r")
content = file.read()
file.close()

with open("output.txt", "w") as f:
    f.write(content + "<copy>") 
f.close()
