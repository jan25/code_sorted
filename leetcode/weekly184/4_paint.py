'''
https://leetcode.com/contest/weekly-contest-184/problems/number-of-ways-to-paint-n-3-grid/
'''
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        def toHash(i, j, k):
            return 100 * i + 10 * j + k
        
        possibles = []
        for i in range(1, 4):
            for j in range(1, 4):
                if i == j: continue
                for k in range(1, 4):
                    if j == k: continue
                    possibles.append(toHash(i, j, k))
        
        def validPossibles(a, b):
            while a > 0:
                if a % 10 == b % 10:
                    return False
                a //= 10; b //= 10
            return True
        
        sols = {}
        def solve(row=0, h=0):
            if row == n: return 1
            if (row, h) not in sols:
                csol = 0
                for p in possibles:
                    if h == 0 or validPossibles(p, h):
                        csol += solve(row + 1, p)
                sols[(row, h)] = csol % MOD
            return sols[(row, h)]
        
        return solve()
    
