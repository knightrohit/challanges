"""
Time Complexity - O(ElogV)
Space Complexity - O(V + E)
"""

import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        min_heap = []
        visited = {}
        adj_dict = defaultdict(list)
        heapq.heappush(min_heap, (0, k))
        
        for s, t, w in times:
            adj_dict[s].append((t, w))
            
        while min_heap:
            dist, node = heapq.heappop(min_heap)
            if node in visited:
                continue
                
            visited[node] = dist
            
            for t, w in adj_dict[node]:
                heapq.heappush(min_heap, (dist + w, t))
                
        return max(visited.values()) if len(visited) == n else -1