'''
https://leetcode.com/contest/weekly-contest-151/problems/compare-strings-by-frequency-of-the-smallest-character/
'''
class Solution:
    def f(self, s):
        s = [ord(c) for c in s]
        min_c = min(s)
        return sum([1 for c in s if c == min_c])
        
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        w = [self.f(x) for x in words]
        r = []
        for q in queries:
            y = self.f(q)
            r.append(sum([1 for x in w if x > y]))
        return r
