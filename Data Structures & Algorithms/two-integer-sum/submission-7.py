class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        se={}
        for i in range(len(nums)):
            if nums[i] not in se:
                se[nums[i]]=i
            if target-nums[i] in se and se[target-nums[i]]!= i:
                print(se[target-nums[i]])
                print(i)
                return [se[target-nums[i]],i]
            
        