#!/usr/bin/env python3
from collections import defaultdict

nums = list(map(int, '7,14,0,17,11,1,2'.split(',')))
last = defaultdict(list)
for i, num in enumerate(nums):
    last[num].append(i)

move = len(nums)
while move < 30000000:
    prev = nums[-1]
    speak = 0
    if len(last[prev]) > 1:
        speak = last[prev][-1] - last[prev][-2]
    last[speak].append(move)
    nums.append(speak)
    move += 1

print(nums[-1])