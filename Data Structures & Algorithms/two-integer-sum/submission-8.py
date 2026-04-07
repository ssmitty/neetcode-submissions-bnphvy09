class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sety={}
        for i in range(len(nums)):
            if target-nums[i] in sety and i!=sety[target-nums[i]]:
                return [sety[target-nums[i]],i]
            if nums[i] not in sety:
                sety[nums[i]]=i
            

