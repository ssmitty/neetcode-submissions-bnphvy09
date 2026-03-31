class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        if len(prices)<=1:
            return profit
        l= 0
        r=1
        while r<len(prices)-1:
            print(prices[r],prices[l])
            if prices[r]>prices[l]:
                if prices[r]-prices[l]>profit:
                    profit=prices[r]-prices[l]
                r+=1
                continue
            if prices[r]<=prices[l]:
                l=r
                r=r+1
                continue
        if prices[-1]-prices[l]>profit:
            profit=prices[-1]-prices[l]
        return profit