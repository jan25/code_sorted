'''
https://leetcode.com/contest/weekly-contest-165/problems/number-of-burgers-with-no-waste-of-ingredients/

Two linear equations solution
'''
class Solution:
    def numOfBurgers(self, t: int, c: int) -> List[int]:
        if t % 2 != 0: return []
        t //= 2
        t -= c
        c -= t
        if t < 0 or c < 0: return []
        return [t, c]
    