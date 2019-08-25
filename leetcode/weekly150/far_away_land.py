'''
https://leetcode.com/contest/weekly-contest-150/problems/as-far-from-land-as-possible/
'''
diffs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class Cell:
    def __init__(self, x, y, dist=0):
        self.dist = dist
        self.x, self.y = x, y

class Solver:
    def __init__(self, grid):
        self.g = grid
        self.l, self.w = len(self.g), len(self.g[0])
        self.inf = 1000
        self.dists = [[Cell(j, i, dist=self.inf) for i in range(self.w)] for j in range(self.l)]

    def solve(self):
        q, qi = [], 0
        lands = 0
        for i in range(self.l):
            for j in range(self.w):
                if self.g[i][j] == 1:
                    self.dists[i][j].dist = 0
                    q.append(self.dists[i][j])
                    lands += 1
        if lands == 0 or lands == self.l * self.w: return -1
        while len(q) - qi > 0:
            f = q[qi]; qi += 1
            for diff in diffs:
                x, y = f.x + diff[0], f.y + diff[1]
                if self.valid_xy(x, y) and self.makes_sense_to_q(x, y, f.dist + 1):
                    c = self.dists[x][y]
                    c.dist = f.dist + 1
                    q.append(c)
        return self.find_farthest_water()

    def find_farthest_water(self):
        max_dist = 0
        for i in range(self.l):
            for j in range(self.w):
                if self.g[i][j] == 0: # water
                    max_dist = max(max_dist, self.dists[i][j].dist)
        if max_dist == self.inf: return -1
        return max_dist

    def makes_sense_to_q(self, x, y, d):
        return self.dists[x][y].dist > d

    def valid_xy(self, x, y):
        return x >= 0 and y >= 0 and x < self.l and y < self.w

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        return Solver(grid).solve()
