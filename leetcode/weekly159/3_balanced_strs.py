'''
https://leetcode.com/contest/weekly-contest-159/problems/replace-the-substring-for-balanced-string/
'''
D = {a: i for i, a in enumerate('QWER')}

def to_int(c):
    return D[c]

class Solution:
    def possible(self, l):
        for i in range(self.n):
            if i + l > self.n: break
            req = self.n // 4
            diff = 0
            for j in range(4):
                tot = 0
                if i > 0: tot += self.s[i - 1][j]
                if i + l < self.n:
                    tot += self.s[-1][j] - self.s[i + l - 1][j]
                if tot > req:
                    diff += l + 1
                    break
                diff += req - tot    
            if diff == l: return True
        return False
    
    def balancedString(self, sx: str) -> int:
        n = len(sx)
        self.n = n
        s = []
        for c in sx:
            ss = [0, 0, 0, 0]
            ic = to_int(c)
            ss[ic] = 1
            if len(s) > 0:
                for i in range(4):
                    ss[i] += s[-1][i]
            s.append(ss)
        ss = s[-1]
        if ss[0] == ss[1] and ss[1] == ss[2] and ss[2] == ss[3]:
            return 0
        self.s = s
        l, r = 1, n
        while l < r:
            m = (l + r) >> 1
            if self.possible(m):
                r = m
            else: l = m + 1
        return l
    