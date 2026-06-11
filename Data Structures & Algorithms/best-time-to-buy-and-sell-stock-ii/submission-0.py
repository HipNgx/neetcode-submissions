class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        sell = 1
        while sell < len(prices):
            if prices[sell] > prices[sell-1] :
                if sell == len(prices) - 1 :
                    profit += (prices[sell]-prices[buy])
                    break
                sell += 1
            else :
                n = prices[sell-1]-prices[buy]
                profit += n
                buy = sell
                sell += 1
        return profit