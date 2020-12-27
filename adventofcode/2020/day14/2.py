#!/usr/bin/env python3
import bisect
import fileinput
import heapq
from collections import Counter, defaultdict, deque
from functools import lru_cache

lines = [l.strip() for l in fileinput.input()]

def memaddrs(mask, addr):
    submask = 0
    for i in range(36):
        if mask[35 - i] == 'X':
            submask |= (1 << i)
            addr = addr & (~(1 << i))
        elif mask[35 - i] == '1':
            addr |= (1 << i)
    yield addr | submask
    nextmask = submask
    while True:
        nextmask = (nextmask - 1) & submask
        yield addr | nextmask
        if nextmask == 0: break

vals = dict()
mask = ''
for line in lines:
    k, v = line.split(' = ')
    if k == 'mask':
        mask = v
    else:
        k = int(k[:-1].split('[')[-1])
        v = int(v)
        for m in memaddrs(mask, k):
            vals[m] = v

print(sum(vals.values()))