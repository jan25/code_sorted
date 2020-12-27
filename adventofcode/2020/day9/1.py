#!/usr/bin/python3
import fileinput

nums = []
for l in fileinput.input():
    nums.append(int(l.strip()))

def first():
    for i in range(25, len(nums)):
        paired = False
        for j in range(i - 25, i):
            for k in range(j + 1, i):
                if nums[j] + nums[k] == nums[i]:
                    paired = True
                    break
            if paired: break
        if not paired: return nums[i]

print(first())
