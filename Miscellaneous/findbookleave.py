
class Solution:
    def __init__(self, N):
        self.n = N

        # Auxilary DS to store left/right occupied room for a given occupied room
        # Useful in updating heap when book() or leave() is called
        self.left_occupied = {}
        self.right_occupied = {}

        # root element stores longest free range of rooms
        # maybe we need custom key to order heap elements
        # element is of form { left_occupied: a, right_occupied: b }
        self._heap = []
    
    def find_place(self):
        '''
        O(1) look up from top of heap
        '''
        optimal_slot = self._heap.top()
        l, r = optimal_slot.left_occupied, optimal_slot.right_occupied
        if abs(r - l) < 1: return -1
        return (r + l + 1) // 2
    
    def book(self, a):
        '''
        O(logN) for heap push (heapify OP)
        Assuming a is most optimal available room
        pick most optimal room from top of heap and update heap
        '''
        optimal_slot = self._heap.pop()
        l, r = optimal_slot.left_occupied, optimal_slot.right_occupied
        self.left_occupied[a] = l
        self.right_occupied[a] = r

        self.left_occupied[r] = self.right_occupied[l] = a
        self._heap.push({
            'left_occupied': l,
            'right_occupied': a,
        })
        self._heap.push({
            'left_occupied': a,
            'right_occupied': r,
        })
        # TODO
        # Need to remove [l, r] range from heap
    
    def leave(self, a):
        '''
        O(logN) for heap push (heapify OP)
        return nil if a is not occupied currently
        '''
        if a not in self.left_occupied: return
        l, r = self.left_occupied[a], self.right_occupied[a]
        self._heap.push({
            'left_occupied': l,
            'right_occupied': r,
        })
        # TODO
        # Needs to remove [l, a] and [a, r] ranges from heap
        