def a(x):
    k=x.read()
    a=len(k)
    b=k.count(" ")
    c=k.count("/n")
    r=a-(b+c)
    return r

def b(x):
    total=0
    for i in x.readlines():
        a=i.split()
        total+=len(a)
    return(total)

def c(x):
    total=0
    for i in x.readlines():
        a=i.split()
        total+=len(a)
    c_list=[]
    C=0
    for i in x:
        if i==" ":
            c_list.append(C)
            C=0
        C=C+1  
    d=0
    for i in c_list:
        d=d+i
    c=d/total

def pr(a,b,c,d):
    print("%s" %(a))
    print("- total characters: %d" %(b))
    print("- total words: %d" %(c))
    print("- average characters per words: %0.3f" %(d))
    
    

an=open("C:\Python33\\fire.txt", "r")
bn=open("C:\Python33\\wheel.txt", "r")
cn=open("C:\Python33\\lever.txt", "r")
dn=open("C:\Python33\\agriculture.txt", "r")
en=open("C:\Python33\\earthware.txt", "r")
A="fire.txt"
B="wheel.txt"
C="lever.txt"
D="agriculture.txt"
E="earthware.txt"

aa=A
ab=a(an)
ac=b(an)
ad=c(an)
pr(aa,ab,ac,ad)

ba=B
bb=a(bn)
bc=b(bn)
bd=c(bn)
pr(ba,bb,bc,bd)

ca=C
cb=a(cn)
cc=b(cn)
cd=c(cn)
pr(ca,cb,cc,cd)

da=D
db=a(dn)
dc=b(dn)
dd=c(dn)
pr(da,db,dc,dd)

ea=E
eb=a(en)
ec=b(en)
ed=c(en)
pr(ea,eb,ec,ed)


f=open("civiliazation.txt","a")
f.write(an.read())
f.write(bn.read())
f.write(cn.read())
f.write(dn.read())
f.write(en.read())
f.close()
an.close()
bn.close()
cn.close()
dn.close()
en.close()
