print("회전변환행렬을 이용한 점의 회전입니다.")
print("원점을 기준으로 몇 도만큼 회전한 점의 위치는 어디가 되는지 확인할 수 있습니다.")
print("(단, 좌표는 근삿값입니다)")

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
    t.write(int(x/10))

for y in range(400,-401,-100):
    if y==0:
        continue
    t.penup()
    t.goto(-5,y)
    t.pendown()
    t.goto(5,y)
    t.penup()
    t.goto(20,y)
    t.write(int(y/10))
    
t.penup()
t.goto(0,0)
t.pendown

def a(x,y):
    import turtle as t
    t.penup()
    t.speed(3)
    t.goto(x*10,y*10)
    t.pendown()
    t.dot(5,"blue")
    t.penup()
    t.goto(x*10-20,y*10-20)
    t.pendown()
    t.write("(%d, %d)" %(x,y))
    t.penup()
    t.goto(0,0)
    t.pendown()

def b(x,y):
    import turtle as t
    t.penup()
    t.speed(3)
    t.goto(x*10,y*10)
    t.pendown()
    t.dot(5,"red")
    t.penup()
    t.goto(0,0)
    t.pendown()

def cir(x,y):
    import turtle as t
    import math
    t.penup()
    t.speed(0)
    q=(x*10)**2
    p=(y*10)**2
    u=float(math.sqrt(q+p))
    t.goto(0,-u)
    t.pendown()
    t.color("pink")
    t.circle(u)
    t.penup()
    t.goto(10,-u/2)
    t.pendown()
    t.color("blue")
    t.write("좌표는 이 원을 따라 반시계 방향으로 이동하게 됩니다.")
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.color("black")








x1 = int(t.numinput("input", "원래의 x좌표: "))
y1 = int(t.numinput("input", "원래의 y좌표: "))

cir(x1,y1)
a(x1,y1)

while True:
    print()
    d = float(t.numinput("input","원래의 점에서 몇 도를 회전하시겠습니까?(그만하실때는 0을 넣어주세요):"))
    if d==0:
        break

    x2=float((x1*(math.cos(math.radians(d)))-y1*(math.sin(math.radians(d)))))
    y2=float((x1*(math.sin(math.radians(d)))+y1*(math.cos(math.radians(d)))))

    b(x2,y2)
    print("회전한 점의 위치는 (%d,%d)입니다" %(x2,y2))


'''
#점을 회전시켜서 원을 그리기
t.speed(0)
for d in range (360):
    x2=(x1*(math.cos(math.radians(d)))-y1*(math.sin(math.radians(d))))
    y2=(x1*(math.sin(math.radians(d)))+y1*(math.cos(math.radians(d))))
    b(x2,y2)
'''
