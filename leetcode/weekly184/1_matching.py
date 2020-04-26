'''
https://leetcode.com/contest/weekly-contest-184/problems/string-matching-in-an-array/
'''
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        m = []
        for w in words:
            for match in words:
                if w != match and w in match:
                    m.append(w)
                    break
        return m
    
