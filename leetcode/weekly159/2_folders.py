'''
https://leetcode.com/contest/weekly-contest-159/problems/remove-sub-folders-from-the-filesystem/
'''
class Node:
    def __init__(self, c=None):
        self.c = c
        self.f = False
        self.nexti = {}
        
    def add_next(self, s, i):
        if s not in self.nexti:
            self.nexti[s] = i
            
    def get_next(self, s):
        if s not in self.nexti:
            return None
        return self.nexti[s]
    
class Solution:
    def add(self, s, i=0):
        if len(s) == 0:
            self.trie[i].f = True
            return
        c = s[0]
        tn = self.trie[i]
        if tn.get_next(c) is None:
            n = Node(c)
            self.trie.append(n)
            tn.add_next(c, len(self.trie) - 1)
        self.add(s[1:], tn.get_next(c))
    
    def dfs(self, root, d=[]):
        if root.f:
            self.dirs.append('/' + '/'.join(d))
            return
        for i in root.nexti.values():
            tn = self.trie[i]
            d.append(tn.c)
            self.dfs(tn, d)
            d.pop()

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        self.trie = [Node()]
        
        for s in folder:
            self.add(s.split('/')[1:])
            
        self.dirs = []
        self.dfs(self.trie[0])
        return self.dirs
    