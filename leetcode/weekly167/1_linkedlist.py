'''
https://leetcode.com/contest/weekly-contest-167/problems/convert-binary-number-in-a-linked-list-to-integer/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        v = 0
        while head:
            v = (v << 1) | head.val
            head = head.next
        return v
    