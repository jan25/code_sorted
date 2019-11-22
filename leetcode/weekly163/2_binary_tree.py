'''
https://leetcode.com/contest/weekly-contest-163/problems/find-elements-in-a-contaminated-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        self.finder = set()
        self._recover(root, 0)
        
    def _recover(self, r, v):
        if r is None: return
        r.val = v
        self.finder.add(v) # this is cheating
        self._recover(r.left, 2 * v + 1)
        self._recover(r.right, 2 * v + 2)        

    def find(self, target: int) -> bool:
        return target in self.finder


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)