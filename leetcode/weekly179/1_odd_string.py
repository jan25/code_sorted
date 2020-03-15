'''
https://leetcode.com/contest/weekly-contest-179/problems/generate-a-string-with-characters-that-have-odd-counts/
'''
class Solution:
    def generateTheString(self, n: int) -> str:
        s = ['a'] * n
        if n % 2 == 0: s[-1] = 'b'
        return ''.join(s)
        
