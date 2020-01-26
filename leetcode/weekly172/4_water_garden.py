'''
https://leetcode.com/contest/weekly-contest-172/problems/minimum-number-of-taps-to-open-to-water-a-garden/
'''
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        rm = [0] * (n + 1)
        
        for i, rang in enumerate(ranges):
            l, r = max(0, i - rang), min(n, i + rang)
            rm[l] = r
        
        inf = 10 ** 5
        
        cache = {}
        def solve(i, r):
            if i == n: return 0
            if (i, r) not in cache:
                sol = inf
                if r >= 0:
                    sol = inf
                    if r > 0: sol = solve(i + 1, r - 1)
                    if rm[i] > 0:
                        d = rm[i] - i
                        sol = min(sol, 1 + solve(i + 1, max(d - 1, r - 1)))
                else:
                    return inf
                cache[(i, r)] = sol
            return cache[(i, r)]
        
        taps = solve(0, 0)
        return -1 if taps == inf else taps
    