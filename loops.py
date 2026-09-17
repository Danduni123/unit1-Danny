import turtle
from turtle import *
t = Turtle()
t.speed(100)

""" def square():
    for i in range(60):
        for i in range(4):
            t.forward(100)
            t.left(90)
        t.left(5)
        
square() """


length = 5

for i in range(60):
    for i in range(4):
        t.forward(length)
        t.right(90)
    t.right(5)
    length += 5

turtle.done()