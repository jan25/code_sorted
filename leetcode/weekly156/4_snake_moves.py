'''
https://leetcode.com/contest/weekly-contest-156/problems/minimum-moves-to-reach-target-with-rotations/
'''

class Pos:
    def __init__(self, x, y, h=True):
        self.x = x
        self.y = y
        self.h = h
        self.d = 0
        
    def to_int(self):
        h = 1 if self.h else 0
        return (self.x << 17) | (self.y << 9) | h

class Solution:
    def is_dest(self, p):
        return p.x == self.n - 1 and p.x == p.y and p.h
    
    def move(self, p):
        self.vis.add(p.to_int())
        self.q.append(p)
        
    def valid_move(self, p, rotation=False):
        x, y = p.x, p.y
        tx, ty = p.x, p.y
        if p.h: ty -= 1
        else: tx -= 1
        if x >= self.n or y >= self.n:
            return False
        if self.g[x][y] + self.g[tx][ty] > 0:
            return False
        if p.to_int() in self.vis:
            return False
        if rotation and self.g[x][y] + self.g[tx + 1][ty + 1] > 0:
            return False
        return True
    
    def push_next(self, p):
        # vertical move
        np = Pos(p.x + 1, p.y, p.h)
        np.d = p.d + 1
        if self.valid_move(np):
            self.move(np)
            
        # horizontal move
        np = Pos(p.x, p.y + 1, p.h)
        np.d = p.d + 1
        if self.valid_move(np):
            self.move(np)
        
        # rotation
        if p.h:
            np = Pos(p.x + 1, p.y - 1, h=False)
        else:
            np = Pos(p.x - 1, p.y + 1, h=True)
        np.d = p.d + 1
        if self.valid_move(np, rotation=True):
            self.move(np)
    
    def minimumMoves(self, grid: List[List[int]]) -> int:
        self.g = grid
        self.n = len(grid)
        
        p = Pos(0, 1)
        self.vis = {p.to_int()}
        self.q, i = [p], 0
        while i < len(self.q):
            p = self.q[i]; i += 1
            if self.is_dest(p):
                return p.d
            self.push_next(p)
        return -1
    