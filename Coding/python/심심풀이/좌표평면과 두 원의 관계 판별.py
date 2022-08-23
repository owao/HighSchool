import turtle as t
import math
t.speed(0)

t.penup()
t.goto(-500,0)
t.pendown()
t.goto(500,0)

t.penup()
t.goto(0,-500)
t.pendown()
t.goto(0,500)



for x in range(-400,401,100):
    if x==0:
        continue
    t.penup()
    t.goto(x,5)
    t.pendown()
    t.goto(x,-5)
    t.penup()
    t.goto(x,-20)
    t.write(int(x))

for y in range(400,-401,-100):
    if y==0:
        continue
    t.penup()
    t.goto(-5,y)
    t.pendown()
    t.goto(5,y)
    t.penup()
    t.goto(20,y)
    t.write(int(y))


t.penup()
t.goto(0,0)
t.pendown


x1 = int(t.numinput("input", "큰 원의 중심좌표 x1: "))
y1 = int(t.numinput("input", "큰 원의 중심좌표 y1: "))
r1 = int(t.numinput("input", "큰 원의 반지름: "))
x2 = int(t.numinput("input", "작은 원의 중심좌표 x2: "))
y2 = int(t.numinput("input", "작은 원의 중심좌표 y2: "))
r2 = int(t.numinput("input", "작은 원의 반지름: "))


t.penup()
t.goto(x1, y1-r1)
t.pendown()
t.circle(r1)

t.penup()
t.goto(x2, y2-r2)
t.pendown()
t.circle(r2)


check = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

if check < r1 - r2 :
    t.write("작은원이 큰원의 내부에 있습니다")
elif check > r1 + r2 :
    t.write("작은원이 큰원의 외부에 있습니다")
else :   
    t.write("작은원과 큰원이 겹칩니다")

