class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []


    def addNum(self, num: int) -> None:
        heappush(self.max_heap,-1 * num)
        if self.max_heap and self.min_heap and (-1 * self.max_heap[0]) > self.min_heap[0]:
            val = -1 * heappop(self.max_heap)
            heappush(self.min_heap,val)
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -1 * heappop(self.max_heap)
            heappush(self.min_heap, val)
        if len(self.min_heap) > len(self.max_heap) + 1:
            val = -1 * heappop(self.min_heap)
            heappush(self.max_heap, val)

        

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):return (self.min_heap[0] + (-1 * self.max_heap[0]))/2
        if len(self.min_heap) > len(self.max_heap):return self.min_heap[0]

        return -1 * self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()