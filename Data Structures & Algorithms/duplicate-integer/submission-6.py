class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        se={}
        for i in range(len(nums)):
            if nums[i] not in se:
                se[nums[i]]=i
            else:
                return True
        return False