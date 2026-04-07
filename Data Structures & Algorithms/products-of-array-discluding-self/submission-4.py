class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixarr=[0]*len(nums)
        postfix=[0]*len(nums)
        postfix[-1]=nums[-1]
        prefixarr[0]=nums[0]
        for i in range(1,len(nums)):
            prefixarr[i]= prefixarr[i-1]*nums[i]
        print(prefixarr)
        for i in range(len(nums)-2,-1,-1):
            postfix[i]= postfix[i+1]*nums[i]
        print(postfix)
        newarr=[0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                newarr[i]=postfix[i+1]
            elif i==len(nums)-1:
                newarr[i]=prefixarr[i-1]
            else:
                newarr[i]=prefixarr[i-1]*postfix[i+1]
        return newarr

