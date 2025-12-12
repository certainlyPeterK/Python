import time
from turtle import *

def a(x, y):
    setheading(180)
    forward(10)

def d(x, y):
    setheading(0)
    forward(10)

def s(x, y):
    setheading(-90)
    forward(10)

def w(x, y):
    setheading(90)
    forward(10)

def makeButton(x, y, func):
    newButton = Turtle()
    newButton.shape('square') # Use a built-in shape
    newButton.shapesize(1, 1) # Make it look like a button (height, width)
    newButton.color("white")
    newButton.teleport(x, y)
    newButton.onclick(func)

bgcolor('black')
color("white")
speed(10)

makeButton(-100, -100, a)
makeButton(0, -100, d)
makeButton(-50, -150, s)
makeButton(-50, -50, w)

mainloop()
