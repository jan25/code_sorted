'''
https://leetcode.com/contest/weekly-contest-154/problems/k-concatenation-maximum-sum/
'''
def the_usual(l):
    max_s, rs = 0, 0
    max_e = l[0]
    for a in l:
        max_e = max(max_e, a)
        rs += a
        if rs > 0:
            max_s = max(max_s, rs)
        else:
            rs = 0
    if max_e < 0: return max_e
    return max_s

def cum_sum(l):
    max_s, s = 0, 0
    for a in l:
        s += a
        max_s = max(s, max_s)
    return max_s

def solver(l, k):
    s = max(l)
    tot = sum(l)
    s = max(s, tot)
    s = max(s, tot * k)
    a, b = cum_sum(l), cum_sum(list(reversed(l)))
    s = max(s, a)
    s = max(s, b)
    if k > 1:
        s = max(s, a + b)
    if k > 2:
        s = max(s, a + b + (k - 2) * tot)
        s = max(s, a + (k - 2) * tot)
        s = max(s, b + (k - 2) * tot)
    s = max(s, the_usual(l))
    return s % (10**9 + 7)

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        return solver(arr, k)
