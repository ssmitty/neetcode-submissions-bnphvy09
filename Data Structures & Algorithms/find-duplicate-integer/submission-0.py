class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sety=set()
        for i in range(len(nums)):
            if nums[i] in sety:
                return nums[i]
            sety.add(nums[i])
        return -1
        