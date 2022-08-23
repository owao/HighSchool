for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            if (10*a+b)+(10*b+a)==11*c:
                print("A: %d, B: %d, C:%d"%(a,b,c))
            c=c+1
        b=b+1
    a=a+1
