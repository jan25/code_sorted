'''
https://leetcode.com/contest/weekly-contest-155/problems/sort-items-by-groups-respecting-dependencies/
'''
class Solution:
    def dfs(self, v):
        if self.vis[v] == 2: return True
        self.vis[v] = 1
        ok = True
        for u in self.gg[v]:
            if u == v: continue
            ok = ok and self.vis[u] != 1
            if ok: ok = ok and self.dfs(u)
        self.vis[v] = 2
        self.order.append(v)
        return ok
    
    def g_dfs(self, v, g):
        if self.vis[v] == 2: return True
        self.vis[v] = 1
        ok = True
        for u in self.b[v]:
            if u not in self.g_map[g]:
                continue
            if self.vis[u] == 1: ok = False
            if ok: ok = ok and self.g_dfs(u, g)
        self.vis[v] = 2
        self.f_order.append(v)
        return ok
    
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        self.b = beforeItems
        self.g = group[:]
        next_m = m
        for i in range(n):
            if self.g[i] == -1:
                self.g[i] = next_m
                next_m += 1
        self.gg = {g : [] for g in range(next_m)}
        for i in range(n):
            for v in self.b[i]:
                self.gg[self.g[i]].append(self.g[v])
        
        # Topo sort groups if possible
        self.order = []
        self.vis = [0] * next_m # 0 !seen, 1 WIP, 2 Done
        for g in self.gg:
            if not self.dfs(g):
                return []
        
        # Topo sort within each group if possible
        self.g_map = {g: set() for g in range(next_m)}
        for i, a in enumerate(self.g):
            self.g_map[a].add(i)
        self.vis = [0] * n # 0 !seen, 1 WIP, 2 Done
        self.f_order = []
        for g in self.order:
            for v in self.g_map[g]:
                if not self.g_dfs(v, g):
                    return []
        return self.f_order
            