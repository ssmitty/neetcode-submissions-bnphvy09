class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sety={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in sety:
                return [sety[complement],i]
            sety[nums[i]]=i
        return {}