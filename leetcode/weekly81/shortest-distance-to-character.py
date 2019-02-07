class Solution:
    def shortestToChar(self, S: 'str', C: 'str') -> 'List[int]':
        cids = [i for i in range(len(S)) if S[i] == C]
        dist = [0] * len(S)
        for i in range(len(cids) - 1):
            a, b, c = cids[i], cids[i + 1], 0
            while a + c <= b - c:
                dist[a + c], dist[b - c] = c, c
                c += 1
        for i in range(cids[0]):
            dist[i] = cids[0] - i
        for i in range(cids[-1], len(S)):
            dist[i] = i - cids[-1]
        return dist
        