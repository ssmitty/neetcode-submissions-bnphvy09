class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[0]*len(nums)
        postfix=[0]*len(nums)
        pre=0
        for i in range(len(nums)):
            prefix[i]=pre
            if i==0:
                pre=nums[i]
            else:
                pre*=nums[i]
        post=0
        for i in range(len(nums)-1,-1,-1):
            postfix[i]=post
            if i==len(nums)-1:
                post=nums[i]
            else:
                post*=nums[i]
        res=[0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                res[i]=postfix[i]
            elif i==len(nums)-1:
                res[i]=prefix[i]
            else:
                res[i]=postfix[i]*prefix[i]
        return res

