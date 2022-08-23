import turtle
n=20
for x in range(0, 10):
    turtle.forward(20)
    turtle.left(120)
    for x in range(0,6):
        turtle.forward(n)
        turtle.left(60)
    turtle.right(120)
    n=n+20
for x in range(0,3):
    turtle.left(120)
    turtle.forward(200)
    turtle.left(120)
    turtle.forward(400)
