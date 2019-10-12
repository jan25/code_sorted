'''
https://leetcode.com/contest/weekly-contest-157/problems/path-with-maximum-gold/
Shamelessy looked at Discussions to understand how this is done
'''

def next_steps(i, j):
    for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        yield (i + d[0], j + d[1])

class Solution:
    def invalid(self, x, y):
        return x < 0 or y < 0 or x >= self.n or y >= self.m or self.vis[x][y] or self.g[x][y] == 0
    
    def max_gold(self, x, y):
        if self.invalid(x, y): return 0
        mg = 0
        self.vis[x][y] = True
        for a, b in next_steps(x, y):
            mg = max(mg, self.max_gold(a, b))
        self.vis[x][y] = False
        return mg + self.g[x][y]
    
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.n, self.m = len(grid), len(grid[0])
        self.g = grid
        max_gold = 0
        self.vis = [[False for _ in range(self.m)] for _ in range(self.n)]
        for x in range(self.n):
            for y in range(self.m):
                max_gold = max(max_gold, self.max_gold(x, y))
        return max_gold
        