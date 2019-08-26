'''
https://leetcode.com/contest/weekly-contest-150/problems/last-substring-in-lexicographical-order/

SA algorithm mostly copied from https://cp-algorithms.com/string/suffix-array.html
Status: tle. probably py3 lists
'''

class SuffixArray:
    def __init__(self, s):
        self.s = s
        self.n = len(s)
        self.p = [0] * self.n
        self.c = [0] * self.n
        c = self.preprocess()
        self.process(c)
    
    def preprocess(self):
        counter = [0] * 260
        for c in self.s:
            counter[ord(c)] += 1
        for i in range(1, len(counter)):
            counter[i] += counter[i - 1]
        for i in range(self.n):
            c = ord(self.s[i])
            counter[c] -= 1
            self.p[counter[c]] = i
        c = 0
        self.c[0] = c
        for i in range(1, self.n):
            if self.s[self.p[i]] != self.s[self.p[i - 1]]:
                c += 1
            self.c[self.p[i]] = c
        return c + 1
    
    def process(self, c):
        cn = [0] * self.n
        i = 0
        pn = [0] * self.n
        while (1 << i) < self.n:
            for j in range(self.n):
                pn[j] = self.p[j] - (1 << i)
                if pn[j] < 0: pn[j] += self.n
            counter = [0] * c
            for j in range(self.n):
                counter[self.c[pn[j]]] += 1
            for j in range(1, c):
                counter[j] += counter[j - 1]
            for j in range(self.n - 1, -1, -1):
                counter[self.c[pn[j]]] -= 1
                self.p[counter[self.c[pn[j]]]] = pn[j]
            cn[self.p[0]] = 0
            c = 1
            for j in range(1, self.n):
                a = [self.c[self.p[j]], self.c[(self.p[j] + (1 << i)) % self.n]]
                b = [self.c[self.p[j - 1]], self.c[(self.p[j - 1] + (1 << i)) % self.n]]
                if a != b: c += 1
                cn[self.p[j]] = c - 1
            self.c, cn = cn, self.c
            i += 1

class Solution:
    def lastSubstring(self, s: str) -> str:
        sa = SuffixArray(s)
        return s[sa.p[-1]:]
