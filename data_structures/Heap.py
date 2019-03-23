from random import randint

class Heap:
    def __init__(self):
        self.heap = []
        self.size = 0
        self.inf = 10**9
    
    def count(self):
        return self.size

    def add(self, e):
        self.heap.append(e)
        self.size += 1
        self.heapify()

    def peek(self):
        if self.size > 0:
            return self.heap[0]
    
    def pop(self):
        if self.size == 0: return
        head_e = self.heap[0]
        self.heap[0] = self.heap[self._tail_index()]
        self.size -= 1
        self.heapify(True)
        return head_e

    def heapify(self, from_top=False):
        if from_top: self._heapify_down(0)
        else: self._heapify_up(self._tail_index())

    def _heapify_up(self, i):
        par = (i - 1) // 2
        if par < 0 or self.heap[par] <= self.heap[i]:
            return
        self._swap(par, i)
        self._heapify_up(par)

    def _heapify_down(self, i):
        if i >= self._tail_index(): return
        li, ri = 2 * i + 1, 2 * i + 2
        tail = self._tail_index()
        l_val = self.heap[li] if li <= tail else self.inf
        r_val = self.heap[ri] if ri <= tail else self.inf
        if l_val <= r_val and self.heap[i] > l_val:
            self._swap(i, li)
            self._heapify_down(li)
        elif r_val < l_val and self.heap[i] > r_val:
            self._swap(i, ri)
            self._heapify_down(ri)

    def _tail_index(self):
        return self.size - 1

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

def main():
    h = Heap()
    rand_ints = [randint(0, 1000000) for _ in range(100000)]
    for a in rand_ints: h.add(a)
    sorted_ints = []
    while h.count() > 0: sorted_ints.append(h.pop())
    assert(sorted(rand_ints) == sorted_ints)
    print ('Test passed :)')

if __name__ == '__main__':
    main()