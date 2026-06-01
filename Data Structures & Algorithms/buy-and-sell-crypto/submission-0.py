class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_value = 0
        for i in range(len(prices)) :
            for j in range (i) :
                if prices[i] - prices[j] > 0 : 
                    max_value = max(max_value,prices[i] - prices[j] )
        return max_value