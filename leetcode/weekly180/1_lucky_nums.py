'''
https://leetcode.com/contest/weekly-contest-180/problems/lucky-numbers-in-a-matrix/
'''
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        rmax, cmax = [10**6]*n, [0]*m
        for r in range(n):
            for c in range(m):
                rmax[r] = min(rmax[r], matrix[r][c])
                cmax[c] = max(cmax[c], matrix[r][c])
        l = []
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == rmax[r] and rmax[r] == cmax[c]:
                    l.append(rmax[r])
        return l
    
