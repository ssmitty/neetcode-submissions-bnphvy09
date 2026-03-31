class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[0]*len(nums)
        postfix=[0]*(len(nums)+1)
        for i in range(len(nums)):
            if i==0:
                prefix[i]=nums[i]
            else:
                prefix[i]=nums[i]*prefix[i-1]
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                postfix[i]=nums[i]
            else:
                postfix[i]=nums[i]*postfix[i+1]
        postfix[len(nums)]=1
        ind=0
        while ind<len(nums):
            if ind==0:
                nums[ind]=postfix[ind+1]
            else:
                nums[ind]=prefix[ind-1]*postfix[ind+1]
            ind+=1
        return nums
        
        print(nums)
        print(prefix)
        print(postfix)
