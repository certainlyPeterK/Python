class Hotel:
    def __doc__(self):
        print("Класс для бронирования и снятия брони номеров отеля\n\n" \
        "Функции:\n\n" \
        "__doc__ - печатает документацию, \n" \
        "__init__(self, newName: str, rooms: dict) - создаёт екземпляр по переданному названию и словарю номеров\n" \
        "info(self) - выводит имя и статус всех комнат\n" \
        "occupy(self, room) - пытается поменять статус комнаты на занятый\n" \
        "set_free(self, room) - пытается поменять статус комнаты на свободній")

    def __init__(self, newName: str, rooms: dict):
        self.name = newName
        self.rooms = rooms
        
    def info(self):
        print(f"{self.name}")
        for room in self.rooms.keys():
            if self.rooms[room] == True:
                print(f"Номер № {room} свободен")
            else:
                print(f"Номер № {room} занят")

    def occupy(self, room):
        if (room in self.rooms and self.rooms[room] != False):
            self.rooms[room] = False
        else:
            print("Чё-то не так")
    
    def set_free(self, room):
        if (room in self.rooms and self.rooms[room] != True):
            self.rooms[room] = True
        else:
            print("Чё-то не так")

hotel = Hotel("У Олега", {100: True, 101: True, 102: True, 203: True})
hotel.info()
hotel.occupy(102)
hotel.info()
hotel.occupy(205)
hotel.info()
hotel.__doc__()

while True:
    inpt = input("[1] - Вывести занятость всех номеров\n" \
    "[2] - Занять номер\n" \
    "[3] - Снять бронь с номера\n" \
    "[4] - Выход\n")

    match inpt:
        case '1':
            hotel.info()
        case '2':
            room = int(input("Введите комнату: "))
            hotel.occupy(room)

        case '3':
            room = int(input("Введите комнату: "))
            hotel.set_free(room)
            
        case '4':
            break

        case _:
            print("Чего?")
