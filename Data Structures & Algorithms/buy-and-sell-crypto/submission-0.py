class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # delta
        # single day to buy and sell
        # naive is iterate, calculate delta as you go...
        # If I'm at i, I look behind, could I buy cheaper? 
        # Then look ahead
        cheapest = prices[0]
        profit = 0
        for price in prices[1:]:
            if price < cheapest:
                cheapest=price
            elif profit < price-cheapest:
                profit = price-cheapest
        return profit
