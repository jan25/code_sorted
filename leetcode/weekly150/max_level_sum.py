'''
https://leetcode.com/contest/weekly-contest-150/problems/maximum-level-sum-of-a-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        q, qi = [root], 0
        pop = 1
        max_sum, s = 0, 0
        l, curr_l = 1, 1
        while len(q) - qi > 0:
            if pop == 0:
                pop = len(q) - qi
                if max_sum < s:
                    l = curr_l
                    max_sum = s
                s = 0
                curr_l += 1
            else:
                pop -= 1
                f = q[qi]
                s += f.val
                if f and f.left: q.append(f.left)
                if f and f.right: q.append(f.right)
                qi += 1
        return l
        