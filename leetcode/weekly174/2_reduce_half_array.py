'''
https://leetcode.com/contest/weekly-contest-174/problems/reduce-array-size-to-the-half/
'''
from collections import defaultdict

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = defaultdict(lambda: 0)
        for a in arr: counts[a] += 1
        
        ordered = sorted(set(arr), key=lambda e: -counts[e])
        c, i = 0, 0
        for e in ordered:
            c += counts[e]
            i += 1
            if c >= len(arr) // 2: break
        return i
            
