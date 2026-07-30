class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sety={}
        for i in range(len(nums)):
            if target-nums[i] in sety:
                return [sety[target-nums[i]],i]
            sety[nums[i]]=i