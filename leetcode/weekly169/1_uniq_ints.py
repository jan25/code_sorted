'''
https://leetcode.com/contest/weekly-contest-169/problems/find-n-unique-integers-sum-up-to-zero/
'''
class Solution:
    def sumZero(self, n: int) -> List[int]:
        l, r = list(reversed(range(1, 1 + n // 2))), list(range(1, 1 + n // 2))
        l = list(map(lambda a: -a, l))
        if n % 2 == 1: l.append(0)
        return l + r
    