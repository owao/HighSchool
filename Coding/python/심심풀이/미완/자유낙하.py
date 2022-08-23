import 좌표평면
import turtle as t
import math

t.showturtle()
t.penup()
t.speed(0)
t.color("red")

for x in range(0,300):
    t.goto(x,-((9.8*x*x)/1000)+300)
    t.pendown()
