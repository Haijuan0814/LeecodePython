import heapq
class MedianFinder:

    # Heap Solution
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

        #heapq.heapify(self.minHeap)
        #heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:

        heapq.heappush(self.minHeap , num)
        heapq.heappush(self.maxHeap , -heapq.heappop(self.minHeap))

        if len(self.minHeap) < len(self.maxHeap):
            heapq.heappush(self.minHeap ,-heapq.heappop(self.maxHeap))
 
    def findMedian(self) -> float:
        if len(self.minHeap) ==  len(self.maxHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        else:
            print('odd：')
            return self.minHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


"""
    # List Solution
    
    def __init__(self):
        self.l = []


    def addNum(self, num: int) -> None:
        self.l.append(num)

    def findMedian(self) -> float:
        if len(self.l) == 0:
            return 0

        self.l.sort()
        length = len(self.l)
        if length % 2 == 0:
            n1 = length // 2 -1
            n2 = n1 + 1
            mid = (self.l[n1] + self.l[n2]) / 2
        else:
            n1 = length // 2
            mid = self.l[n1]

        return mid
        
 """