"""
Time Complexity = O(N)
Space Complexity = O(1)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = float('inf')
        max_profit = float('-inf')
        
        for price in prices:
            if price < min_price:
                min_price = price
            
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max(max_profit, 0)