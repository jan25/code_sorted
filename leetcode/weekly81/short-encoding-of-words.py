class Solution:
    def minimumLengthEncoding(self, words: 'List[str]') -> 'int':
        
        trie = []
        def insert(s, si=0, next_i=0):
            if si == len(s): return
            if next_i == len(trie): trie.append({})
            if s[si] not in trie[next_i]:
                trie.append({})
                trie[next_i][s[si]] = len(trie) - 1
            insert(s, si + 1, trie[next_i][s[si]])
        
        leaves_depth = []
        def dfs(i=0, d=1):
            if 0 == len(trie[i].keys()):
                leaves_depth.append(d - 1); return
            for k in trie[i]:
                dfs(trie[i][k], d + 1)
    
        for w in words:
            insert(w[::-1])
        
        dfs()
        return len(leaves_depth) + sum(leaves_depth)