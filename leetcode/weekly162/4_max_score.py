'''
https://leetcode.com/contest/weekly-contest-162/problems/maximum-score-words-formed-by-letters/
'''
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def toi(c): return ord(c) - 97
        
        n = len(words)
        l = [0] * 26
        for c in letters: l[toi(c)] += 1
        
        maxg = 0
        for m in range(1, 1 << n):
            ls = [0] * 26
            for i in range(n):
                if m & (1 << i):
                    for c in words[i]:
                        ls[toi(c)] += 1
            
            maxs = 0
            for i in range(26):
                if ls[i] > l[i]:
                    maxs = 0; break
                maxs += ls[i] * score[i]
            maxg = max(maxg, maxs)
            
        return maxg
                