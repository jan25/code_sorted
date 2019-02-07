class Solution:
    def numFactoredBinaryTrees(self, A: 'List[int]') -> 'int':
        ids = {x : i for i, x in enumerate(A)}
        g = {x : [] for x in A}
        A.sort()
        for i in range(len(A)):
            for j in range(len(A)):
                if A[j] % A[i] == 0 and (A[j] // A[i]) in ids:
                    g[A[j]].append((A[i], A[j] // A[i]))
        mod = (10 ** 9) + 7
        
        memo = {}
        def dp(x):
            if len(g[x]) == 0: return 1
            if x in memo: return memo[x]
            memo[x] = 1
            for childs in g[x]:
                memo[x] += dp(childs[0]) * dp(childs[1])
                if memo[x] >= mod: memo[x] %= mod
            return memo[x]
        
        total = 0
        for a in A:
            total += dp(a)
            if total >= mod: total %= mod
        return total