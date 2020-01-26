'''
https://leetcode.com/problems/majority-element/
'''class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majorityElem = -1
        
        for num in nums:
            if num == majorityElem:
                count += 1
            elif count == 0:
                count = 1
                majorityElem = num
            else:
                count -= 1
        
        return majorityElem
    
