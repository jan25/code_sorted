'''
https://leetcode.com/problems/design-skiplist/

Implementation based on:
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-introduction-to-algorithms-sma-5503-fall-2005/video-lectures/lecture-12-skip-lists/lec12.pdf
'''
import math
import random
from typing import List

class Node:
    def __init__(self, val):
        self.val = val
        self.up = None
        self.prev = None
        self.down = None
        self.next = None

class Skiplist:
    def __init__(self):
        a, b = Node(-math.inf), Node(math.inf) # left, right most infinite columns
        a.next = b
        b.prev = a
        self.l = a # top-left node
        # self._pretty_print('__init__')

    def search(self, target: int) -> bool:
        return self._search(target) is not None

    def _search(self, target: int) -> Node:
        node = self.l
        while node is not None:
            if node.val == target: return node
            next_node = node.next
            if next_node.val > target:
                node = node.down
            else:
                node = next_node
        return None

    def add(self, num: int) -> None:
        node = self.l
        down_nodes = []
        while node is not None:
            next_node = node.next
            if next_node.val >= num:
                down_nodes.append(node)
                node = node.down
            else:
                node = next_node
        
        new_node = Node(num)
        prev_node = down_nodes.pop()
        new_node.next = prev_node.next
        new_node.next.prev = new_node
        new_node.prev = prev_node
        prev_node.next = new_node

        self._do_promote(new_node, down_nodes)

        # self._pretty_print('after %d add' % num)
    
    def _do_promote(self, node: Node, down_nodes: List[Node]) -> None:
        while self._must_promote():
            prev_node = None
            if len(down_nodes) > 0:
                prev_node = down_nodes.pop()
            else:
                new_minf_node = Node(-math.inf)
                new_inf_node = Node(math.inf)
                new_inf_node.prev = new_minf_node
                new_minf_node.next = new_inf_node
                new_minf_node.down = self.l # Note: we are not setting new_inf_node.down, not idea how to set quickly
                self.l.up = new_minf_node
                self.l = new_minf_node

                prev_node = new_minf_node
            
            new_node = Node(node.val)
            new_node.next = prev_node.next
            new_node.next.prev = new_node
            prev_node.next = new_node
            new_node.prev = prev_node

            new_node.down = node
            node.up = new_node
            node = node.up

    # coin flip to decide whether to promote a node to a upper level
    def _must_promote(self) -> bool:
        return random.randint(0, 1) == 1

    def erase(self, num: int) -> bool:
        node = self._search(num)
        if node is None: return False
        while node.down is not None:
            node = node.down
        while node is not None:
            node.prev.next = node.next
            node.next.prev = node.prev
            node = node.up
        # self._pretty_print('after %d erase' % num)
        return True

    # prints columns of list top-down
    def _pretty_print(self, msg=''):
        print(msg)
        cols = [[]]
        node = self.l
        while True:
            cols[-1].append(node.val)
            if node.down is None: break
            node = node.down
        cols[0] = cols[0][::-1]
        
        node = node.next
        while node is not None:
            col = []
            up_node = node
            while up_node is not None:
                col.append(up_node.val)
                up_node = up_node.up
            while len(col) < len(cols[0]):
                col.append(' ')
            cols.append(col)
            node = node.next
        for col in cols:
            print(col)
