import turtle

n=50
a=70
turtle.speed(30)

while a<100:
    for x in range(n):
        turtle.circle(a)
        turtle.left(360/n)
    a=a+10
