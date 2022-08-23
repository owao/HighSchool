'''
A=[1,5,6,8]
B=[1,2,8,9]
C=[2,5,6,9]
D=[1,3,6,7]
E=[1,2,3,4]
F=[2,4,6,7]
G=[3,5,7,8]
H=[3,4,8,9]
I=[4,5,7,9]
'''

A=[1,2,3,7,8,9]
B=[1,2,3]
C=[7,8,9]
D=[1,2,3]
E=[1,2,3,4,5,6]
F=[4,5,6]
G=[7,8,9]
H=[4,5,6]
I=[4,5,6,7,8,9]

K=[A,B,C,D,E,F,G,H,I]

asdf=0
poiu={}

def delete(n,K):
    for k in K:
        if len(k)==1:
            continue
        if n not in k:
            continue
        else:
            k.remove(n)

while True:
    while True:
        print("A_1=",A)
        print("B_2=",B)
        print("C_3=",C)
        print("D_4=",D)
        print("E_5=",E)
        print("F_6=",F)
        print("G_7=",G)
        print("H_8=",H)
        print("I_9=",I)
        s=int(input("지우고자 하는 집합이 몇 번째인지 입력하세요."))
        n=int(input("지우고자 하는 숫자를 입력하세요."))
        qwer=int(input("임의로 가짓수를 더하고 건너뛸까요?"))
        print()
        if qwer!=0:
            break
        delete(n,K)
        if s==1:
            A=[n]
            poiu["A"]=A
        if s==2:
            B=[n]
            poiu["B"]=B
        if s==3:
            C=[n]
            poiu["C"]=C
        if s==4:
            D=[n]
            poiu["D"]=D
        if s==5:
            E=[n]
            poiu["E"]=E
        if s==6:
            F=[n]
            poiu["F"]=F
        if s==7:
            G=[n]
            poiu["G"]=G
        if s==8:
            H=[n]
            poiu["H"]=H
        if s==9:
            I=[n]
            poiu["I"]=I
        if len(A)==len(B)==len(C)==len(D)==len(E)==len(F)==len(G)==len(H)==len(I)==1:
            break
    if qwer==0:
        asdf+=1
    if qwer!=0:
        asdf=asdf+qwer
    print("결과 한 쌍을 완성했습니다. 지금까지의 경우의 수는 %d입니다." %(asdf))
    print(poiu,"순서대로 입력했습니다.")
    print()
    print()
    A=[1,2,3,7,8,9]
    B=[1,2,3]
    C=[7,8,9]
    D=[1,2,3]
    E=[1,2,3,4,5,6]
    F=[4,5,6]
    G=[7,8,9]
    H=[4,5,6]
    I=[4,5,6,7,8,9]
    '''
    A=[1,5,6,8]
    B=[1,2,8,9]
    C=[2,5,6,9]
    D=[1,3,6,7]
    E=[1,2,3,4]
    F=[2,4,6,7]
    G=[3,5,7,8]
    H=[3,4,8,9]
    I=[4,5,7,9]
    '''
    poiu={}
    K=[A,B,C,D,E,F,G,H,I]
