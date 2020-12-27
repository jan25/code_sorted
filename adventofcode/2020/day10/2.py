#!/usr/bin/env python3
import fileinput
from collections import defaultdict

nums = [int(l.strip()) for l in fileinput.input()]
nums.sort()
device = nums[-1] + 3
nums.append(device)

combinations = defaultdict(int)
combinations[device] = 1
for i in range(len(nums) - 1, -1, -1):
    for j in range(nums[i] + 1, nums[i] + 4):
        combinations[nums[i]] += combinations[j]

print(sum(combinations[i] for i in range(0, 4)))
