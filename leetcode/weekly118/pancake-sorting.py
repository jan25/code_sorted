class Solution:
    def pancakeSort(self, A):
        A.reverse()
        sortedA = sorted(A)
        sortedA.reverse()
        flips = []
        for i in range(len(A) - 1):
            if A[i] != sortedA[i]:
                for j in range(i + 1, len(A) - 1):
                    if A[j] == sortedA[i]:
                        self.flip(A, j)
                        flips.append(len(A) - j)
                self.flip(A, i)
                flips.append(len(A) - i)
        return flips
    
    def flip(self, l, k):
        subArray = l[k:]
        subArray.reverse()
        for i, n in enumerate(subArray):
            l[k + i] = n
