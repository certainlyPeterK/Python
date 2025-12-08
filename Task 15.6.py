import time
from turtle import *

bgcolor("black")
speed(100)

colours = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]

for i in range(0, 56):
    pencolor(colours[i%7])
    circle(100)
    right(180/28)

time.sleep(3)
