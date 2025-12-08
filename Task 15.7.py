import time
from turtle import *

bgcolor("black")
speed(1)

a = Turtle()
b = Turtle()

a.color("red")
b.color("blue")

a.shape("turtle")
b.shape("turtle")

a.left(180)
a.circle(-100, 180)
b.circle(100, 180)

b.left(90)
b.forward(200)

a.circle(-100, -90)
a. right(90)
a.forward(200)

time.sleep(1)
        
