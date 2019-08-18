'''
https://leetcode.com/contest/weekly-contest-149/problems/swap-for-longest-repeated-character-substring/

Test cases:
"baaaa"
"aabaa"
"aaaaa"
"abbaa"
'''

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        counts, sub_strs = {}, {}
        i = 0
        while i < len(text):
            c = text[i]
            if c not in counts: counts[c] = 0
            if c not in sub_strs: sub_strs[c] = []
            for j in range(i, len(text) + 1):
                if j == len(text) or c != text[j]:
                    sub_strs[c].append((i, j - 1))
                    i = j - 1
                    break
                counts[c] += 1
            i += 1

        max_l = 1
        for c in sub_strs.keys():
            strs = sub_strs[c]
            l = strs[0][1] - strs[0][0] + 1
            if counts[c] > l: l += 1
            for i in range(1, len(strs)):
                ld = strs[i][1] - strs[i][0] + 1
                if counts[c] > ld: ld += 1
                l = max(l, ld)
                if strs[i - 1][1] + 2 == strs[i][0]:
                    ld = strs[i][1] - strs[i - 1][0]
                    if counts[c] > ld: ld += 1
                    l = max(l, ld)
            max_l = max(l, max_l)
        return max_l
