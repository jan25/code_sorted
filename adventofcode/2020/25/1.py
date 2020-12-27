#!/usr/bin/env python3
import bisect
import fileinput
import heapq
from collections import Counter, defaultdict, deque
from functools import lru_cache

lines = []
for l in fileinput.input(): lines.append(l.strip())
door, key = map(int, lines)
print(door, key)

div = 20201227

def getloop(pubkey):
    sub = 7
    val = 1
    loop = 0
    while val != door:
        val *= sub
        val %= div
        loop += 1
    return loop

doorl, keyl = getloop(door), getloop(key)

sub = key
val = 1
for _ in range(doorl):
    val *= sub
    val %= div
print(val)