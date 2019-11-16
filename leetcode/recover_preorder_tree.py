'''
https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        def toi(s, i):
            if s.find('-', i) == -1: return int(s[i:])
            return int(s[i:s.find('-', i)])
        
        def parse(s, i=0, l=[]):
            if i == -1: return l
            for j in range(i, len(s)):
                if s[j] != '-':
                    l.append(((j - i), toi(s, j)))
                    return parse(s, s.find('-', j), l)
        t = parse(S)

        r = (0, TreeNode(t[0][1]))
        stk = [r]
        for e in t[1:]:
            while stk[-1][0] != e[0] - 1:
                stk.pop()
            p = stk[-1][1]
            n = TreeNode(e[1])
            if p.left is None: p.left = n
            else: p.right = n
            stk.append((e[0], n))

        return r[1]            

