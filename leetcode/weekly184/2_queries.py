'''
https://leetcode.com/contest/weekly-contest-184/problems/queries-on-a-permutation-with-key/
'''
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        l = list(range(m + 1))[1:]
        li = {e: i for i, e in enumerate(l)}
        r = []
        for e in queries:
            i = li[e]
            r.append(i)
            for j in range(i - 1, -1, -1):
                li[l[j]] = j + 1
                l[j + 1] = l[j]
            l[0] = e
            li[e] = 0
        return r
    
