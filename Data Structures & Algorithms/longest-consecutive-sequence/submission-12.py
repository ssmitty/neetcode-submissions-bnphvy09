class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numt={}
        if len(nums)==0:
            return 0
        for i in range(len(nums)):
            if nums[i] in numt:
                numt[nums[i]]+=1
            else:
                numt[nums[i]]=1
        mini=min(nums)
        k=0
        count=0
        maxcount=1
        while k< len(nums):
            while mini in numt:
                mini+=1
                count+=1
            maxcount=max(maxcount,count)
            count=0
            k+=1
            print(maxcount,mini)
            if k<len(nums):
                mini=nums[k]
        return maxcount
            
            
        