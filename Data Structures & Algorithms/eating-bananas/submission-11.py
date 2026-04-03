class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ma=max(piles) 
        if h== len(piles):
            return ma
        l=1
        r=ma
        while l<r:
            num=0
            mid=(r+l)//2
            for j in range(len(piles)):
                num+= math.ceil(piles[j]/mid)
            if num>h:
                l=mid+1
            else:
                r=mid
        return l  

    #trying to eat all bananas from a pile
    #Eat whatever your banna eating rate is
    #If you eat before the hour is up till have to wait
    # if h= length of array k = max of the array
    # if h< length of the array cant return
    #if h>len of array 