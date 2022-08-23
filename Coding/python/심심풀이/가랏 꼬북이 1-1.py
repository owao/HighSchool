import turtle
turtle.speed(10)
color=["red","orange","yellow","pink","gray"]

turtle.up()
for i in range(0,2):
    turtle.left(90)
    turtle.forward(100)
turtle.down()
while True:
    for x in color:
        turtle.color(x)
        turtle.left(70)
        turtle.forward(150)
