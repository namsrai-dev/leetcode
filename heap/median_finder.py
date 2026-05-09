import heapq


class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if not self.maxheap and not self.minheap:
            heapq.heappush(self.maxheap, -num)

        elif self.maxheap[0] * -1 > num:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)


        if len(self.minheap) - len(self.maxheap) > 1:
            popped = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -popped)
            
        elif len(self.maxheap) - len(self.minheap) > 1:
            popped = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -popped)

        print(self.maxheap)
        print(self.minheap)


    def findMedian(self) -> float:
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        elif len(self.minheap) < len(self.maxheap):
            return -self.maxheap[0]
        return (-self.maxheap[0] + self.minheap[0]) / 2


sol = MedianFinder()
sol.addNum(7)
sol.addNum(3)
sol.addNum(5)
sol.addNum(4)
sol.addNum(6)
sol.addNum(2)
sol.addNum(1)
print(sol.findMedian())

sol2 = MedianFinder()
sol2.addNum(2)
sol2.addNum(3)
sol2.addNum(4)

print(sol2.findMedian())

sol3 = MedianFinder()
sol3.addNum(2)
sol3.addNum(3)

print(sol3.findMedian())