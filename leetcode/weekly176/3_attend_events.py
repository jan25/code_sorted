'''
https://leetcode.com/contest/weekly-contest-176/problems/maximum-number-of-events-that-can-be-attended/
'''
from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        maxd = max(e[1] for e in events)
        events.sort()
        h = [] # min-heap on event end day
        
        ei, attend = 0, 0
        for d in range(1, maxd + 1):
            while h and h[0] < d:
                heappop(h)
            while ei < len(events) and events[ei][0] <= d:
                heappush(h, events[ei][1])
                ei += 1
            if h:
                heappop(h)
                attend += 1
        
        return attend
            