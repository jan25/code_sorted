'''
https://leetcode.com/contest/weekly-contest-161/problems/minimum-remove-to-make-valid-parentheses/
'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        stk = []
        for i, c in enumerate(s):
            if c not in '()': continue
            if len(stk) > 0 and s[stk[-1]] == '(' and c == ')': stk.pop()
            else: stk.append(i)
        
        stk = set(stk)
        return ''.join(s[i] for i in range(n) if i not in stk)
