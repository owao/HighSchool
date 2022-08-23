import 좌표평면
import turtle as t
import math

t.showturtle()
t.penup()
t.speed(0)
t.color("red")

for x in range(-300,300):
    t.goto(x,abs((1/100)*(x**2)-100))
    t.pendown()
