import turtle as t
t.speed(5)
for abc in range(2):
    t.begin_fill()
    for ask in range(5):
        for a in range(4):
            t.fd(30)
            t.lt(90)
        t.fd(70)
    t.end_fill()
    t.rt(90)
    t.fd(150)
    t.rt(90)
    t.color("red")
    t.fillcolor("red")
