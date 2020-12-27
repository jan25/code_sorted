#!/usr/bin/python3

c = list('614752839')

def dec(i):
    i = int(i) - 1
    if i == 0: i = 9
    return str(i)

def move(c):
    t = c[1:4]
    c[1:4] = []
    val = dec(c[0])
    while val in t:
        val = dec(val)

    i = c.index(val)
    print(t, c, i)
    c[i+1:i+1] = t
    return c[1:] + [c[0]]

for _ in range(100):
    c = move(c)
    print(c)

i = c.index('1')
print(''.join(c[i+1:] + c[:i]))