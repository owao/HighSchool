def cir (x,y):
    import math
    pi=math.pi #math모듈 쓸 겸 이게 더 값도 정밀할테니까 걍 바꿨음
    L = (2*pi*x)*(y/360) #걍 내가 보기 편할라고 괄호쳤는디 지워도대고..
    return L

import math , turtle

a=float(input("반지름(cm)은 얼마인가요?(1~30 사이로 입력해주세요)"))
b=float(input("부채꼴의 중심각은 얼마인가요?"))
result = cir(a,b)
print ("부채꼴의 호의 길이는 약 %.2f(cm)입니다!" %(result)) #굳이 올림 쓸 필요 없었던거같음 잘 나오는디

#부채꼴 그리기
#a가 1이면 그림이 안보여서 걍 10 곱해서 씀
turtle.hideturtle()
turtle.forward(a*10)
turtle.left(90)
turtle.circle(a*10,b) #걍 반지름 콤마 각도엿어 
turtle.left(90)
turtle.forward(a*10)
turtle.left(180-b)

'''
**문제점**
1. 터틀 할때 그림이 안보여서 부채꼴 그릴땐 걍 내가 임의조정햇음 좋은 대책을 생각해보아라
    반지름 제한은 30 넘으면 화면 밖으로 도형애 넘어가서..
2. 넓이는 뭐....... 걍 터틀로 도형색칠하면 되지않을까?? 막상 부채꼴 그리니까 좀 허전하긴하다
3. 각도가 ~~고 반지름이 ~~인 부채꼴의 호의 길이는 ~~이다라고 터틀이 부채꼴을 다 그린 다음에 출력하게 해봐
   내가 거기까지 다해주는건 좀 치사한거같아서 놔두겟음 정 필요하면 낼 다시 물어보고
'''
