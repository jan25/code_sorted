#!/usr/bin/python3
import fileinput

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
    
    val = nums[0]
    for op, num in zip(ops, nums[1:]):
        if op == '+': val += num
        else: val *= num
    return val

print(sum(map(solve, map(tokenize, lines))))
