from random import choice

with open('valid.txt') as f:
    diction = f.read().split('\n')

def say(log):
    words = []
    for l in diction:
        if l[0]==log[-1][-1]:
            words.append(l)
    k = choice(words)
    diction.remove(k)
    return k

def name():
    return "용진"
