'''
https://leetcode.com/contest/weekly-contest-158/problems/maximum-equal-frequency/
'''

class Solution:
    def f(self, co, c, l):
        if c == 1 and l == co[1]: return True
        if 1 not in co or co[1] != 1: return False
        if (l - 1) in co and co[l - 1] * (l - 1) == l - 1:
            return True
        for a in range(2, l):
            if a * a >= l: break
            if (l - 1) % a > 0: continue
            i, j = a, (l - 1) // a
            if i in co and i * co[i] == (l - 1):
                return True
            if j in co and j * co[j] == (l - 1):
                return True
        return False
        
    def maxEqualFreq(self, nums: List[int]) -> int:
        ac, co = {}, {}
        ef = 1
        for i, a in enumerate(nums):
            if a not in ac: ac[a] = 0
            else: co[ac[a]] -= 1
            ac[a] += 1
            if ac[a] not in co: co[ac[a]] = 0
            co[ac[a]] += 1
            
            c = ac[a]
            l = i + 1
            # odd one out
            if self.f(co, c, l): ef = max(ef, l)
            # one of others
            if c - 1 in co and co[c] == 1 and (c - 1) * co[c - 1] == l - c:
                ef = max(ef, l)
            if c + 1 in co and co[c + 1] == 1 and c * co[c] == l - (c + 1):
                ef = max(ef, l)
            if c == l: ef = max(ef, l)
                
        return ef
        