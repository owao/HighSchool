a=int(input("How many bottles of beer on the wall?"))
b=a
print()
print("Okay! Let's start to count!\n")

while True:
    if b==2:
        print("2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n")
        b-=1
    if b==1:
        print("1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n")
        b-=1
    if b==0:
        ans=input("Do you want to buy more bottles of beer? y/n")
        print()
        if ans=="y":
            print("No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, %d bottles of beer on the wall.\n" %(a))
            b=a
        if ans=="n":
            print("No more bottles of beer on the wall, no more bottles of beer.")
            break
    else:
        print("%d bottles of beer on the wall, %d bottles of beer.\nTake one down and pass it around, %d bottles of beer on the wall.\n" %(b,b,b-1))
        b-=1
    
