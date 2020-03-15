'''
https://leetcode.com/contest/weekly-contest-179/problems/time-needed-to-inform-all-employees/
'''
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        maxt = [-1] * n
        maxt[headID] = 0
        
        def dfs(c):
            if c == -1 or maxt[c] != -1: return
            m = manager[c]
            dfs(m)
            maxt[c] = max(maxt[c], maxt[m] + informTime[m])
        
        for c in range(n): dfs(c)
        
        return max(maxt)
    
