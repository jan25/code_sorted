'''
https://leetcode.com/contest/weekly-contest-168/problems/find-numbers-with-even-number-of-digits/
'''
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        def count_digs(n):
            if n == 0: return 0
            return 1 + count_digs(n // 10)
        
        return sum((count_digs(n) & 1 ^ 1) for n in nums)
    