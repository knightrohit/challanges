"""
Time/Space complexity = O(N)
"""

# Top down
from functools import lru_cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @lru_cache(None)
        def dfs(n):
            
            if n <= 1:
                return 0           
        
            return min(dfs(n-1) + cost[n-1], dfs(n-2) + cost[n-2])
                       
        return dfs(len(cost))


# Bottom up
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        min_cost = [0] * (len(cost) + 1)
        
        for i in range(2, len(cost) + 1):
            min_cost[i] = min(min_cost[i-1] + cost[i-1], min_cost[i-2] + cost[i-2])
            
        return min_cost[-1]
    