'''
https://leetcode.com/contest/weekly-contest-176/problems/count-negative-numbers-in-a-sorted-matrix/
'''
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        neg = 0
        for i in range(m - 1, -1, -1):
            if grid[n - 1][i] >= 0: break
            for j in range(n - 1, -1, -1):
                if grid[j][i] >= 0: break
                neg += 1
        return neg
    