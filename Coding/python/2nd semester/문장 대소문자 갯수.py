import time

sentence = input()
cal= {}
for char in sentence:
    cal[char]=sentence.count(char)

print(cal)
time.sleep(0,7)
exit()
