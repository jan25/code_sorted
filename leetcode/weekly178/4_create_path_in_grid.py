'''
https://leetcode.com/contest/weekly-contest-178/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

We can reach a set of cells from (0, 0). Imagine all these cells are at level 0
Now hopping to next level would be to change the direction of one or more cells in level 0

Level wise traversal can be done with BFS
within a level traversal can be done by DFS
'''
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        inf = float('inf')
        n, m = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        q, d = [], 0
        dist = [[inf for j in range(m)] for i in range(n)]
        
        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m or dist[x][y] < inf:
                return
            dist[x][y] = d
            q.append((x, y))
            dfs(x + dirs[grid[x][y] - 1][0], y + dirs[grid[x][y] - 1][1])
            
        dfs(0, 0)
        # bfs
        while q:
            q2 = q
            q = []
            d += 1
            for x, y in q2:
                for dx, dy in dirs:
                    dfs(x + dx, y + dy)
        
        return dist[-1][-1]
    
