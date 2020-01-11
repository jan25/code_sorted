'''
https://leetcode.com/contest/weekly-contest-170/problems/decrypt-string-from-alphabet-to-integer-mapping/
'''
class Solution:
    def freqAlphabets(self, s: str) -> str:
        if len(s) == 0: return ''
        if s[-1] == '#':
            return self.freqAlphabets(s[:-3]) + chr(ord('a') - 1 + int(s[-3:-1]))
        return self.freqAlphabets(s[:-1]) + chr(ord('a') - 1 + int(s[-1]))
    