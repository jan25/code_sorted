'''
https://leetcode.com/contest/weekly-contest-168/problems/maximum-candies-you-can-get-from-boxes/
'''
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        q, qi = [b for b in initialBoxes], 0
        done = set()
        seen = [1000] * len(status)
        
        c = 0
        while qi < len(q):
            b = q[qi]; qi += 1
            if b in done: continue
            if status[b] == 0:
                if seen[b] == 0: break
                q.append(b)
                seen[b] -= 1
                continue
            c += candies[b]
            done.add(b)
            for k in keys[b]:
                status[k] = 1
            for cb in containedBoxes[b]:
                q.append(cb)
        
        return c
            