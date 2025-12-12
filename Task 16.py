import random

actions = {"w":0, "a":0, "d":0}

currentAction = input("Начинаем игру. Повороты: [a]-Налево, [w]-Направо, [d]-Направо Куда идти?\n")
while currentAction != "a" and currentAction != "w" and currentAction != "d":
    currentAction = input("Неккоректно. Повороты: [a]-Налево, [w]-Направо, [d]-Направо Куда идти?\n")    
rand = random.randint(1, 10)

while rand != 1:
    match currentAction:
        case "w":
            actions[currentAction] += 1            
            currentAction = input("Пошёл прямо. Выхода пока нет... Куда идти?\n")
            rand = random.randint(1, 10)
        case "a":
            actions[currentAction] += 1
            currentAction = input("Пошёл налево. Выхода пока нет... Куда идти?\n")
            rand = random.randint(1, 10)
        case "d":
            actions[currentAction] += 1
            currentAction = input("Пошёл направо. Выхода пока нет... Куда идти?\n")
            rand = random.randint(1, 10)
        case _:
            currentAction = input("Неккоректно. Повороты: [a]-Налево, [w]-Направо, [d]-Направо Куда идти?\n")

match currentAction:
    case "w":
        result = "Пошёл прямо."
        actions[currentAction] += 1
    case "a":
        result = "Повернул налево."
        actions[currentAction] += 1
    case "d":
        result = "Повернул направо."
        actions[currentAction] += 1
    case _:
        result = "Я сам не понял, что я сделал."
result += f" Выход найден. Ты выиграл. Для того, чтобы найти выход ты {actions["a"]} раз повернул налево, {actions["w"]} раз пошёл прямо и {actions["d"]} раз повернул направо."
print(result)
