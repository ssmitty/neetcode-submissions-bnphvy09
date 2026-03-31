class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sety={}
        for x in range(len(nums)):
            if nums[x] in sety:
                return True
            sety[nums[x]]=x
        return False