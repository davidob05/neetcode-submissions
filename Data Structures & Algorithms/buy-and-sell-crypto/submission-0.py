class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, i, best_sell, best_buy = 0, 0, 0, 0, 0
        while i < len(prices):

            if i == 0:
                i+=1
                continue

            if prices[i] > prices[sell]:
                sell = i
            
            elif prices[i] < prices[buy]:
                buy = i
                if sell<buy:
                    sell = buy
            
            if prices[best_sell] - prices[best_buy] < prices[sell] - prices[buy]:
                best_buy, best_sell = buy,sell
            i+=1
        return prices[best_sell] - prices[best_buy]


        return prices[buy] - prices[sell]