class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_price = prices[0]
        res = 0 
        for p in prices :
            if p < min_price :
                min_price = p 
            res = max(res,p-min_price)
        return res 
        