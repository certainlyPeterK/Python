def alpha(string: str) -> str:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    string += alphabet
    string = dict.fromkeys(string)
    string = " ".join(string)
    print(string)
