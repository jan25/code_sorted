'''
Python list.append() has auto doubling(maybe?) list on list full(sure?)
But this implementation doesnt take that into account
'''
class MinHeap:
	def __init__(self):
		self.heap = [0] * 10
		self.size = 0

	def checkSpace(self):
		if self.size < len(self.heap):
			return None
		newHeap = [0] * (self.size * 2)
		for i in range(self.size):
			newHeap[i] = self.heap[i]
		self.heap = newHeap

	def getMin(self):
		if self.size > 0:
			return self.heap[0]
		return None

	def removeMin(self):
		minVal = None
		if self.size > 0:
			minVal = self.heap[0]
			self.size -= 1
			self.heap[0] = self.heap[self.size]
			self.heapifyDown()
		return minVal

	def insert(self, newVal):
		self.checkSpace()
		self.heap[self.size] = newVal
		self.size += 1
		self.heapifyUp(self.size - 1)

	def heapifyUp(self, ptr):
		if ptr <= 0: return None
		par = (ptr - 1) // 2
		if self.heap[ptr] >= self.heap[par]:
			return None
		self.swap(ptr, par)
		self.heapifyUp(par)

	def heapifyDown(self, ptr = 0):
		if 2 * ptr + 1 >= self.size:
			return None
		minChild = 2 * ptr + 1
		if 2 * ptr + 2 < self.size and \
		self.heap[2 * ptr + 2] < self.heap[minChild]:
			minChild = 2 * ptr + 2
		if self.heap[minChild] < self.heap[ptr]:
			self.swap(minChild, ptr)
			self.heapifyDown(minChild)

	def swap(self, a, b):
		self.heap[a], self.heap[b] = \
		self.heap[b], self.heap[a]

''' running median solution '''
leftHalf = MinHeap() # neg vals
rightHalf = MinHeap() # pos vals
def balance():
	while rightHalf.size - leftHalf.size > 1:
		leftHalf.insert(-1 * rightHalf.removeMin())
	while leftHalf.size > 0 and rightHalf.getMin() < (-1 * leftHalf.getMin()):
		leftHalf.insert(-1 * rightHalf.removeMin())
		rightHalf.insert(-1 * leftHalf.removeMin())
def median():
	balance()
	if rightHalf.size > leftHalf.size:
		return rightHalf.getMin()
	sum = rightHalf.getMin() + (-1 * leftHalf.getMin())
	return sum / 2
for i in range(int(input())):
	x = int(input())
	rightHalf.insert(x)
	print (float(x) if i == 0 else float(median()))
