'''
https://leetcode.com/contest/weekly-contest-185/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/
'''
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod = 10**9 + 7
        
        sols = dict()
        def sol(i, m, k, maxm):
            if i == n:
                if k == 0: return 1
                return 0
            
            if (i, m, k) in sols:
                return sols[(i, m, k)]

            c = 0
            for j in range(1, maxm + 1):
                if j > m:
                    c += sol(i + 1, j, k - 1, maxm)
                else:
                    c += sol(i + 1, m, k, maxm)
                c %= mod
                
            sols[(i, m, k)] = c
            return c
        
        return sol(0, 0, k, m)

