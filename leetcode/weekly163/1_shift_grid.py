'''
https://leetcode.com/contest/weekly-contest-163/problems/shift-2d-grid/
'''
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        r = [[] for _ in range(n)]
        
        k %= (n * m)
        
        # treat grid as a flattened array and figure the k rotated indices
        for i in range(n * m):
            j = (n * m + i - k) % (n * m)
            x, y = j // m, j % m
            rx = i // m
            r[rx].append(grid[x][y])
            
        return r
            