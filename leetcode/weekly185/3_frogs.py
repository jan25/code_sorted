'''
https://leetcode.com/contest/weekly-contest-185/problems/minimum-number-of-frogs-croaking/
'''
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        cr = 'croak'
        
        def nextChar(c):
            if c == cr[-1]: return
            for i, cc in enumerate(cr):
                if c == cc: return cr[i + 1]
        
        stacks = {c: [] for c in cr[1:]}
        for i, c in enumerate(croakOfFrogs):
            if c != cr[0]: stacks[c].append(i)
        for c in stacks:
            stacks[c].reverse()
        
        def pop_and_get_ki(i):
            c = cr[1]
            j = None
            while nextChar(c):
                if stacks[c]:
                    j = stacks[c].pop()
                    if j > i:
                        i = j
                        c = nextChar(c)
                    else: return
                else: return
            if not stacks[c]: return
            j = stacks[c].pop()
            if j > i: return j
        
        h = []
        f = 0
        for i, c in enumerate(croakOfFrogs):
            if c == 'c':
                ki = pop_and_get_ki(i)
                if ki is None: return -1
                if len(h) > 0:
                    if h[0] > i:
                        f += 1
                        heapq.heappush(h, ki)
                    else:
                        heapq.heappop(h)
                        heapq.heappush(h, ki)
                else:
                    f = 1
                    h.append(ki)
        
        for c in stacks:
            if stacks[c]: return -1
        
        return f
        
