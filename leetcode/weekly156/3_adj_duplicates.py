'''
https://leetcode.com/contest/weekly-contest-156/problems/remove-all-adjacent-duplicates-in-string-ii/
'''
class C:
    def __init__(self, c):
        self.c = c
        self.n = 1
        
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        for c in s:
            if len(stk) > 0:
                tc = stk[-1]
                if tc.c == c:
                    tc.n += 1
                    tc.n %= k
                    if tc.n == 0: stk.pop()
                    continue
            stk.append(C(c))
        
        return ''.join([c.c * c.n for c in stk])
    