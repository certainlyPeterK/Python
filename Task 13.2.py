def CreateCalendar(month: str, year: int, days: int) -> str:
    print(f"calendar: {month} {year}")

    for i in range(days//7):
        week = ""
        for j in range(1, 8):
            week += str(i * 7 + j) + " "
        print(week)
    
    week = ""
    for i in range(1, days%7 + 1):
        week += str(days - days%7 + i) + " "
    print(week)
