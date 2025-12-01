def task_4121():
    ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    en = 'abcdefghijklmnopqrstuvwxyz'
    a = input("?\n")
    if a in ru:
        print("rus")
    elif a in en:
        print("eng")
    else:
        print(None)
