class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def kworks(k):
            hour=0
            for pile in piles:
                flt=float(pile)/k
                flt2=float(pile)//k
                if flt!=flt2:
                    hour+=flt2+1
                else:
                    hour+=flt2
                if hour>h:
                    return False
            return True


        l=1
        r=max(piles)
        mini=max(piles)
        while l<=r:
            k=(l+r)//2
            if kworks(k):
                mini=min(mini,k)
                r=k-1
            else:
                l=k+1
        return mini
            

        