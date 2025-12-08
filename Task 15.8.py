import time
from turtle import *

bgcolor("black")
color("white")
speed(1)

for i in range(4):
    forward(100)
    circle(50, 90)

teleport(xcor(), ycor() + 100)

write(">>> Hello World!", font=('Arial', 12, 'normal'))

time.sleep(1)
        
