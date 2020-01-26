'''
https://leetcode.com/contest/weekly-contest-172/problems/maximum-69-number/
'''
class Solution:
    def maximum69Number (self, num: int) -> int:
        stk = []
        while num > 0:
            stk.append(num % 10)
            num //= 10
        done = False
        while len(stk) > 0:
            if not done and stk[-1] == 6:
                stk[-1] = 9; done = True
            num = num*10 + stk[-1]
            stk.pop()
        return num
    