import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_number = sys.maxsize
        for i in range(len(prices)):
            if prices[i] < min_number:
                min_number = prices[i]
            
            current_profit = prices[i] - min_number
            max_profit = max(max_profit,current_profit)
        return max_profit