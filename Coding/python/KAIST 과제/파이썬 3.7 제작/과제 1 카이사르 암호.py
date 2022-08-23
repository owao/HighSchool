def sc(p):
    a=["'",".",",",":",";","?","!","`","~","(",")"," ","‘", "’"]
    if p in a:
        return True
    else:
        return False

while True:
    s=input("영어 문자열을 입력하세요")
    n=int(input("몇 자를 옮길지 입력하세요"))
    result=""
    for a in s:
        if sc(a) == True:
            result+=a
            continue
        b=int((ord(a)+n))
        if n>0 :
            if 65<=ord(a)<=90:
                if 91<=b<=116:
                    b=b-26
            if 97<=ord(a)<=122:
                if 123<=b<=148:
                    b=b-26
        if n<0:
            if 65<=ord(a)<=90:
                if 39<=b<=64:
                    b=b+26
            if 97<=ord(a)<=122:
                if 71<=b<=96:
                    b=b+26
        c=chr(b)
        result+=c
    print(result)
    print()







    

'''

Hsle ozpd l mwzddzx mpnzxp
+15
What does a blossom become



Cngz oy znk yvuxz zngz oy vrgekj hkzckkt zcu zkgsy ul krkbkt vrgekxy cozn g hgrr
-6
What is the sport that is played between two teams of eleven players with a ball



Patm labgxl bg max gbzam ldr
+7
What shines in the night sky



Epib qa bpm vium wn i tqycql bpib gwc kivvwb tqdm eqbpwcb
-8
What is the name of a liquid that you cannot live without



Ufyr kyicq y zgpb djw
+2
What makes a bird fly

'''
