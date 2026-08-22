class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n=len(prices)
        result=[0]*n
        for i in range(0,n):
            result[i]=prices[i]
            for j in range(i+1,n):
                if prices[j]<=prices[i]:
                    result[i]=prices[i]-prices[j]
                    break
                
        return result
        