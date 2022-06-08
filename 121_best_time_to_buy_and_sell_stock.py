# 121. Best Time to Buy and Sell Stock


# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0. 


class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        
        max = prices[len(prices)-1]
        profit = 0
        
        for item in prices[::-1]:
            if max - item > profit:
                profit = max - item
            if item > max:
                max = item
        
        return profit