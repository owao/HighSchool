with open('단어목록.txt') as f:
    dic=f.read().split('\n')

p=set(dic)

noun=open("명사.txt",'w')
verb=open("동사.txt",'w')
adj=open("형용사.txt",'w')
adv=open("부사.txt",'w')


for i in p:
    print(i)
    a=input()
    if a=="1":
        noun.write(i)
    if a=="3":
        adj.write(i)
    if a=="2":
        verb.write(i)
    if a=="4":
        adv.write(i)

dic.close()
noun.close()
verb.close()
adj.close()
adv.close()
