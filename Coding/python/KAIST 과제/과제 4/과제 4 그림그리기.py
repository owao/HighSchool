#기본 세팅

import turtle as t

t.title("mypicture")
t.setup(1000,800,0,0)

ts=t.getscreen()
ts.bgcolor("gray")








#별 그리기

t.speed(0)
t.pencolor("yellow")
t.color("yellow")

t.penup()
t.goto(300,300)
t.pendown()
t.begin_fill()
for i in range(0,5):
    t.forward(200)
    t.right(144)
t.end_fill()

t.penup()
t.goto(100,400)
t.pendown()
t.right(25)
t.begin_fill()
for i in range(0,5):
    t.forward(50)
    t.right(144)
t.end_fill()

t.penup()
t.goto(50,100)
t.pendown()
t.right(70)
t.begin_fill()
for i in range(0,5):
    t.forward(25)
    t.right(144)
t.end_fill()

t.penup()
t.goto(-300,200)
t.pendown()
t.right(50)
t.begin_fill()
for i in range(0,5):
    t.forward(100)
    t.right(144)
t.end_fill()

t.penup()
t.goto(-150,250)
t.pendown()
t.right(190)
t.begin_fill()
for i in range(0,5):
    t.forward(150)
    t.right(144)
t.end_fill()

t.penup()
t.goto(-400,350)
t.pendown()
t.right(30)
t.begin_fill()
for i in range(0,5):
    t.forward(50)
    t.right(144)
t.end_fill()

t.penup()
t.goto(200,210)
t.pendown()
t.right(165)
t.begin_fill()
for i in range(0,5):
    t.forward(60)
    t.right(144)
t.end_fill()









#구름 그리기

t.penup()
t.goto(-500,160)
t.pendown()
t.color(0.85,0.85,0.85)
t.begin_fill()
t.circle(60)
t.end_fill()

t.penup()
t.goto(-450,140)
t.pendown()
t.color(0.85,0.85,0.85)
t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
t.goto(-400,130)
t.pendown()
t.color(0.85,0.85,0.85)
t.begin_fill()
t.circle(40)
t.end_fill()

t.penup()
t.goto(-350,110)
t.pendown()
t.color(0.85,0.85,0.85)
t.begin_fill()
t.circle(30)
t.end_fill()

t.penup()
t.goto(-320,100)
t.pendown()
t.color(0.85,0.85,0.85)
t.begin_fill()
t.circle(20)
t.end_fill()




t.penup()
t.goto(400,130)
t.pendown()
t.color(0.85,0.85,0.85)
t.begin_fill()
t.circle(40)
t.end_fill()

t.penup()
t.goto(350,140)
t.pendown()
t.color(0.85,0.85,0.85)
t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
t.goto(300,130)
t.pendown()
t.color(0.85,0.85,0.85)
t.begin_fill()
t.circle(40)
t.end_fill()

t.penup()
t.goto(250,110)
t.pendown()
t.color(0.85,0.85,0.85)
t.begin_fill()
t.circle(30)
t.end_fill()

t.penup()
t.goto(220,100)
t.pendown()
t.color(0.85,0.85,0.85)
t.begin_fill()
t.circle(20)
t.end_fill()








#언덕과 사람 그리기

t.penup()
t.goto(0,-70)
t.pendown()
t.color(0.35,0.35,0.35)
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(0,-100)
t.pendown()
t.color(0.35,0.35,0.35)
t.begin_fill()
t.circle(40)
t.end_fill()

t.penup()
t.goto(0,-110)
t.pendown()
t.color(0.35,0.35,0.35)
t.begin_fill()
t.circle(40)
t.end_fill()

t.penup()
t.goto(0,-120)
t.pendown()
t.color(0.35,0.35,0.35)
t.begin_fill()
t.circle(40)
t.end_fill()

t.penup()
t.goto(0,-130)
t.pendown()
t.color(0.35,0.35,0.35)
t.begin_fill()
t.circle(40)
t.end_fill()

t.penup()
t.goto(0,-140)
t.pendown()
t.color(0.35,0.35,0.35)
t.begin_fill()
t.circle(40)
t.end_fill()



t.penup()
t.goto(0,-200)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(1000)
t.end_fill()

t.hideturtle()
