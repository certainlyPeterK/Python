import time
from turtle import *

bgcolor('black')
color("white")
speed(10)

colours = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]
for i in range(0, len(colours)):
    color(colours[i])
    begin_fill()
    circle(100)
    end_fill()
    
time.sleep(1)
        
