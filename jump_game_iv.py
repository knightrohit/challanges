"""
Time/Space complexity: O(N)
"""

from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        if not arr or len(arr) == 1:
            return 0
        
        if len(arr) == 2:
            return 1
        
        no_freq = defaultdict(list)
        
        for indx, val in enumerate(arr):
            no_freq[val].append(indx)
            
        
        visited = set()
        queue = deque([(0, 0)])
        min_step = 0
        
        while queue:
            indx, step = queue.popleft()
            
            if indx == len(arr) - 1:
                min_step = step if not min_step else min(min_step, step)
                continue                
            
            for i in no_freq[arr[indx]]:
                if i not in visited:
                    queue.append((i, step + 1))
                    visited.add(i)
                    
            # clear list to prevent redundant search
            no_freq[arr[indx]] = []
            
                
            for i in indx + 1, indx - 1:
                if i not in visited:
                    if 0 <= i <= len(arr) - 1:
                        queue.append((i, step + 1))
                        visited.add(i)                    
        return min_step