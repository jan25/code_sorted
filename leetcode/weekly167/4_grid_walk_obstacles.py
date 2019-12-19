'''
https://leetcode.com/contest/weekly-contest-167/problems/shortest-path-in-a-grid-with-obstacles-elimination/

Improvised BFS with visited state being (row, column, number_of_seen_obstacles)
'''
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        r, c = len(grid), len(grid[0])
        
        # Node represents a visited node in the graph using BFS
        # hash and eq are necessary so the python set would work correcly
        # addition and find on set requires hash of two elements to be the same and
        # it also looks at eq method to figure if two different objects are not infact equal
        class Node:
            def __init__(self, r, c, seen_k, dist):
                self.r = r
                self.c = c
                self.seen_k = seen_k
                self.dist = dist
            
            def __hash__(self):
                return self.seen_k * 10000 + self.r * 100 + self.c
            
            def __eq__(self, other):
                return self.r == other.r and self.c == other.c and self.seen_k == other.seen_k
        
        def valid_cell(x, y):
            return x >= 0 and y >= 0 and x < r and y < c
        
        def moves(x, y):
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                yield (x + dx, y + dy)
        
        vis = set()
        start = Node(0, 0, grid[0][0], 0)
        vis.add(start)
        q, i = [start], 0
        while i < len(q):
            n = q[i]; i += 1
            if n.r == r - 1 and n.c == c - 1:
                return n.dist
            for rc in moves(n.r, n.c):
                new_r, new_c = rc
                if valid_cell(new_r, new_c):
                    if grid[new_r][new_c] == 1:
                        new_n = Node(new_r, new_c, n.seen_k + 1, n.dist + 1)
                        if n.seen_k < k and new_n not in vis:
                            q.append(new_n)
                            vis.add(new_n)
                    else:
                        new_n = Node(new_r, new_c, n.seen_k, n.dist + 1)
                        if new_n not in vis:
                            q.append(new_n)
                            vis.add(new_n)
        return -1
        