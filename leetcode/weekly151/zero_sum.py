'''
https://leetcode.com/contest/weekly-contest-151/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# For debugging
def p(l):
    r = []
    while l:
        r.append(l.val)
        l = l.next
    return r

# For debugging
def pd(d):
    return ['%d:%d'%(k,d[k].val) for k in d if d[k]]

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        formers = {} # sum -> first ListNode seen with cumulative sum
        h, s = head, 0
        while head:
            s += head.val
            if s == 0:
                h = head.next
                formers = {}
            elif s in formers and formers[s]:
                if h: # valid head
                    t = formers[s].next
                    formers[s].next = head.next
                    ss = s
                    while t and t != head:
                        ss += t.val
                        formers[ss] = None
                        t = t.next
                else:
                    h = head.next
                    formers = {}
            else: formers[s] = head
            head = head.next
        return h
