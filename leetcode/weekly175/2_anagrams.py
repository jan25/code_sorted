'''
https://leetcode.com/contest/weekly-contest-175/problems/minimum-number-of-steps-to-make-two-strings-anagram/
'''
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sc, tc = {c: 0 for c in s}, {c: 0 for c in t}
        for c in s: sc[c] += 1
        for c in t: tc[c] += 1
        
        steps = 0
        for c, v in sc.items():
            if c not in tc: steps += v
            elif sc[c] > tc[c]: steps += sc[c] - tc[c]
        return steps
                
