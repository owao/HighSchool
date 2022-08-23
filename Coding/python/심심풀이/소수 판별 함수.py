def prime_number(n):
    if n == 2:
        return True
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    ps = round(n**0.5) +1
    for ps in range(3, ps, 2):
        if n% ps == 0:
            return False
    else:
        return True

while True:
    num = input("Input a number: ")
    if prime_number(int(num)):
        print("True")
    else:
        print("False")
