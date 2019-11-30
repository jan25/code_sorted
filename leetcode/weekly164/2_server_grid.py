'''
https://leetcode.com/contest/weekly-contest-164/problems/count-servers-that-communicate/
'''
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        def toi(i, j):
            return i * m + j
        
        s = [-1] * 62500
        
        def top(i):
            if s[i] < 0: return i
            s[i] = top(s[i])
            return s[i]
        
        def union(i, j):
            i = top(i); j = top(j)
            if i == j: return
            if s[i] > s[j]: i, j = j, i
            s[i] += s[j]
            s[j] = i
            
        def do_union(f, r, c):
            if grid[r][c] == 1:
                if f is not None: union(f, toi(r, c))
                else: f = toi(r, c)
            return f
        
        for r in range(n):
            f = None
            for c in range(m):
                f = do_union(f, r, c)
        for c in range(m):
            f = None
            for r in range(n):
                f = do_union(f, r, c)
        
        return -1 * sum(c for c in s if c < -1)
        