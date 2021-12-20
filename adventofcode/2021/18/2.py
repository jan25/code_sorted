import fileinput
from typing import Union
from dataclasses import dataclass
from copy import deepcopy


@dataclass
class Pair:
    left: Union['Pair', int] = None
    right: Union['Pair', int] = None
    parent: 'Pair' = None

    def __str__(self) -> str:
        l = 'node' if type(self.left) is Pair else str(self.left)
        r = 'node' if type(self.right) is Pair else str(self.right)
        return f'[{l},{r}]'

    def addchild(self, c: Union['Pair', int]):
        if type(c) is Pair:
            c.parent = self

        if self.left is None:
            self.left = c
        elif self.right is None:
            self.right = c
        else:
            assert False

    def _inorder(self):
        l = self.left._inorder() if type(self.left) is Pair else []
        r = self.right._inorder() if type(self.right) is Pair else []
        return l + [self] + r

    def _explode(self):
        print('exploding', self)

        root = self
        while root.parent:
            root = root.parent
        o = root._inorder()

        # print(o)

        lval, rval = self.left, self.right
        node = None
        for p in o:
            if p is self:
                break
            if type(p.right) is int or type(p.left) is int:
                node = p
        if node:
            if type(node.right) is int:
                node.right += lval
            elif type(node.left) is int:
                node.left += lval

        print('left', node)

        node = None
        while o:
            p = o.pop()
            if p is self:
                break
            if type(p.right) is int or type(p.left) is int:
                node = p

        print('right', node)

        if node:
            if type(node.left) is int:
                node.left += rval
            elif type(node.right) is int:
                node.right += rval

        # print(self.tos())

        if self.parent and self.parent.left is self:
            self.parent.left = 0
        elif self.parent and self.parent.right is self:
            self.parent.right = 0

    def _split(self, val):
        return Pair(val // 2, (val + 1) // 2)

    def _reduce(self, dep=0):
        # explode
        if dep == 4:
            self._explode()
            return True

        if type(self.left) is Pair:
            if self.left._reduce(dep + 1):
                return True
        if type(self.right) is Pair:
            if self.right._reduce(dep + 1):
                return True

        # split
        if type(self.left) is int and self.left >= 10:
            self.left = self._split(self.left)
            self.left.parent = self
            return True

        if type(self.right) is int and self.right >= 10:
            self.right = self._split(self.right)
            self.right.parent = self
            return True

        return False

    def _rec_explode(self, dep=0):
        if dep == 4:
            self._explode()
            return True

        if type(self.left) is Pair:
            if self.left._rec_explode(dep + 1):
                return True
        if type(self.right) is Pair:
            if self.right._rec_explode(dep + 1):
                return True

        return False

    def _rec_split(self):
        if type(self.left) is int and self.left >= 10:
            self.left = self._split(self.left)
            self.left.parent = self
            return True
        elif type(self.left) is Pair:
            if self.left._rec_split():
                return True

        if type(self.right) is int and self.right >= 10:
            self.right = self._split(self.right)
            self.right.parent = self
            return True
        elif type(self.right) is Pair:
            if self.right._rec_split():
                return True

        return False

    def reduce(self):
        print('-----------------')
        print('reducing', self.tos())
        while True:
            print(self.tos())
            if self._rec_explode():
                continue
            elif self._rec_split():
                continue
            else:
                break
        return self

    def mag(self):
        if type(self.left) is Pair:
            self.left = self.left.mag()
        if type(self.right) is Pair:
            self.right = self.right.mag()
        return self.left * 3 + self.right * 2

    def tos(self):
        if type(self.left) is int:
            l = str(self.left)
        else:
            l = self.left.tos()

        if type(self.right) is int:
            r = str(self.right)
        else:
            r = self.right.tos()

        return f'[{l},{r}]'


def toi(c: str):
    if c.isdigit():
        return int(c)
    return c


def parse(l):
    tokens = [toi(c) for c in l if c != ',']
    root, stack = None, []
    for t in tokens:
        if t == '[':
            p = Pair()
            if stack:
                stack[-1].addchild(p)
            stack.append(p)
            continue
        if t == ']':
            root = stack.pop()
            continue

        assert len(stack) > 0
        stack[-1].addchild(t)
    # print(root.tos())
    return root


lines = [parse(l.strip()) for l in fileinput.input()]


def reducer(a, b):
    a, b = deepcopy(a), deepcopy(b)
    root = Pair(a, b)
    a.parent = b.parent = root
    p = root.reduce()
    print(p.tos())
    return p


print(max(reducer(a, b).mag() for a in lines for b in lines if a is not b))
