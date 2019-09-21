'''
https://leetcode.com/contest/weekly-contest-154/problems/reverse-substrings-between-each-pair-of-parentheses/
'''
class Solution:
    def balance(self, s):
        self.b = {}
        st = []
        for i, c in enumerate(s):
            if c == '(': st.append(i)
            elif c == ')': self.b[st.pop()] = i

    def flip(self, s, l, r, really=True):
        i = l
        while i <= r:
            if s[i] == '(':
                bi = self.b[i]
                self.flip(s, i + 1, bi - 1)
                i = bi
            i += 1
        if really:
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1; r -= 1

    def reverseParentheses(self, s: str) -> str:
        s = list(s)
        self.balance(s)
        really_flip = s[0] in '()' and self.b[0] == len(s) - 1
        l, r = 0, len(s) - 1
        if really_flip: l += 1; r -= 1
        self.flip(s, l, r, really=really_flip)
        return ''.join([c for c in s if c not in '()'])
