class Solution:
    def findMin(self, nums: List[int]) -> int:
        r=len(nums)-1
        l=0
        while l<=r:
            m=(l+r)//2
            print(nums[m],nums[r],nums[l])
            if nums[m]>nums[r]:
                l=m+1
            elif nums[m]<nums[r]:
                r=m
            else:
                return nums[l]
