'''
https://leetcode.com/contest/weekly-contest-182/problems/find-lucky-integer-in-an-array/
'''
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        for a in sorted(arr)[::-1]:
            if a == arr.count(a):
                return a
        return -1
    
