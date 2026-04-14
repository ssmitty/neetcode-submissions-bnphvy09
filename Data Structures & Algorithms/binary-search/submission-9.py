class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        upper=len(nums)-1
        c=0
        while i<=upper and c<len(nums):
            mid=upper+i//2
            if nums[mid]<target:
                i=mid+1
                c+=1
            elif nums[mid]>target:
                upper=mid-1
                c+=1
            else:
                return mid
            
        return -1
        