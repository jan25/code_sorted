'''
https://leetcode.com/contest/weekly-contest-173/problems/minimum-difficulty-of-a-job-schedule/
'''
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d: return -1
        
        inf = 10 ** 9
        
        cache = {}
        def schedule(i, d):
            if i == n:
                return 0 if d == 0 else inf
            if d == 0: return inf
            if (i, d) not in cache:
                min_sol, max_sofar = inf, -1
                for j in range(i, n):
                    max_sofar = max(max_sofar, jobDifficulty[j])
                    min_sol = min(min_sol, max_sofar + schedule(j + 1, d - 1))
                cache[(i, d)] = min_sol
            return cache[(i, d)]
        
        return schedule(0, d)
    