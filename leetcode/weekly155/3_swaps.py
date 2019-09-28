'''
https://leetcode.com/contest/weekly-contest-155/problems/smallest-string-with-swaps/
'''
class Solution:
    def root(self, r):
        if self.g[r] < 0: return r
        r = self.root(self.g[r])
        return r
        
    def un(self, a, b):
        a, b = self.root(a), self.root(b)
        if a == b: return
        if self.g[a] > self.g[b]:
            a, b = b, a
        self.g[a] += self.g[b]
        self.g[b] = a
        
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.n = len(s)
        self.g = [-1] * self.n
        self.chars = {} # key -> [ char, ]
        
        for p in pairs: self.un(*p)
        for i in range(self.n):
            r = self.root(i)
            if r not in self.chars:
                self.chars[r] = []
            self.chars[r].append(s[i])
        for k in self.chars:
            self.chars[k] = sorted(self.chars[k])[::-1]
        
        sp = []
        for i in range(self.n):
            r = self.root(i)
            sp.append(self.chars[r].pop())
        return ''.join(sp)
        