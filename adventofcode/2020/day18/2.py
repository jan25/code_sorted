#!/usr/bin/python3
import fileinput
from collections import deque

lines = []
for l in fileinput.input():
    lines.append(l.strip())

def tokenize(l):
    l = l.replace(' ', '')
    tokens = []
    for ch in l:
        if ch.isdigit(): tokens.append(int(ch))
        else: tokens.append(ch)
    return tokens

def closing(t, i):
    starts = 0
    for j in range(i, len(t)):
        if t[j] == '(': starts += 1
        elif t[j] == ')': starts -= 1
        if starts == 0: return j

def solve(t):
    i = 0
    nums, ops = [], []
    while i < len(t):
        if t[i] == '(':
            j = closing(t, i)
            t[i:j + 1] = [solve(t[i + 1:j])]
        if t[i] not in set('*+()'): nums.append(t[i])        
        else: ops.append(t[i])
        i += 1
    
    for currop in ('+', '*'):
        nums, ops = deque(nums), deque(ops)
        for _ in range(len(ops)):
            a, b = nums.popleft(), nums.popleft()
            op = ops.popleft()
            if currop == op:
                b = (b + a) if op == '+' else (b * a)
                nums.appendleft(b)
            else:
                ops.append(op)
                nums.append(a)
                nums.appendleft(b)
    return nums.pop()

print(sum(map(solve, map(tokenize, lines))))
