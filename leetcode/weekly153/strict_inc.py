'''
https://leetcode.com/contest/weekly-contest-153/problems/make-array-strictly-increasing/
Seems like LC Python3 environment is broken, I see expected output consitently with my output for this. But i get WA on Submit for same test case.
Edit:
Fixed py3 issue
See https://leetcode.com/discuss/general-discussion/381888/issues-with-python3-environment/343057 and https://docs.python-guide.org/writing/gotchas/
'''
import bisect

class Compressor:
    def __init__(self, l):
        self.keys = {}
        self.nexti = 0
        self.compress(l)

    def compress(self, l):
        l = sorted(l)
        for a in l:
            if a not in self.keys:
                self.keys[a] = self.nexti
                self.nexti += 1

    def transform(self, l):
        for i in range(len(l)):
            l[i] = self.keys[l[i]]
            
    def reset(self):
        self.keys = {}
        self.nexti = 0

class Solution:
    def __init__(self):
        self.inf = 10**9

    def find_next_last(self, e, l):
        if e <= l[0]: return None
        li = bisect.bisect_left(l, e - 1)
        if li == len(l) or l[li] > e - 1: li -= 1
        return l[li]

    def dp(self, ai, last, a, b, memo):
        if ai < 0: return 0
        if (ai, last) in memo:
            return memo[(ai, last)]
        sol = self.inf
        if a[ai] < last:
            sol = min(sol, self.dp(ai - 1, a[ai], a, b, memo))
        next_last = self.find_next_last(last, b)
        if next_last is not None:
            sol = min(sol, 1 + self.dp(ai - 1, next_last, a, b, memo))
        memo[(ai, last)] = sol
        return sol
    
    def clone(self, l):
        return [a for a in l]

    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = self.clone(arr1)
        arr2 = self.clone(arr2)
        c = Compressor(arr1 + arr2)
        c.transform(arr1); c.transform(arr2)
        c.reset()
        arr2.sort()
        sol = self.dp(len(arr1) - 1, self.inf, arr1, arr2, {})
        if sol >= self.inf: sol = -1
        return sol
