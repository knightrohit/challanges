"""
Time Complexity = O(NlogN)
Space Complexity = O(N)
"""

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if not stones:
            return 0
        
        max_heap = [i*-1 for i in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            first, second = heapq.heappop(max_heap), heapq.heappop(max_heap)
            
            if first == second:
                continue
            else:
                heapq.heappush(max_heap, (first*-1 - second*-1)*-1)
                
        return max_heap[0]*-1 if max_heap else 0