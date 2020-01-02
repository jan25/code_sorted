'''
https://leetcode.com/contest/weekly-contest-168/problems/maximum-number-of-occurrences-of-a-substring/
'''
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        max_c = 0
        c = {}
        for i in range(0, len(s) - minSize + 1):
            current_s = s[i:i + minSize]
            if len(set(current_s)) > maxLetters:
                continue
            if current_s not in c:
                c[current_s] = 0
            c[current_s] += 1
            max_c = max(max_c, c[current_s])
        return max_c
    