'''
https://leetcode.com/contest/weekly-contest-155/problems/minimum-absolute-difference/
'''
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = 10**7
        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i - 1])
        sarr = set(arr)
        return [[a, a + min_diff] for a in arr if a + min_diff in sarr]
