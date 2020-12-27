#!/usr/bin/python3
import fileinput

nums = []
for l in fileinput.input():
    nums.append(int(l.strip()))

pre = 25

def first():
    for i in range(pre, len(nums)):
        paired = False
        for j in range(i - pre, i):
            for k in range(j + 1, i):
                if nums[j] + nums[k] == nums[i]:
                    paired = True
                    break
            if paired: break
        if not paired: return i

def solve():
    i = first()
    seen = dict()
    seen[nums[0]] = 0
    cumsum = nums[0]
    for j in range(1, i):
        cumsum += nums[j]
        if cumsum - nums[i] in seen:
            k = seen[cumsum - nums[i]]
            if j - k > 1:
                return nums[k + 1:j + 1]
        if cumsum not in seen:
            seen[cumsum] = j

s = solve()
print(min(s) + max(s))