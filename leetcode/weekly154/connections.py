'''
https://leetcode.com/contest/weekly-contest-154/problems/critical-connections-in-a-network/
'''
class Solution:
    def dfs(self, v, par=-1):
        if self.visited[v]: return
        self.visited[v] = True
        self.tin[v] = self.low[v] = self.t
        self.t += 1
        for to in self.g[v]:
            if to == par: continue
            if not self.visited[to]:
                self.dfs(to, v)
            self.low[v] = min(self.low[v], self.low[to])
            if self.low[to] > self.tin[v]:
                self.crit.append([v, to])

    def add_edge(self, u, v):
        if u not in self.g: self.g[u] = []
        self.g[u].append(v)
    
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.g = {}
        for c in connections:
            u, v = c
            self.add_edge(u, v)
            self.add_edge(v, u)
        
        self.visited = [False] * n
        self.tin = [-1] * n
        self.low = [-1] * n
        self.crit = []
        self.t = 1
        for i in range(n): self.dfs(i)
        return self.crit