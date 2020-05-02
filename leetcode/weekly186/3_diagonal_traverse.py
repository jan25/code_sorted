'''
https://leetcode.com/contest/weekly-contest-186/problems/diagonal-traverse-ii/
'''
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        stk = []
        for i, row in enumerate(nums[::-1]):
            stk.append([len(nums) - i - 1, row[::-1]])
        
        diag = []
        maxi = 0
        while stk:
            other_stk = []
            while stk and stk[-1][0] <= maxi:
                row = stk.pop()
                other_stk.append(row)
            while other_stk:
                row = other_stk.pop()
                diag.append(row[1].pop())
                if row[1]: stk.append(row)
            maxi += 1
        
        return diag
    
