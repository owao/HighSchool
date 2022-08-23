a=["p","r","n","c","s","s"]
b=["p","r","n","c","s","s"]
c=[]
d=0

def counting(a,b,c,d):
    for k in a:
        if k not in b:
            continue
        b.remove(k)
        c.append(k)
        d=d+1
        counting(a,b,c,d)
        b=a
        c=[]
    return d

asdf=counting(a,b,c,d)
print(asdf)

'''
for q in a:
    b.remove(q)
    c.append(q)
    for w in a:
        if w not in b:
            continue
        b.remove(w)
        c.append(w)
        for e in a:
            if e not in b:
                continue
            b.remove(e)
            c.append(e)
            for r in a:
                if r not in b:
                    continue
                b.remove(r)
                c.append(r)
'''
