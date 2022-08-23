import 좌표평면
import turtle as t
import math

t.showturtle()
t.penup()
t.speed(0)
t.color("red")

for x in range(-100,100):
    if -100<=y<=0:
        if y**2==-(x**2)+100:
            t.goto(x,abs(y))
            t.pendown()
    t.penup() 
    if 0<=y<=100:
        if y**2==-x**2+100:
            t.goto(x,-1*abs(y))
            t.pendown()
