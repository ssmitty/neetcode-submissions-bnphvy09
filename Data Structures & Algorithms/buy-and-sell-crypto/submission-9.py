class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=len(prices)-1
        maxprofit=0
        while l<r:
            while l<r:
                maxprofit=max(maxprofit,prices[r]-prices[l])
                l+=1
            l=0
            r-=1
                



        return maxprofit
                
                