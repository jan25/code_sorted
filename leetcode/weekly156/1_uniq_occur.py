'''
https://leetcode.com/contest/weekly-contest-156/problems/unique-number-of-occurrences/
'''
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        h = {}
        for a in arr:
            if a not in h:
                h[a] = 0
            h[a] += 1
        uniq = h.values()
        return sorted(uniq) == sorted(list(set(uniq)))
