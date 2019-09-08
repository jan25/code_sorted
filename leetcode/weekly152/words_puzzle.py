'''
https://leetcode.com/contest/weekly-contest-152/problems/number-of-valid-words-for-each-puzzle/
'''

def to_int(s, mask=0):
    if mask == 0: mask = (1 << 30) - 1
    i = 0
    for idx, c in enumerate(s):
        if mask & (1 << idx) == 0:
            continue
        b = ord(c) - 97
        i |= (1 << b)
    return i

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        buckets = {} # c -> { i -> count }

        for w in words:
            i = to_int(w)
            for c in set(w):
                sc = ord(c) - 97
                if sc not in buckets:
                    buckets[sc] = {}
                if i not in buckets[sc]:
                    buckets[sc][i] = 0
                buckets[sc][i] += 1

        answer = []
        for p in puzzles:
            pc = ord(p[0]) - 97
            if pc not in buckets:
                answer.append(0)
                continue
            bucket = buckets[pc]
            s = sorted(list(set(p)))
            n = len(s)
            a = 0
            for mask in range(1, (1 << n)):
                pi = to_int(s, mask)
                if pi in bucket: a += bucket[pi]
            answer.append(a)
        return answer
