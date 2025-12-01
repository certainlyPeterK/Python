notebook = {}

def addNote(notebook, noteName, note):
    notebook[noteName] = note

def getNotes(notebook):
    if len(notebook) > 0:
        return str(notebook.keys())
    else:
        return "Заметок нет..."

def getNote(notebook, noteName):
    if noteName in notebook:
        return notebook[noteName]
    else:
        return "Такой заметки нет..."
    
def deleteNote(notebook, noteName):
    if noteName in notebook:
        notebook.pop(noteName)
        return ""
    else:
        return "Такой заметки нет..."
    
def menu():
    while True:
        choice = input("[1] - Create a new note. [2] - Read a note. [3] - Delete entry. [4] - Exit.\n> ")
        match choice:
            case "1":
                header = input("Header: ")
                text = input("Text: ")
                addNote(notebook, header, text)
            case "2":
                print(getNotes(notebook))
                if (len(notebook) > 0):
                    name = input("Which note to read?\n> ")
                    print(getNote(notebook, name))
            case "3":
                print(getNotes(notebook))
                if (len(notebook) > 0):
                    name = input("Which note to delete?\n> ")
                    print(deleteNote(notebook, name))
            case "4":
                return False
            case _:
                print("Не понял_/('_')\\_")

menu()
