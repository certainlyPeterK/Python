import time
from turtle import *

bgcolor('black')
color("white")
speed(10)

left(90)
while True:
    string = textinput("Куда?", "Куда?")
    howMuch = numinput("На сколько?", "На сколько?")
    match string:
        case "exit":    
            break
        case "w":
            setheading(90)
        case "d":
            setheading(0)
        case "s":
            setheading(-90)
        case "a":
            setheading(180)
        case _:
            pass
    forward(howMuch)
