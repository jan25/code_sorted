'''
https://leetcode.com/contest/weekly-contest-182/problems/count-number-of-teams/
'''
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        def nt(r):
            n = len(r)
            p = [0] * n
            for j in range(n - 2, -1, -1):
                for k in range(j + 1, n):
                    if r[k] > r[j]: p[j] += 1
            t = [0] * n
            for i in range(n - 2, -1, -1):
                for j in range(i + 1, n - 1):
                    if r[j] > r[i]: t[i] += p[j]
            return sum(t)
        
        return nt(rating) + nt(rating[::-1])
    
