'''
https://leetcode.com/contest/weekly-contest-171/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
'''
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def noz(a):
            return a == 0 or (a % 10 != 0 and noz(a // 10))
        
        for a in range(1, n + 1):
            if noz(a) and noz(n - a):
                return [a, n - a]
            