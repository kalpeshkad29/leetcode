class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        min_price=prices[0]
        max_profit=0
        for i in range(0,n):
            profit=prices[i]-min_price
            max_profit=max(max_profit,profit)
            min_price=min(min_price,prices[i])
        return max_profit
        
            

       
            

           
        