import time
from turtle import *

bgpic('back1.png')
color("black")
speed(5)

cell = 60

for i in range(2):
    right(90)
    forward(cell * 1.5)   
right(90)
forward(cell*3)
right(90)
forward(cell*2.2)
right(90)
forward(cell)
left(90)
forward(cell)
right(90)
forward(cell*1.5)

time.sleep(1)
