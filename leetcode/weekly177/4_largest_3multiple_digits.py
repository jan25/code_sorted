'''
https://leetcode.com/contest/weekly-contest-177/problems/largest-multiple-of-three/
'''
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        if sum(digits) == 0: return '0'
        
        twos = sorted(filter(lambda d: d % 3 == 2, digits), reverse=1)
        ones = sorted(filter(lambda d: d % 3 == 1, digits), reverse=1)
        final = list(filter(lambda d: d % 3 == 0, digits))

        ti, oi = 0, 0
        while ti + 3 < len(twos):
            ti += 3
        while oi + 3 < len(ones):
            oi += 3
        final += twos[:ti] + ones[:oi]
        
        twos, ones = twos[ti:], ones[oi:]
        rt, ro = len(twos), len(ones)
        if rt > ro:
            ti, oi = oi, ti
            twos, ones = ones, twos
        if rt == ro:
            final += twos + ones
        elif 2 in (rt, ro):
            mto = min(rt, ro)
            final += twos[:mto] + ones[:mto]
        elif len(ones) == 3:
            final += ones
        
        final.sort(reverse=1)
        return ''.join(map(str, final))
    
