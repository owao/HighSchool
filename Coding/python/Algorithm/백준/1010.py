from math import * #for factorial

T=int(input()) #test case

for i in range(T):
    a,b=map(int, input().split()) #a는 서쪽, b는 동쪽
    s=factorial(b)/(factorial(a)*factorial(b-a))
    print(int(s))
            
        

#이쌉새기가일대일함수를만들라고하네
