'''
휴 다됐다 이제
1. 결과물 정렬
2. 개설된 시간 구분하기(수학 분반 영어 분반같은거...) **다음으로 중요!
3. 덮어써서 수강 가능하게 하기 ***젤 중요!
이정도만 더 하면 되겠지ㅎㅎㅎㅎㅎㅎ
'''

import time

def A(a,b,c,d,e): #a는 학번, b는 학기, c/d/e는 각각 정보/철학, 중어/일어, 영문/영미
    res=["인문", "화학", "물리", "사회", "생명과학", "생물", "경영", "수학/통계학", "수학", "통계학", "통계"]
    if a%2==0:
        if b == "1" or b == "1학기":
            print("\n당신의 1학기 시간표를 짭니다.\n당신은 짝수 학번이므로 이번 학기에는 논술, 음악 과목을 선택해서 듣게 됩니다.")
            p=["수학", "영어", "국어", "한국사", "논술", "음악", "통합과학", "통합사회", "체육", c, d, e, "공강"]
            print("당신의 이번 학기 선택 과목은 %s입니다." %(p))
            return p
        if b == "2" or b == "2학기":
            print("\n당신의 2학기 시간표를 짭니다.\n당신은 짝수 학번이므로 이번 학기에는 과학탐구실험, 미술 과목을 선택해서 듣게 됩니다.")
            while True:
                s=input("당신의 과제연구 분야는 무엇입니까?:")
                if s not in res:
                    print("개설되지 않은 과목입니다. 개설된 과목을 선택해주세요.")
                    continue
                else:
                    if s == "수학" or s == "통계" or s == "통계학":
                        s="수학/통계학"
                    if s == "생물":
                        s="생명과학"
                    break    
            p=["과제연구(%s)"%(s), "수학", "영어", "국어", "한국사", "과학탐구실험", "미술", "통합과학", "통합사회", "체육", c, d, e]
            print()
            print("당신의 이번 학기 선택 과목은 %s입니다." %(p))
            return p
    if a%2==1:
        if b == "1" or b== "1학기":
            print(" \n당신의 1학기 시간표를 짭니다. \n당신은 홀수 학번이므로 이번 학기에는 과학탐구실험, 미술 과목을 선택해서 듣게 됩니다.")
            p=["수학", "영어", "국어", "한국사", "과학탐구실험", "미술", "통합과학", "통합사회", "체육", c, d, e, "공강"]
            print("당신의 이번 학기 선택 과목은 %s입니다." %(p))
            return p
        if b == "2" or b == "2학기":
            print("\n당신의 2학기 시간표를 짭니다.\n당신은 홀수 학번이므로 이번 학기에는 논술, 음악 과목을 선택해서 듣게 됩니다.")
            while True:
                s=input("당신의 과제연구 분야는 무엇입니까?:")
                if s not in res:
                    print("개설되지 않은 과목입니다. 개설된 과목을 선택해주세요.")
                    continue
                else:
                    if s == "수학" or s == "통계" or s == "통계학":
                        s="수학/통계학"
                    if s == "생물":
                        s="생명과학"
                    break
            p=["과제연구(%s)"%(s), "수학", "영어", "국어", "한국사", "논술", "음악", "통합과학", "통합사회", "체육", c, d, e]
            print()
            print("당신의 이번 학기 선택 과목은 %s입니다." %(p))
            return p

def B(a,b,d): #a는 학번, b는 학기, d는 중어/일어. 3타임짜리 과목을 지정함
    if a%2==0:
        if b == "1" or b == "1학기":
            p=["수학", "영어", "국어", "한국사", "음악", "통합과학", "통합사회", d]
            return p
        if b == "2" or b == "2학기":
            p=["수학", "영어", "국어", "한국사", "미술", "통합과학", "통합사회", d]
            return p
    if a%2==1:
        if b == 1:
            p=["수학", "영어", "국어", "한국사", "미술", "통합과학", "통합사회", d]
            return p
        if b == "2" or b == "2학기":
            p=["수학", "영어", "국어", "한국사", "음악", "통합과학", "통합사회", d]
            return p
        
def tita(A,B,C,D,E,F,G,H,a,b,c,d,e):
    M="월요일"
    T="화요일"
    W="수요일"
    Th="목요일"
    Fri="금요일"

    print()
    print("      %s    %s    %s    %s    %s" %(M,T,W,Th,Fri))
    print(" 1     %s       %s       %s       %s       %s" %(B,F,c,d,e))
    print(" 2     %s       %s       %s       %s       %s" %(B,H,c,d,e))
    print(" 3     %s       %s       %s       %s       %s" %(A,a,D,E,G))
    print(" 4     %s       %s       %s       %s       %s" %(A,a,D,E,G))
    print(" 5     %s       %s       %s       %s       %s" %(E,b,C,F,B))
    print(" 6     %s       %s       %s       %s       %s" %(D,b,C,F,H))
    print(" 7     %s       %s                 %s       %s" %(C,G,A,H))
    print()






while True:
    print("당신의 하나고등학교 1학년 시간표를 짜 주는 프로그램입니다.(9기 기준) \n시작하시려면 <Enter>를 눌러주세요.")
    input()

    while True:
        try:
            a=int(input("당신의 고유학번은 몇 번입니까?:"))
            if a<18000 or a>18300:
                print("9기의 학번이 아닙니다. 다시 입력해주세요.")
                continue
            else:
                break
        except:
            print("숫자만 입력해주세요.")
            continue
    while True:
        b=input("몇학기입니까?:")
        if b =="1" or b=="1학기" or b=="2" or b=="2학기":
            break
        else:
            print("정상적인 학기가 아닙니다. 다시 입력해주세요.")
            continue
    while True:
        c=input("정보입니까 철학입니까?:")
        if c=="정보" or c=="철학":
            break
        else:
            print("두 과목 중에 선택해주세요.")
            continue
    while True:
        d=input("중국어입니까 일본어입니까?:")
        if d=="중국어" or d=="일본어":
            break
        else:
            print("두 과목 중에 선택해주세요.")
            continue
    while True:
        e=input("영어권문화입니까 영미문학읽기입니까?:")
        if e=="영문" or e=="영어권문화" or e=="영어권 문화":
            e="영어권문화"
            break
        if e=="영미" or e=="영미문학읽기":
            e="영미문학읽기"
            break
        else:
            print("두 과목 중에 선택해주세요.")
            continue

    p=A(a,b,c,d,e)
    th=B(a,b,d)
    res=["인문", "화학", "물리", "사회", "생명과학", "생물", "경영", "수학/통계학", "통계학", "통계"]

    AAA="3A1"
    BBB="3B1"
    CCC="3C1"
    DDD="3D1"
    EEE="3E1"
    FFF="3F1"
    GGG="3G1"
    HHH="3H1"
    AA="2A1"
    BB="2B1"
    CC="2C1"
    DD="2D1"
    EE="2E1"

    tt=[AAA, BBB, CCC, DDD, EEE, FFF, GGG, HHH, AA, BB, CC, DD, EE]
    tht=[AAA, BBB, CCC, DDD, EEE, FFF, GGG, HHH]
    twt=[AA, BB, CC, DD, EE]

    tita(AAA,BBB,CCC,DDD,EEE,FFF,GGG,HHH,AA,BB,CC,DD,EE)
    
    print("시간표 작성 현황을 보고 싶으시면 언제든지 0을 눌러주세요.")
    print("종료하고 싶으실 때는 언제든지 1을 눌러주세요.")

    while True:
        if p==[]:
            break

        print()
        sub=input("듣고 싶은 과목을 입력하세요:")
        if sub=="0":
            print()
            print("남은 과목은 %s입니다.\n아래는 현 시간표 현황입니다." %(p))
            tita(AAA,BBB,CCC,DDD,EEE,FFF,GGG,HHH,AA,BB,CC,DD,EE)
            continue
        if sub=="1":
            exit()
        if sub=="영문" or a=="영어권 문화":
            sub="영어권문화"
        if sub=="영미":
            sub="영미문학읽기"
        if sub=="통사":
            sub="통합사회"
        if sub=="통과":
            sub="통합과학"
        if sub=="과탐실":
            sub="과학탐구실험"
        if sub=="과제연구" or sub=="과연" or sub in res:
            sub=p[0]

        if sub not in p:
            print("신청이 불가능한 과목입니다. 다시 입력해주세요.")
            continue
        if sub in th:
            while True:
                ti=input("어느 시간에 신청하시겠습니까? 시간표에 나온 기호를 입력해주세요.")
                if ti=="0":
                    print()
                    print("남은 과목은 %s입니다.\n아래는 현 시간표 현황입니다." %(p))
                    tita(AAA,BBB,CCC,DDD,EEE,FFF,GGG,HHH,AA,BB,CC,DD,EE)
                    continue
                if ti=="1":
                    exit()
                if ti not in tt:
                    print("신청 가능한 시간대가 아닙니다. 다시 입력해주세요.")
                    continue
                if ti in twt:
                    print("3타임짜리 수업이기 때문에 이 곳에는 넣을 수 없습니다.")
                else:
                    if ti==AAA:
                        tt.remove(AAA)
                        AAA=sub
                        p.remove(sub)
                    if ti==BBB:
                        tt.remove(BBB)
                        BBB=sub
                        p.remove(sub)
                    if ti==CCC:
                        tt.remove(CCC)
                        CCC=sub
                        p.remove(sub)
                    if ti==DDD:
                        tt.remove(DDD)
                        DDD=sub
                        p.remove(sub)
                    if ti==EEE:
                        tt.remove(EEE)
                        EEE=sub
                        p.remove(sub)
                    if ti==FFF:
                        tt.remove(FFF)
                        FFF=sub
                        p.remove(sub)
                    if ti==GGG:
                        tt.remove(GGG)
                        GGG=sub
                        p.remove(sub)
                    if ti==HHH:
                        tt.remove(HHH)
                        HHH=sub
                        p.remove(sub)
                    break
        if sub not in th:
            while True:
                ti=input("어느 시간에 신청하시겠습니까? 시간표에 나온 기호를 입력해주세요.")
                if ti=="0":
                    print()
                    print("남은 과목은 %s입니다.\n아래는 현 시간표 현황입니다." %(p))
                    tita(AAA,BBB,CCC,DDD,EEE,FFF,GGG,HHH,AA,BB,CC,DD,EE)
                    continue
                if ti=="1":
                    exit()
                if ti not in tt:
                    print("신청 가능한 시간대가 아닙니다. 다시 입력해주세요.")
                    continue
                if ti not in twt:
                    print("2타임짜리 수업이기 때문에 이 곳에는 넣을 수 없습니다.")
                else:
                    if ti==AA:
                        tt.remove(AA)
                        AA=sub
                        p.remove(sub)
                    if ti==BB:
                        tt.remove(BB)
                        BB=sub
                        p.remove(sub)
                    if ti==CC:
                        tt.remove(CC)
                        CC=sub
                        p.remove(sub)
                    if ti==DD:
                        tt.remove(DD)
                        DD=sub
                        p.remove(sub)
                    if ti==EE:
                        tt.remove(EE)
                        EE=sub
                        p.remove(sub)
                    break

    print()
    print("당신의 %s학기 시간표는 이렇게 완성되었습니다." %(b))
    tita(AAA,BBB,CCC,DDD,EEE,FFF,GGG,HHH,AA,BB,CC,DD,EE)

    i=input("다시 짜고 싶으시면 0을, 종료하고 싶으시면 아무 키나 눌러주세요.")
    if i=="0":
        print()
        print()
        print("***잠시 후 다시 시작됩니다***")
        print()
        print()
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print()
        print()
        continue
    else:
        exit()
    
