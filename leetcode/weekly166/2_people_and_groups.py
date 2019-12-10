'''
https://leetcode.com/contest/weekly-contest-166/problems/group-the-people-given-the-group-size-they-belong-to/
'''
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = []
        h = {}
        for n, g in enumerate(groupSizes):
            if g not in h: h[g] = []
            h[g].append(n)
            if len(h[g]) == g:
                groups.append(h[g])
                h[g] = []
        return groups
    