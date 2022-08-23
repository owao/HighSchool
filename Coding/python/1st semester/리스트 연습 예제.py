a=[30, 20, 50]


print("현재 리스트:",a)


a.append(40)
print("append(40) list:",a)
#리스트의 마지막에 하나의 값을 추가


a.pop()
print("pop() list:",a)
#현재의 가장 마지막 값을 제거
#pop(숫자)를 하면 그 숫자번째의 값을 제거


a.sort()
print("sort() list:",a)
#최소부터 정렬


a.reverse()
print("reverse() list:", a)
#리스트의 순서를 뒤집음
#정렬 XX


print("50의 위치는:",a.index(50))
#값의 위치를 헤아림


a.insert(2, 60)
print("insert(2,60) list:",a)
#insert(숫자1,숫자2) : 숫자1자리에 숫자2를 집어넣음


a.remove(60)
print("remove(60)후 list:",a)
#괄호 안의 값을 제거
#pop은 값을 나타낸 후 제거, remove는 그냥 제거


a.extend([70,80,20])
print("Extend()후 list:",a)
#원래 리스트에 입력한 리스트 값을 일일히 합침


a.sort(reverse=True)
print("reverse sort후 list:",a)
#내림차순 정렬


print("20의 갯수:",a.count(20))
#갯수를 헤아림








































print()
print()

asdf=[3,2,5,4,1]
asdf.sort(reverse=True)
print(asdf)



fdsa=[10,20,30,40,50]
fdsa.pop(0)
fdsa.pop(2)
print(fdsa)











