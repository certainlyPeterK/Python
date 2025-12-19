from datetime import datetime

def AddEntry(entryText: str):
    file = open("log note.txt", "a+")
    file.write(datetime.today().strftime('%Y-%m-%d') + " " + datetime.now().strftime("%H:%M:%S") + ": " + entryText)
    file.close()
