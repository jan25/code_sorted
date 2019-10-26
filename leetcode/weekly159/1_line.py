'''
https://leetcode.com/contest/weekly-contest-159/problems/check-if-it-is-a-straight-line/
'''
class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        fx, fy = c[0]
        n, d = fy - c[1][1], fy - c[1][0]
        for x, y in c[2:]:
            if n * (x - fx) != d * (y - fy): return False
        return True
        