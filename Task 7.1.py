table = [["folder", "coursework.doc", "folder", "pict.png", "data.accdb"],
        ["icon.ico", "script.js", "index.html", "style.css", "prog.py"],
        ["my_song.mp3", "anapa-2003.jpg", "cs_1.6.exe", "folder", "cheat.txt"],
        ["notext.txt", "main.py", "work.pdf", "cartoon.mp4", "array.py"],
        ["project.psd", "cycle.py", "folder", "cycle.js", "turtle.py"]]

print(table)

pys = []
jss = []

for row in table:
    for elem in reversed(row):
        if row[row.index(elem)] == "folder":
            row.pop(row.index(elem))
        elif row[row.index(elem)] == "data.accdb":
            row[row.index(elem)] = "data.sql"
        elif row[row.index(elem)][-3:] == ".py":
            pys.append(row[row.index(elem)])
        elif row[row.index(elem)][-3:] == ".js":
            jss.append("new_" + row[row.index(elem)])

print(table)

print(pys)
print(jss)
            
