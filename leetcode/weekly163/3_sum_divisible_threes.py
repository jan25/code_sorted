'''
https://leetcode.com/contest/weekly-contest-163/problems/greatest-sum-divisible-by-three/
'''
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # put nums into sorted remainder buckets
        b = [[] for _ in range(3)]
        nums.sort()
        for n in nums:
            b[n % 3].append(n)
        
        # combine remainder=2's list and remainder=1's list independently
        def be_smart(a, b):
            s = 0
            while len(a) >= 3:
                s += sum(a.pop() for _ in range(3))
            while len(b) >= 3:
                s += sum(b.pop() for _ in range(3))
            while len(a) > 0 and len(b) > 0:
                s += a.pop() + b.pop()
            return s
        
        # handle corner case
        # mix one or two from remainder=2's list with remainder=1's list
        l1, l2 = b[1], b[2]
        s1 = 0
        if len(l1) > 0 and len(l2) > 0:
            s1 = l1[-1] + l2[-1] + be_smart(l1[:-1], l2[:-1])
        s2 = 0
        if len(l1) > 1 and len(l2) > 1:
            s2 = sum(l1[-2:] + l2[-2:]) + be_smart(l1[:-2], l2[:-2])
        
        maxs = sum(b[0])
        maxs += max(s1, s2, be_smart(l1, l2))
        return maxs
    