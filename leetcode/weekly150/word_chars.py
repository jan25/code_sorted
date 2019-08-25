'''
https://leetcode.com/contest/weekly-contest-150/problems/find-words-that-can-be-formed-by-characters/
'''
def make_ds(s):
    ds = {}
    for c in s:
        if c not in ds: ds[c] = 0
        ds[c] += 1
    return ds

def can_do(a, b):
    ak = set(a.keys())
    for c in b.keys():
        if c not in ak or b[c] > a[c]: return False
    return True

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = make_ds(chars)
        sum_of_lens = 0
        for w in words:
            if can_do(c, make_ds(w)): sum_of_lens += len(w)
        return sum_of_lens