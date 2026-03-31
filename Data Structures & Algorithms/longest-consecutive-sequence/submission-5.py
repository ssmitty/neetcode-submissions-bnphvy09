class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        has={}
        longest=0
        i=0
        while i< len(nums):
            has[nums[i]]=i
            i+=1
        j=0
        while j <len(nums):
            if nums[j]-1 not in has:
                length=0
                while(nums[j]+length in has):
                    length+=1
                longest=max(length,longest)
            j+=1

        return longest
               
        