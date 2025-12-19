import urllib.request
import webbrowser

print("Проверка подключния к интернету...")

try:
    urllib.request.urlopen("https://github.com/TeachKait20/Python-Practice-Exercises/")
    
except IOError:
    print("Соединение не установлено\nПроверьте подключение к интернету")

else:
    print("Соединение стабильно")

    question = input("Введите запрос: ")

    print("Выбор браузера для поиска\n[1] - Google, [2] - Яндекс")
    browser = int(input("> "))
    while browser not in range(1, 3):
        print("Выберите из предложенных вариантов.\nВыбор браузера для поиска\n[1] - Google, [2] - Яндекс")
        browser = int(input("> "))
    
    match browser:
        case 1:
            webbrowser.open("https://www.google.com/search?q=" + question)
        case 2:
            webbrowser.open("https://ya.ru/search/?text=" + question)
