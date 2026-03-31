class Solution:
    def maxArea(self, num: List[int]) -> int:
      n=len(num)
      m=min(num[0],num[n-1])*(n-1)
      l=0
      r=n-1
      while(l<r):
        if min(num[l],num[r])*(r-l)>m:
          m=min(num[l],num[r])*(r-l)
          if num[l]<num[r]:
            l+=1
          else:
            r-=1
        else:
          if num[l]<num[r]:
            l+=1
          else:
            r-=1
      return m
        
