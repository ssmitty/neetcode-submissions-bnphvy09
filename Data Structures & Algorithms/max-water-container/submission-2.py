class Solution:
    def maxArea(self, num: List[int]) -> int:
        l=0
        r=len(num)-1
        maximum=min(num[l],num[r])*(r-l)
        while l<=r:
            if min(num[l],num[r])*(r-l)>maximum:   
                maximum= min(num[l],num[r])*(r-l)
            if num[l]>num[r]:
                r-=1
            else:
                l+=1
                
        return maximum

