'''
https://leetcode.com/problems/majority-element-ii/
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elema, elemb = -1, -1
        counta, countb = 0, 0
        
        for num in nums:
            if num == elema:
                counta += 1
            elif num == elemb:
                countb += 1
            elif counta == 0:
                counta = 1
                elema = num
            elif countb == 0:
                countb = 1
                elemb = num
            else:
                counta -= 1
                countb -= 1
            
        n = len(nums)
        result = []
        if sum(1 for a in nums if a == elema) > n // 3:
            result.append(elema)
        if sum(1 for a in nums if a == elemb) > n // 3:
            result.append(elemb)
            
        return result
            
