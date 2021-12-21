"""
Time Complexity = O(NlogN)
space Complexity = O(N)
"""

import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        self.n = 0
        

    def addNum(self, num: int) -> None:
        self.n += 1
        if not self.max_heap:
            heapq.heappush(self.max_heap, num*-1)
            
        # check the size
        elif len(self.max_heap) == len(self.min_heap):
            if num < self.min_heap[0]:
                heapq.heappush(self.max_heap, num*-1)
            else:
                val = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, val*-1)
                heapq.heappush(self.min_heap, num)
                
        elif len(self.max_heap) > len(self.min_heap):
            if num < self.max_heap[0]*-1:
                val = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, val*-1)
                heapq.heappush(self.max_heap, num*-1)
            else:
                heapq.heappush(self.min_heap, num)
        

    def findMedian(self) -> float:
        if not self.max_heap:
            return 0
        
        if self.n == 1:
            return self.max_heap[0]*-1
        
        if self.n % 2:
            return self.max_heap[0]*-1
        else:
            return (self.min_heap[0] + self.max_heap[0]*-1)/2
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()