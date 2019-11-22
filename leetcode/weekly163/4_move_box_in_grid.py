'''
https://leetcode.com/contest/weekly-contest-163/problems/minimum-moves-to-move-a-box-to-their-target-location/

Algorithm:
BFS algorithm to crawl the grid through bfs tree to obtain minimum number of box pushes

Key:
Instead of normal boolean visited cells used in BFS, we can use a notion of visited edges. This allows visting same cell multiple times from different directions

'''
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        
        # extract grid metadata to work with
        s, b, t = None, None, None
        for i, r in enumerate(grid):
            for j, a in enumerate(r):
                if a == 'S':
                    s = [i, j]
                elif a == 'B':
                    b = [i, j]
                elif a == 'T':
                    t = [i, j]
                        
        # left right up down
        def lrud(u):
            for d in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                yield d
        
        # tells if (x, y) cell is within the grid
        def is_valid_pos(x, y):
            return x >= 0 and y >= 0 and x < n and y < m
        
        # to check if dest cell can be reached from cell u
        def dfs(u, dest, vis):
            if not is_valid_pos(*u): return False
            x, y = u
            if grid[x][y] == '#': return False
            if u == dest: return True
            if vis[x][y]: return False
            vis[x][y] = True
            reachable = False
            for dx, dy in lrud(u):
                reachable = dfs([x + dx, y + dy], dest, vis) or reachable
            return reachable
    
        # Finds from f cell whether we can reach t cell given box at b cell
        def is_reachable(f, t, b):
            vis = [[False] * m for _ in range(n)]
            c = grid[b[0]][b[1]]
            grid[b[0]][b[1]] = '#'
            r = dfs(f, t, vis)
            grid[b[0]][b[1]] = c
            return r
        
        # queue
        q, i = [(b, 0, None)], 0
        # visited edges used in bfs
        vis = [[set()] * m for _ in range(n)]
        
        # marks a move/edge as visited
        # when box is moved from cell par to cell v
        def mark_vis(v, par):
            vis[v[0]][v[1]].add((par[0], par[1]))
        
        # get next moves we can make for a given cell and parent cell the box moved from earlier
        def get_next_moves(cell, par):
            par = par if par else s
            moves = []
            for dx, dy in lrud(cell):
                x, y = cell[0] + dx, cell[1] + dy
                tx, ty = cell[0] - dx, cell[1] - dy
                if is_valid_pos(x, y) and grid[x][y] != '#' \
                    and (cell[0], cell[1]) not in vis[x][y] \
                    and is_valid_pos(tx, ty) and grid[tx][ty] != '#' \
                    and is_reachable(par, [tx, ty], cell):
                    moves.append([x, y])
            return moves

        # petty bfs
        while i < len(q):
            u = q[i]; i += 1
            if u[0] == t: return u[1]
            moves = get_next_moves(u[0], u[2])
            for mv in moves:
                mark_vis(mv, u[0])
                q.append((mv, u[1] + 1, u[0]))
        
        # by this point we didn't hit T cell
        return -1
    