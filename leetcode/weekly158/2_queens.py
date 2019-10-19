'''
https://leetcode.com/contest/weekly-contest-158/problems/queens-that-can-attack-the-king/
'''
class Solution:
    def f(self, dx, dy, x, y):
        if dx == 0 and dy == 0: return
        x += dx; y += dy
        if x < 0 or x >= 8 or y < 0 or y >= 8: return
        if [x, y] in self.q: return [x, y]
        return self.f(dx, dy, x, y)
    
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        self.q = queens
        return [self.f(dx, dy, *king) for dx in (1, -1, 0) for dy in (1, -1, 0) if self.f(dx, dy, *king)]
    