import time
from turtle import *

speed(1)
bgcolor("red")
pencolor("yellow")
fillcolor("yellow")

begin_fill()
for i in range(5):
    forward(100)
    right(144)
    forward(100)
    left(72)
end_fill()

time.sleep(1)
