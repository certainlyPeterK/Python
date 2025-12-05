def TimeToTravel(speed, diameter):
    if speed > 0 and diameter > 0:
        return 3.14259 * diameter/speed
    else:
        return "Скорость и диаметр должны быть ненулевыми положительными числами"
