class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        min_price=prices[0]
        profit=0
        for i in range(0,n-1):
            if prices[i]<prices[i+1]:
                profit=profit+(prices[i+1]-prices[i])
        return profit



        