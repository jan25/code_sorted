'''
https://leetcode.com/contest/weekly-contest-161/problems/minimum-swaps-to-make-strings-equal/
'''
class Solution:
    
    def minimumSwap(self, s1: str, s2: str) -> int:
        def c(s, c):
            return sum(1 for a in s if a == c)
        
        x = c(s1, 'x') + c(s2, 'x')
        y = c(s1, 'y') + c(s2, 'y')
        if x % 2 + y % 2 > 0: return -1
        
        xy, yx = 0, 0
        for a, b in zip(s1, s2):
            if a != b:
                if a == 'x': xy += 1
                else: yx += 1
        
        moves = xy // 2 + yx // 2
        xy %= 2; yx %= 2
        if xy + yx > 0: moves += 2

        return moves
    