'''
https://leetcode.com/contest/weekly-contest-171/problems/minimum-flips-to-make-a-or-b-equal-to-c/
'''
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        f = 0
        while c > 0 or a > 0 or b > 0:
            cb = c % 2; c >>= 1
            ab, bb = a % 2, b % 2
            a >>= 1; b >>= 1
            if cb == ab | bb: continue
            if cb == 0: f += ab + bb
            else: f += 1
        return f
    