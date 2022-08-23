with open('명사.txt') as f:
    noun=f.read().split('\n')
with open('동사.txt') as f:
    verb=f.read().split('\n')
with open('조사.txt') as f:
    asdf=f.read().split('\n')

from random import *



while True:
    a=choice(noun)
    b=choice(asdf)
    c=choice(noun)
    d=choice(asdf)
    e=choice(verb)
    print("%s%s %s%s %s" %(a,b,c,d,e))
    input()

noun.close()
verb.close()
d.close()
