'''
https://leetcode.com/contest/weekly-contest-148/problems/binary-tree-coloring-game/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def findX(r, x):
    if r == None: return None
    if r.val == x: return r
    return findX(r.left, x) or findX(r.right, x)

def getSize(r):
    if r == None: return 0
    return 1 + getSize(r.left) + getSize(r.right)

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        x_node = findX(root, x)
        x_sz = getSize(x_node)
        l_sz, r_sz = getSize(x_node.left), getSize(x_node.right)
        max_y_sz = max(l_sz, r_sz, n - x_sz)
        return max_y_sz >= (n + 1) // 2