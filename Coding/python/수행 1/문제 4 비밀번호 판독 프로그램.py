asdf=0
while asdf<5:
    a=int(input("Enter password: "))
    x=int(a//100)
    y=int((-100*x+a)/10)
    z=int(a -100*x -10*y)
    if (x+y+z)%7==0:
        if (x*z)%4==0:
            print("Incorrect Password!!")
            asdf=asdf+1
            continue
        else:
            print("Welcome!!")
            break
    else:
        print("Incorrect Password!!")
        asdf=asdf+1
        continue
if asdf==5:
    print("BYE!")
