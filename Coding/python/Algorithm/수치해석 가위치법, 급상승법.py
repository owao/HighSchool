import numpy as np
import math
from scipy.optimize import fsolve


def false_position(func, x1, xu):
    #가위치법의 프로그래밍 코드 출처 : https://gist.github.com/harrydrippin/0932b2b5293839cd7d79fa6b513c8128
    # 최고 반복 한계값, 에러 최댓값 설정
    maxit = 100
    es = 1.0e-4

    # f(최저값)과 x(최고값)을 곱함
    test = func(xl) * func(xu)

    """
        False Position은 Bisection과 마찬가지로 구간을 기반으로 판단하는 알고리즘입니다.
        그러므로 역시 중간값 정리를 적용하여, 양쪽 끝값의 부호가 달라야 계산이 가능합니다.
        그렇지 않다면, 계산을 하지 않고 함수를 종료합니다.
    """
    if test > 0:
        print("No sign change")
        return [], [], [], []
    
    # 반복 카운터 초기화
    iter = 0

    # 중간값 초기화
    xr = xl

    # 오차 초기화
    ea = 100

    # 무한 반복
    while True:
        # 이전 중간값 저장
        xrold = xr

        # False Position 알고리즘 : 삼각형의 닮은꼴 기반 계산법 (PPT 참조)
        xr = np.float(xu - func(xu) * (xl - xu) / (func(xl) - func(xu)))

        # 반복 카운터 1 증가
        iter = iter + 1

        # 중간값이 0이 아니면
        if xr != 0:
            # 다음 식을 계산해서 오차값을 찾음
            # |{(현재 중심값) - (이전 중심값)} / (현재 중심값) | * 100
            ea = np.float(np.abs((np.float(xr) - np.float(xrold))/np.float(xr)) * 100)
        
        # f(최저값)과 x(최고값)을 곱함
        test = func(xl) * func(xr)

        # 만약 곱한 값이 양수라면
        if test > 0:
            # 최저값을 현재 중심값으로 설정함
            xl = xr
        # 아니고 만약 음수라면
        elif test < 0:
            # 최고값을 현재 중심값으로 설정함
            xu = xr
        # 만약 양수도, 음수도 아닌 0이라면
        else:
            # 오차 없음, 정확히 찾음
            ea = 0
        
        # 만약 (1) 계산된 오차값이 허용된 오차값보다 작다면 = 대강 이쯤되면 답이다 싶으면
        # 또는
        # 만약 (2) 설정한 최대 반복값보다 더 많이 돌았으면
        if np.int(ea < es) | np.int(iter >= maxit):
            # 계산 그만, 반복 종료
            break

    # 찾은 중심값을 근으로 함
    root = xr

    # f(근) 계산
    fx = func(xr)

    # 근, f(근), 오차, 반복 횟수 반환
    return root, fx, ea, iter


def soar_function(func,x1,x2): #단 x1<x2일 것
    while True:
        inclin=(func(x2)-func(x1))/(x2-x1) #기울기
        if incline==0:
            return (x1+x2)/2 #사잇값을 근으로 추정해서 반환한다
        if inclin>0:
            k=x1
            x1=x2
            x2=x2+(x2-k)
            a=1 #기울기가 양수일 때 변수를 1로 둔다
        if incline<0:
            k=x2
            x2=x1
            x1=x1-(x2-x1)
            a=2 #기울기가 음수일 때 변수를 2로 둔다
    #프로그램을 반복해도 0이 나오지 않는 경우에 대해서는 오류를 잡지 못함(기운이...없어....ㅠㅠ 미래의 나 수정해줘...)
    











    
