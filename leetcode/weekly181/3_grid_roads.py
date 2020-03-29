'''
https://leetcode.com/contest/weekly-contest-181/problems/check-if-there-is-a-valid-path-in-a-grid/

DFS algorithm with checks of possible previous cells for a currently visiting cell
'''
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        pre = [None, (0, -1), (-1, 0), (0, -1), (0, 1), (0, -1), (0, 1)]
        nex = [None, (0, 1),  (1, 0),  (1, 0),  (1, 0), (-1, 0), (-1, 0)]

        n, m = len(grid), len(grid[0])
        seen = set()
        
        def invalid_prev(x, y, px, py):
            c = grid[x][y]
            xp, yp = x + pre[c][0], y + pre[c][1]
            valid = xp == px and yp == py
            if valid: return 1
            xp, yp = x + nex[c][0], y + nex[c][1]
            valid = xp == px and yp == py
            if valid: return 2
            return 0
        
        def get_next(x, y, rev_prev):
            if rev_prev == 1:
                return x + nex[grid[x][y]][0], y + nex[grid[x][y]][1]
            if rev_prev == 2:
                return x + pre[grid[x][y]][0], y + pre[grid[x][y]][1]
        
        def invalid_pos(x, y):
            return x < 0 or y < 0 or x >= n or y >= m

        def dfs(x, y, px, py):
            if invalid_pos(x, y): return False
            if (x, y) in seen: return False
            rev_prev = invalid_prev(x, y, px, py)
            if rev_prev == 0: return False
            if x == n - 1 and y == m - 1: return True
            seen.add((x, y))
            nx, ny = get_next(x, y, rev_prev)
            return dfs(nx, ny, x, y)
        
        valid = False
        for d in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            seen = set()
            valid = valid or dfs(0, 0, *d)
        
        return valid
    
