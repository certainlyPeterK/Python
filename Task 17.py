import random
import time

def strsum(iterable):
    result = ""
    for string in iterable:
        result += string
    return result

def loading():
    for i in range(1, 101):
        print("\n"*20)
        print(f"Загрузка: {i}%")
        print("-"*(i//8))
        if (i not in range(90, 100)):
            time.sleep(random.uniform(0.01, 0.1))
        else:
            time.sleep(random.uniform(0.1, 1))
            if (i == 99):
                time.sleep(random.uniform(1, 2))

loading()

figurePieces = ["┌", "┐", "└", "┘"]
idealFigure = ["┌", "┐", "└", "┘"]
curFigure = [figurePieces[random.randint(0, 3)] for i in range(len(figurePieces))] 

while idealFigure != curFigure:
    print("\n"*20)
    print(f"Должна получиться такая фигура:\n{strsum(idealFigure[0:2])}\n{strsum(idealFigure[2:])}")
    print(f"С помощью кнопок 1, 2, 3, 4 меняйте направление элементов фигуры.\n{strsum(curFigure[0:2])}\n{strsum(curFigure[2:])}")
    where = int(input("> "))
    curFigure[where-1] = figurePieces[random.randint(0, 3)]
    
print(f"{strsum(curFigure[0:2])}\n{strsum(curFigure[2:])}")
print("Ура! Победа!")
    
