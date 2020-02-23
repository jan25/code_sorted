'''
https://leetcode.com/contest/weekly-contest-176/problems/construct-target-array-with-multiple-sums/
'''
from heapq import heappush, heappop, heapify

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        h = [-e for e in target]
        tot = sum(target)
        heapify(h)
        
        def push(e):
            heappush(h, -e)
        def pop():
            return -1 * heappop(h)
        
        while h[0] != -1:
            t = pop()
            remaining = tot - t
            if t <= remaining or remaining == 0:
                return False
            rem_t = t % remaining
            push(rem_t)
            tot -= t - rem_t
            
        return True