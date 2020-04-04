'''
https://leetcode.com/contest/weekly-contest-182/problems/find-all-good-strings/

Idea:
    Inclusion-Exclusion principle. i.e.
    numGoodStrings(s1, s2) = countGoodStrings(s2) - countGoodStrings(s1) + addOneIfGoodString(s1)

countGoodStrings(string) can be a Dynamic programming algorithm:
    State - (string_index=[0, n], prefix_is_equal_so_far, next_evil_index_to_match)
    
Within Dynamic programming we can do KMP string comparision to exclude evil substrings
'''
class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        MOD = 10**9 + 7
        en = ''.join(chr(c) for c in range(ord('a'), ord('z') + 1))
        
        # longest prefix suffix length array for evil string
        # lp[j] = i if evil[:i] == evil[-i:]
        lp, i = [0], 0
        for j in range(1, len(evil)):
            if evil[j] == evil[i]:
                i += 1
            else:
                while i - 1 >= 0 and evil[lp[i - 1]] != evil[j]:
                    i = lp[i - 1]
                if i > 0 and evil[i] == evil[j]:
                    i += 1
            lp.append(i)

        def isValid(s):
            i = 0
            for c in s:
                if c == evil[i]: i += 1
                else: i = lp[i]
                if i == len(evil):
                    return 0 # found evil substring
            return 1
        
        def adjust(ei, c):
            while ei > 0 and evil[ei] != c:
                ei = lp[ei - 1]
            if evil[ei] == c: return ei + 1
            return 0
        
        # (s_i, s_eq, evil_i) 500 x 2 x 50 x 26(inner-loop)
        memo = {}
        cs = []
        def count(s, si, seq, ei):
            if ei == len(evil):
                return 0
            if si >= n:
                return 1
            if (si, seq, ei) in memo:
                return memo[(si, seq, ei)]
            lcount = 0
            for c in en:
                if seq:
                    if c <= s[si]:
                        lei = adjust(ei, c)
                        cs.append(c)
                        lcount += count(s, si + 1, seq and c == s[si], lei)
                        cs.pop()
                else:
                    lei = adjust(ei, c)
                    cs.append(c)
                    lcount += count(s, si + 1, False, lei)
                    cs.pop()
            lcount %= MOD
            memo[(si, seq, ei)] = lcount
            return lcount
        
        good = count(s2, 0, True, 0); memo = {}
        good = (MOD + good - count(s1, 0, True, 0)) % MOD
        good = (good + isValid(s1)) % MOD
        return good
    
