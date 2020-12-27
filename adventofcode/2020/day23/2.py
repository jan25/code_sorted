#!/usr/bin/python3

c = list(map(int, '614752839'))
for i in range(10, 10**6 + 1):
    c.append(i)

neighbor = dict()
for i in range(len(c)):
    j = (i + 1) % len(c)
    neighbor[c[i]] = c[j]

def move(val):
    cached = val
    first = neighbor[val]
    second = neighbor[first]
    third = neighbor[second]
    neighbor[val] = neighbor[third]
    val -= 1
    if val == 0: val = 10**6
    while val in {first, second, third}:
        val -= 1
        if val == 0: val = 10**6
    tail = neighbor[val]
    neighbor[val] = first
    neighbor[third] = tail
    return neighbor[cached]

val = c[0]
for _ in range(10**7 + 1):
    val = move(val)

prod = neighbor[1] * neighbor[neighbor[1]]
print(prod)
