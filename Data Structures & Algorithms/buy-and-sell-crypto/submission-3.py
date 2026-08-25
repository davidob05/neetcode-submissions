class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        best_profit = 0

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                best_profit = max(best_profit, price - min_price)
        return best_profit