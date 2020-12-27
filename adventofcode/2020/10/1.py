#!/usr/bin/env python3
import bisect
import fileinput
import heapq
from collections import Counter, defaultdict, deque
from functools import lru_cache

nums = [0] + [int(l.strip()) for l in fileinput.input()]
nums.sort()
ones, threes = 0, 1
for i in range(1, len(nums)):
    diff = nums[i] - nums[i - 1]
    if diff == 1: ones += 1
    if diff == 3: threes += 1

print(ones * threes)