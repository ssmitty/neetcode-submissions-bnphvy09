class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)-1
        i=0
        while i<n:
            if numbers[i]+numbers[n]==target:
                return [i+1,n+1]
            if numbers[n]+numbers[i]>target:
                n-=1
                continue
            else:
                i+=1
                continue
        return[]
