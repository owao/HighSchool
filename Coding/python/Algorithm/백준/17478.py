def re_func(a,b): #제어 값/확인 값
    re_word1="\"재귀함수가 뭔가요?\""
    re_word2="\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어."
    re_word3="마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
    re_word4="그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""
    ans1="\"재귀함수가 뭔가요?\""
    ans2="\"재귀함수는 자기 자신을 호출하는 함수라네\""
    ans3="라고 답변하였지."
    s="____"
    while True:
        if a==0:
            print("%s%s"%(b*s,ans1))
            print("%s%s"%(b*s,ans2))
            print("%s%s"%(b*s,ans3))
            break
        else:
            print("%s%s"%((b-a)*s,re_word1))
            print("%s%s"%((b-a)*s,re_word2))
            print("%s%s"%((b-a)*s,re_word3))
            print("%s%s"%((b-a)*s,re_word4))
            a-=1
            re_func(a,b)
            print("%s%s"%((b-(a+1))*s,ans3))
            break


a=int(input()) #반복횟수
b=a
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
re_func(a,b)
