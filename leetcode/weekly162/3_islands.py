'''
https://leetcode.com/contest/weekly-contest-162/problems/number-of-closed-islands/
'''
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        vis = [[False] * m for _ in range(n)]
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m:
                return False
            if vis[i][j] or grid[i][j] == 1: return True
            vis[i][j] = True
            what = True
            for d in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                ii, jj = i + d[0], j + d[1]
                what = dfs(ii, jj) and what
            return what
            
        isl = 0
        for x in range(n):
            for y in range(m):
                if not vis[x][y] and grid[x][y] == 0:
                    isl += int(dfs(x, y))

        return isl
    