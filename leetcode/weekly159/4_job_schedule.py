'''
https://leetcode.com/contest/weekly-contest-159/problems/maximum-profit-in-job-scheduling/
'''
class Solution:
    def dp(self, i):
        if i >= self.n: return 0
        if i in self.c:
            return self.c[i]
        cc = self.dp(i + 1)
        e = self.e[self.id[i]]
        l, r = i + 1, self.n - 1
        while l < r:
            m = (l + r) >> 1
            if self.s[self.id[m]] >= e:
                r = m
            else: l = m + 1
        if l < self.n and self.s[self.id[l]] >= e:
            cc = max(cc, self.p[self.id[i]] + self.dp(l))
        else:
            cc = max(cc, self.p[self.id[i]])
        self.c[i] = cc
        return cc
    
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        self.n = len(profit)
        self.id = sorted(list(range(self.n)), key=lambda x: startTime[x])
        print(self.id)
        self.s = startTime
        self.e = endTime
        self.p = profit
        
        self.c = {}
        return self.dp(0)
        